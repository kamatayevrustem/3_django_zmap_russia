from django.shortcuts import render
import csv


def inflation_view(request):
    template_name = 'inflation.html'

    # чтение csv-файла и заполнение контекста
    with open("inflation_russia.csv", encoding='utf8') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=';')
        data = list(reader)
        context = {'rows': data}

    return render(request, template_name, context)
