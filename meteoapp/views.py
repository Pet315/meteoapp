from django.shortcuts import render
from meteoapp import main
# from meteoapp import models
# from pandas import isnull

def index(request):
    return render(request, 'index.html')


def show_db(request):
    city = request.POST['city']
    id = int(request.POST['id'])
    lan1 = int(request.POST['lan'])
    interp_method = request.POST['interp_method']
    interp_value = request.POST['interp_value']

    if interp_method != 'linear':
        interp_value = int(interp_value)
        if interp_value<2:
            return render(request, 'index.html')

    lan = 0
    if lan1 == 0:
        lan = 1
    main.lan_localisation(lan, lan1, id-1, city)

    main.data_correction(id-1, city, interp_method, interp_value)

    rows = main.create_data_list(id-1, city)
    # context = {i: columns[i] for i in range(len(columns))}
    context = {'rows': rows}
    return render(request, 'show_db.html', context)

