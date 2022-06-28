from django.shortcuts import render
from meteoapp import main
from meteoapp import data


def index(request, error=''):
    context = {'error': error}
    return render(request, 'index.html', context)


def show_db(request):
    id_city = int(request.POST['city'])
    id = int(request.POST['id'])
    lan1 = int(request.POST['lan'])
    interp_method = request.POST['interp_method']
    interp_value = request.POST['interp_value']
    day = request.POST['day']
    hours = request.POST['hours']
    minutes = str(request.POST['minutes'])

    # checking
    if day != '':
        day = int(day)
        if day < 1 or day > 31:
            return index(request, 'Неправильно введений день (1-31)')
    if hours != '':
        hours = int(hours)
        if hours < 0 or hours > 23:
            return index(request, 'Неправильно введено кількість годин (0-23)')
        if hours < 10:
            s_hours = '0' + str(hours)
            hours = s_hours
    if interp_method != 'linear':
        interp_value = int(interp_value)
        if interp_value<2:
            return index(request, 'Неправильно введено межу/порядок інтерполяції (має бути більше 2)')
    lan = 0
    if lan1 == 0:
        lan = 1

    # functions

    # lab 1
    city = data.cities_tr[0][id_city]
    wc = main.find_file(id, city)
    main.lan_localisation(lan, lan1, id, city)
    main.data_correction(id, city, interp_method, interp_value)
    rows = main.create_data_list(wc)

    # lab 2
    if day != '':
        if hours == '':
            rows = main.get_rows(rows, day)
        else:
            rows = main.get_rows(rows, day, str(hours), minutes)
    main.t_conditions(wc)
    rd_list = main.t_duration(wc)
    main.wind_rose(id, city, lan1)
    main.w_duration(wc)

    month = data.months_names[id]
    city = data.cities_tr[1][id_city]
    # output
    # context = {i: columns[i] for i in range(len(columns))}
    context = {'rows': rows, 't_range': rd_list[0], 't_duration': rd_list[1], 'month': month, 'city': city}
    return render(request, 'show_db.html', context)