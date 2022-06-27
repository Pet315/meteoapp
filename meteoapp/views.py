from django.shortcuts import render
from meteoapp import main
# import matplotlib.pyplot as plt
from meteoapp.models import Actor


def index(request):
    error = ''
    error = {'error': error}
    return render(request, 'index.html', error)


def show_db(request):
    city = request.POST['city']
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
            error = 'Неправильно введений день (1-31)'
            error = {'error': error}
            return render(request, 'index.html', error)
    if hours != '':
        hours = int(hours)
        if hours < 0 or hours > 23:
            error = 'Неправильно введено кількість годин (0-23)'
            error = {'error': error}
            return render(request, 'index.html', error)
        if hours < 10:
            s_hours = '0' + str(hours)
            hours = s_hours
    if interp_method != 'linear':
        interp_value = int(interp_value)
        if interp_value<2:
            error = 'Неправильно введено межу/порядок інтерполяції (має бути більше 2)'
            error = {'error': error}
            return render(request, 'index.html', error)
    lan = 0
    if lan1 == 0:
        lan = 1

    # functions

    # lab 1
    wc = main.find_file(id-1, city)
    main.lan_localisation(lan, lan1, id-1, city)
    main.data_correction(id-1, city, interp_method, interp_value)
    rows = main.create_data_list(wc)

    # lab 2
    if day != '':
        if hours == '':
            rows = main.get_rows(rows, day)
        else:
            rows = main.get_rows(rows, day, str(hours), minutes)
    main.t_conditions(wc)
    rd_list = main.t_duration(wc)

    # output
    # context = {i: columns[i] for i in range(len(columns))}
    context = {'rows': rows, 'range': rd_list[0], 'duration': rd_list[1]}
    return render(request, 'show_db.html', context)