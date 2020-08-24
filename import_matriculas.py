import csv
import os
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Coletor.settings')
django.setup()


from AppColetor.models import CadastroPessoa


def csv_to_list(filename: str) -> list:
    with open(filename) as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        next(reader)
        csv_data = [line for line in reader]
    return csv_data


def save_data(data):
    aux = []
    for item in data:
        nome, cracha = item

        obj = CadastroPessoa(
            nome=nome,
            cracha=cracha,
        )
        aux.append(obj)
    CadastroPessoa.objects.bulk_create(aux)


data = csv_to_list('/home/lelenux/Área de Trabalho/cadas.csv')
save_data(data)