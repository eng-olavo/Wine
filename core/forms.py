from django import forms


class VinhoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    cor = forms.CharField(label='Cor', max_length=20)
    uva = forms.CharField(label='Uva', max_length=20)
    acucar = forms.CharField(label='Teor de Açucar', max_length=20)
    safra = forms.IntegerField(label='Safra')
    nacionalidade = forms.CharField(label='Nacionalidade', max_length=20)
    vinicula = forms.CharField(label='Vinícula', max_length=20)
    alcool = forms.DecimalField(label='Teor de Álcool', max_digits=3, decimal_places=1)
    volume = forms.IntegerField(label='Volume')
    reserva = forms.BooleanField(label='Reserva')
    tonalidade = forms.ImageField(label='Tonalidade', upload_to='produtos', variations={'thumb': (124, 124)})
    img_rotulo = forms.ImageField(label='Rótulo', upload_to='produtos', variations={'thumb': (124, 124)})
    img_garrafa = forms.ImageField(label='Garrafa', upload_to='produtos', variations={'thumb': (256, 256)})
    descricao = forms.CharField(label='descrição', widget=forms.Textarea())
    preco = forms.DecimalField(label='Preço', max_digits=8, decimal_places=2)
    promocao = forms.DecimalField(label='Promoção', max_digits=8, decimal_places=2)
    estoque = forms.IntegerField(label='Estoque')
    avaliacao = forms.IntegerField(label='Avaliação')
    num_avaliacoes = forms.IntegerField(label='Número de avaliações')
    destaque = forms.BooleanField(label='Destaque',initial=False)
