from pandas import isnull
from random import randint
from meteoapp import data
import pandas as pd
import openpyxl

# список даних обраного міста та місяця
def create_data_list(i, city):
    months_value = 'meteoapp/cities/' + city + '/' + data.months_dict[i]
    wb = openpyxl.reader.excel.load_workbook(filename=months_value, data_only=True)
    wb.active = 0
    wc = wb.active
    rows = []
    for i in range(1400):
        r = []
        rows.append(r)
    i = 1
    for row in rows:
        for col_name in data.col_names:
            row.append(wc[col_name + str(i)].value)
        i += 1
    return rows

# мовна локалізація (переклад)
def lan_localisation(lan, lan1, i, city):
    months_value = 'meteoapp/cities/' + city + '/' + data.months_dict[i]
    wb = openpyxl.reader.excel.load_workbook(filename=months_value, data_only=True)
    wb.active = 0
    wc = wb.active
    wc['A1'] = data.column1_tr[lan1]
    for i in range(2, 1440):
        for j in range(9):
            if wc['D' + str(i)].value == data.wind_tr[lan][j]:
                wc['D' + str(i)] = data.wind_tr[lan1][j]
    wb.save(months_value)

# корекція даних
def data_correction(i, city, interp_method, interp_value):
    months_value = 'meteoapp/cities/' + city + '/' + data.months_dict[i]
    wb = openpyxl.reader.excel.load_workbook(filename=months_value, data_only=True)
    wb.active = 0
    wc = wb.active
    columns = data_interpolation(wc, interp_method, interp_value) # інтерполяція даних

    # запис в бд
    for i in range(2, 1440):
        if isnull(wc['F' + str(i)].value): # заповнення порожніх полей колонки ww позначенням CL - тобто, "без явищ"
            wc['F' + str(i)] = 'CL'
        if isnull(wc['D' + str(i)].value): # напрям вітру
            if i != 2: # у порожніх полях вказується напрям за попереднє число місяця
                wc['D' + str(i)] = wc['D' + str(i-1)].value
            else: # першому елементу таблиці надається напрям за найближче наступне число місяця
                for j in range(2, 1439):
                    if not isnull(wc['D' + str(j)].value):
                        wc['D' + str(i)] = wc['D' + str(j)].value
                        break
        wc['I' + str(i)] = randint(0, 100)
        wc['G' + str(i)] = columns[0][i]
        wc['K' + str(i)] = columns[1][i]


    wb.save(months_value)

# інтерполяція даних
def data_interpolation(wc, interp_method, interp_value):
    columns = []
    for i in range(2):
        c = []
        columns.append(c)
    i = 0
    for column in columns:
        for wc_item in wc[data.ic_names[i]]:
            column.append(wc_item.value)
        i += 1
    for i in range(2):
        columns[i].pop(0)
    for i in range(2):
        ic = pd.Series(columns[i])
        if isnull(ic[0]):
            ic[0] = round(ic.mean())
        if interp_method == 'linear':
            ic = round(ic.interpolate())
        if interp_method == 'polynomial':
            ic = round(ic.interpolate(method=interp_method, order=interp_value))
        if interp_method == 'pad':
            ic = round(ic.interpolate(method=interp_method, limit=interp_value))
        columns[i] = ic
    return columns