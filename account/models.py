from django.db import models

# criando meus modelos de tabela
class Categoria(models.Model):
    name = models.CharField(max_length=100)
    creation = models.DateTimeField(auto_now_add=True)

    # definindo como será listado
    def __str__(self):
        return self.name


class Transacao(models.Model):
    data = models.DateTimeField()
    descr = models.CharField(max_length=200)
    value = models.DecimalField(max_digits=7, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    obs = models.TextField(null=True, blank=True)

    # definindo como sera o plural
    class Meta:
        verbose_name_plural = 'Transacoes'

    # definindo como será listado
    def __str__(self):
        return self.descr
