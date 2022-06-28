import datetime

from pandas import isnull
import openpyxl
import pandas as pd
from meteoapp import data
# import string
# import numpy as np
# import statistics

if __name__ == '__main__':

    months_value = 'cities/' + 'kyiv' + '/' + data.months_dict[1]
    wb = openpyxl.reader.excel.load_workbook(filename=months_value, data_only=True)
    wb.active = 0
    wc = wb.active

    column = []

    for wc_item in wc['B']:
        column.append(wc_item.value)

    column.pop(0)

    a=1
    b=30
    for column_item in column:
        if column_item == datetime.time(a, b):
            print(column_item)
    print(column)


############################

    # for i in range(2):
    #     ic = pd.Series(columns[i])
    #     if (isnull(ic[0])):
    #         ic[0] = round(ic.mean())
    #     ic = round(ic.interpolate(method='polynomial', order=2))
    #     columns[i] = ic
    #
    # print(columns[0], '\n', columns[1])
    # wb.save(months_value)

############################

    # ic = pd.Series(columns[1])
    # ic[0] = ic.mean()
    # ic = ic.interpolate()
    # columns[1] =ic
    # print(columns[1])

    # a = pd.Series([0, 1, np.nan, 3, 4, 5, 7])
    # a[0] = round(a.mean())
    # print(a)
    # a = a.interpolate()
    # print(a)

############################

    # for column in columns:
    #     if (isnull(column[0])):
    #         df = pd.DataFrame(column)
    #         column[0] = round(df.mean())
    #     column = round(df.interpolate(method="linear"))

    # columns[0].interpolate()

    # df = pd.DataFrame(wc['G'])
    # wc['G'][0] = round(wc['G'].mean())

############################

    # i = 0
    # for column in columns:
    #     for j in range(1, 1489):
    #         column.append(wc[data.cor_col_names[i]][j].value)
    #         j += 1
    #     i += 1

    # context = {i: columns[i] for i in range(len(columns))}
    # print(context)

############################

    # мовна локалізація (переклад з російської на українську)
    # for i in range(12):
    #     break
    #     months_value = months.months_dict[months_keys_list[i]]
    #     wb = openpyxl.reader.excel.load_workbook(filename=months_value, data_only=True)
    #     wb.active = 0
    #     wc = wb.active
    #     wc['A1'] = "Число місяця"
    #     for i in range(2, 1490):
    #         if wc['D' + str(i)].value == "Западный":
    #             wc['D' + str(i)] = "Західний"
    #         if wc['D' + str(i)].value == "Южный":
    #             wc['D' + str(i)] = "Південний"
    #         if wc['D' + str(i)].value == "Северный":
    #             wc['D' + str(i)] = "Північний"
    #         if wc['D' + str(i)].value == "Восточный":
    #             wc['D' + str(i)] = "Східний"
    #         if wc['D' + str(i)].value == "Переменный":
    #             wc['D' + str(i)] = "Змінний"
    #         if wc['D' + str(i)].value == "Ю-З":
    #             wc['D' + str(i)] = "Пд-Зх"
    #         if wc['D' + str(i)].value == "С-З":
    #             wc['D' + str(i)] = "Пн-Зх"
    #         if wc['D' + str(i)].value == "Ю-В":
    #             wc['D' + str(i)] = "Пд-Сх"
    #         if wc['D' + str(i)].value == "С-В":
    #             wc['D' + str(i)] = "Пн-Сх"
    #
    #     # корекція даних
    #     # for i in range(2, 1490):
    #     #     if wc['D' + str(i)].value is None:
    #     #         corr = i
    #     #         fixed = wc['D' + str(i - 1)].value
    #     #         stop = False
    #     #         while stop is False:
    #     #             if str(wc['D' + str(i)].value) is None:
    #     #                 i += 1
    #     #             else:
    #     #                 stop = True
    #     #         limit = round((i + 1 - corr) / 2)
    #     #         for j in range(corr, limit):
    #     #             wc['D' + str(j)] = fixed
    #     #         for j in range(limit, i + 1):
    #     #             wc['D' + str(j)] = wc['D' + str(i + 1)].value
    #
    #     wb.save(months_value)