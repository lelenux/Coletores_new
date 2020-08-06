import csv
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Coletor.settings')
django.setup()


from AppColetor.models import Coletores


def csv_to_list(filename: str) -> list:
    with open(filename) as csv_file:
        reader = csv.reader(csv_file, delimiter='\t')
        next(reader)
        csv_data = [line for line in reader]
    return csv_data


def save_data(data):
    aux = []
    for item in data:
        marca, model, serial_number, codigo, status = item
        print(marca, model, serial_number, codigo, status)

        obj = Coletores(
            marca=marca,
            model=model,
            serial_number=serial_number,
            codigo=codigo,
            status=status,
        )
        aux.append(obj)
    Coletores.objects.bulk_create(aux)


data = csv_to_list('/home/lelenux/Área de Trabalho/coletores.csv')
save_data(data)