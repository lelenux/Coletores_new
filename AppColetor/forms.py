from django import formsfrom django.core.exceptions import ValidationErrorfrom .models import *class PessoasForm(forms.ModelForm):    class Meta:        model = CadastroPessoa        fields = ['nome', 'cracha']    def clean(self):        data = self.cleaned_data # cleaned_data contem todas as informações do meu form        cracha = data.get('cracha') # esta variavel pega as informações do cracha que peguei com o .get        operador_exists = CadastroPessoa.objects.filter(cracha=cracha).exists() # faço uma consulta no        # banco no campo cracha e passo o valor de cracha        if operador_exists:            raise ValidationError("Um usuário com este cracha já existe!")# Cria a validação se o            # valor do cracha já existe, se existir imprime a msg de erro.class ColetoresForm(forms.ModelForm):    class Meta:        model = Coletores        fields = ['codigo', 'model', 'marca', 'serial_number', 'status']    def clean(self):        data = self.cleaned_data        codigo = data.get('codigo')        codigo_exists = Coletores.objects.filter(codigo=codigo).exists()        if codigo_exists:            raise ValidationError("Um coletor com este código já existe!")class ControleForm(forms.ModelForm):    cracha = forms.CharField()    nome = forms.CharField(required=False)    serial = forms.CharField(required=False)    marca = forms.CharField(required=False)    codigo = forms.CharField()    coletor = forms.IntegerField(required=False)    userretirada = forms.IntegerField(required=False)    operador = forms.IntegerField(required=False)    class Meta:        model = Controle        fields = '__all__'    def clean(self):        data = self.cleaned_data        cracha = data.get('cracha')        codigo = data.get('codigo')        operador_is_pending = Controle.objects.filter(operador__cracha=cracha, dtentrega__isnull=True)        if operador_is_pending:            raise ValidationError("Este operador já retirou um coletor!")        coletor_is_pending = Controle.objects.filter(coletor__codigo=codigo, dtentrega__isnull=True)        if coletor_is_pending:            raise ValidationError("Este coletor já está em uso por outro operador!")        coletor = Coletores.objects.filter(codigo=codigo).first()        if coletor and coletor.status != Coletores.NORMAL:            raise ValidationError(f'Este coletor no momento esta com o seguinte status: "{coletor.get_status_display()}"')## class DateInput(forms.DateInput):#     input_type = 'date'### class ExampleForm(forms.Form):#     my_date_field = forms.DateField(widget=DateInput)### class ExempleModelForm(forms.Form):#     class Meta:#         widgets = {'my_date_field': DateInput()}###