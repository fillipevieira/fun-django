from django.forms import ModelForm
from .models import Transacao

# definindo um formulario
class TransacaoForm(ModelForm):
    class Meta:
        model = Transacao
        fields = ['data', 'descr', 'value', 'obs', 'categoria'] # definindo os campos do meu formulario