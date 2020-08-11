from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class CadastroPessoa(models.Model):
    nome = models.CharField(max_length=100)
    cracha = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.nome}"


class Coletores(models.Model):
    NORMAL = 'no'

    STATUS = (
        ('fo', 'Fornecedor'),
        ('co', 'Condenado'),
        ('de', 'Defeito'),
        ('ma', 'Manutenção'),
        (NORMAL, 'Normal')
    )
    MARCA = (
        ('mo', 'Motorola'),
        ('in', 'Intermec'),
        ('ro', 'Honeywell')
    )

    codigo = models.CharField(max_length=50)
    model = models.CharField(max_length=15)
    marca = models.CharField(max_length=30, choices=MARCA)
    serial_number = models.CharField(max_length=20)
    status = models.CharField(max_length=30, choices=STATUS)

    def __str__(self):
        return f"{self.codigo}"

    @property
    def display_marca(self):
        return self.get_marca_display()


class Controle(models.Model):
    operador = models.ForeignKey(CadastroPessoa, on_delete=models.PROTECT)
    coletor = models.ForeignKey(Coletores, on_delete=models.PROTECT)
    userretirada = models.ForeignKey(User, related_name='usercadastro', on_delete=models.PROTECT)
    dtretirada = models.DateTimeField(auto_now_add=True)
    dtentrega = models.DateTimeField(null=True, blank=True)
    userentrega = models.ForeignKey(User, related_name='userentrega', null=True, blank=True, on_delete=models.PROTECT)
    observacao = models.TextField(null=True, blank=True)

    # def __str__(self):
    #     return f"{self.operador} - {self.coletor}"

