from django.db import models
from django.contrib.auth.models import User


class Tonners(models.Model):
    descricao = models.CharField(max_length=25, verbose_name='Descrição')
    quantidade = models.PositiveIntegerField(default=0)
    ultimaAlteracao = models.DateTimeField(auto_now=True, verbose_name='Ultima Alteração')

    def __str__(self):
        return self.descricao

    def get_ultimaAlteracao(self):
        return self.ultimaAlteracao.strftime('%d/%m/%Y %H:%M')

    class Meta:
        verbose_name = 'Tonner'
        verbose_name_plural = 'Tonners'


class Empresa(models.Model):
    empresa = models.CharField(max_length=50, verbose_name='Empresa')

    def __str__(self):
        return self.empresa

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'


class Setor(models.Model):
    setor = models.CharField(max_length=30, verbose_name='Setor')

    def __str__(self):
        return self.setor

    class Meta:
        verbose_name = 'Setor'
        verbose_name_plural = 'Setores'


class Categoria(models.Model):
    categoria = models.CharField(max_length=30, verbose_name='Categoria')

    def __str__(self):
        return self.categoria

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'


class Abertura(models.Model):
    A = 'Aberto'
    AN = 'Andamento'
    C = 'Concluido'
    CHOICE_STATUS = (
        (A, 'ABERTO'),
        (AN, 'ANDAMENTO'),
        (C, 'CONCLUIDO')
    )
    status = models.CharField(max_length=9, choices=CHOICE_STATUS, default='ABERTO')
    # numTicket = models.PositiveIntegerField(primary_key=True, unique=True, auto_created=True, db_index=True,help_text='Identificação do Chamado',)
    empresa = models.ForeignKey(Empresa, on_delete=models.DO_NOTHING, default=1)
    setor = models.ForeignKey(Setor, on_delete=models.DO_NOTHING)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    tecnico = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="abertura_tecnico")
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    descricao = models.TextField(max_length=250)
    # descricaoCancelamento = models.TextField(max_length=250, blank=True, null=True)
    descricaoTecnico = models.TextField(max_length=250, blank=True, null=True)
    dataAbertura = models.DateTimeField(auto_now_add=True)
    dataUltimaAlteracao = models.DateTimeField(auto_now=True)
    dataFechamento = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{str(self.usuario)}'

    def get_dataAbertura(self):
        return self.dataAbertura.strftime('%d/%m/%Y %H:%M:%S')

    def get_dataUltimaAlteracao(self):
        return self.dataUltimaAlteracao.strftime('%d/%m/%Y %H:%M:%S')

    def get_dataFechamento(self):
        if self.status == 'CONCLUIDO':
            return self.dataFechamento.strftime('%d/%m/%Y %H:%M:%S')
        else:
            pass

    class Meta:
        verbose_name = 'Abertura'
        verbose_name_plural = 'Aberturas'






