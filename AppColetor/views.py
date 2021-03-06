from .forms import *
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from datetime import datetime, timedelta
from django.utils import timezone
from datetime import datetime
from django.db.models import Q

@login_required
def listar_controles(request, template_name="home.html"):
    busca = request.GET.get("busca")  #Pego o conteudo do campo busca do html

    if busca:
        coletores = Controle.objects.filter(Q(coletor__codigo=busca) | Q(operador__cracha=busca)).all()
        return render(request, 'home.html', {'lista': coletores}) # Realiza a pesquisa no banco e traz o valor em home.html

    coletores = Controle.objects.filter(dtentrega__isnull=True).all() #caso branco traz todos disponiveis

    return render(request, template_name, {'lista': coletores})


@login_required
def adduser(request):
    form_user = PessoasForm(request.POST, None)
    if form_user.is_valid():
        form_user.save()
        return redirect('listar_controles')
    return render(request, 'user_new.html', {'form': form_user})


@login_required
def addcoletor(request):
    form_coletor = ColetoresForm(request.POST, None)
    if form_coletor.is_valid():
        form_coletor.save()
        return redirect('listar_controles')
    return render(request, 'coletor_new.html', {'form': form_coletor})

@login_required
def controle(request):
    form_controle = ControleForm(request.POST, None)

    if form_controle.is_valid():
        data = form_controle.cleaned_data
        operador = CadastroPessoa.objects.get(cracha=data.get("cracha"))
        coletor = Coletores.objects.get(codigo=data.get("codigo"))
        doc = form_controle.save(commit=False)
        doc.operador = operador
        doc.coletor = coletor
        doc.userretirada = request.user
        doc.save()
        # form_controle.save()
        return redirect('listar_controles')
    return render(request, 'controle.html', {'form': form_controle})


def search_user(request, cracha):
    pessoa = get_object_or_404(CadastroPessoa, cracha=cracha)
    return JsonResponse(model_to_dict(pessoa))


def search_coletor(request, codigo):
    coletor = get_object_or_404(Coletores, codigo=codigo)
    data = {'marca': coletor.get_marca_display(), 'serial_number': coletor.serial_number}
    return JsonResponse(data)


@login_required
def coletor_retirada(request, id):
    coletor = get_object_or_404(Controle, pk=id)
    coletor.dtretirada = None
    coletor.userretirada = None
    coletor.save()
    return redirect('listar_controles')


@login_required
def coletor_update(request, id):
    coletor = get_object_or_404(Controle, pk=id)
    coletor.dtentrega = None
    coletor.userentrega = None
    coletor.save()
    return redirect('listar_controles')

@login_required
def status_coletor_update(request, id): # Recebe a reposta da pesquisa + o ID.
    coletor = get_object_or_404(Coletores, pk=id) # Tenta recuperar o objeto que o usuario esta tentando, se não ele retorna o erro de 404 de dado que não exsite)
    # Pego o ID no banco pelo "pk é o ID de cada código do coletor no banco"
    form = ColetoresForm(request.POST or None, instance=coletor) # instanciando o form se Or None(se tiver alguma coisa no banco
    # ele já instancia se não cria um novo, No instance é o valor recuperado da consulta, ou seja o form já inicia com uma instancia do ID.)

    if form.is_valid():
        form.save()
        return redirect('coletores_list')
    return render(request, 'coletor_new.html', {"form": form})

@login_required
def observacao(request, id):
    controle = get_object_or_404(Controle, pk=id)
    form_controle = ControleForm(request.POST or None, instance=controle)
    if form_controle.is_valid():
        data = form_controle.cleaned_data
        operador = CadastroPessoa.objects.get(cracha=data.get("cracha"))
        coletor = Coletores.objects.get(codigo=data.get("codigo"))
        doc = form_controle.save(commit=False)
        doc.operador = operador
        doc.coletor = coletor
        doc.dtentrega = timezone.now()
        doc.userentrega = request.user
        doc.userretirada = request.user
        doc.save()
        return redirect('listar_controles')
    return render(request, 'controle.html',  {"form": form_controle, "entrega": True})

@login_required
def voltar_coletor(request, id):
    coletor = get_object_or_404(Controle, pk=id)
    coletor.dtentrega = None
    coletor.save()
    return redirect('listar_controles')


@login_required
def entrega_coletor(request, id):
    coletor = get_object_or_404(Controle, pk=id)
    coletor.dtentrega = timezone.now()
    coletor.userentrega = request.user
    coletor.save()
    return redirect('listar_controles')

@login_required
def history(request, template_name='list_control.html'):
    dtinicial = request.GET.get("dtinicial")
    dtfinal = request.GET.get("dtfinal")
    if dtinicial and dtfinal:
        dtinicial = f"{dtinicial} 00:00:00"
        dtfinal = f"{dtfinal} 23:59:59"
        dt = Controle.objects.filter(dtretirada__gte=dtinicial, dtretirada__lte=dtfinal)

        return render(request, template_name, {'dados': dt})

    dados = Controle.objects.all().order_by("dtretirada")
    return render(request, 'list_control.html', {'dados': dados})

@login_required
def listar_coletores(request):
    busca = request.GET.get("busca")
    if busca:
        coletor = Coletores.objects.filter(codigo=busca)
        return render(request, 'coletores_list.html', {'dados': coletor})

    coletor = Coletores.objects.all()
    return render(request, 'coletores_list.html', {'dados': coletor})

@login_required
def status_users_update(request, id):
    user = get_object_or_404(CadastroPessoa, pk=id)
    form = PessoasForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        return redirect('listar_users')
    return render(request, 'user_new.html', {"form": form})

@login_required
def listar_users(request):
    busca = request.GET.get("busca")
    if busca:
        user = CadastroPessoa.objects.filter(Q(nome__icontains=busca) | Q(cracha__icontains=busca)).all()
        return render(request, 'user_list.html', {'dados': user})
    user = CadastroPessoa.objects.all()
    return render(request, 'user_list.html', {'dados': user})

