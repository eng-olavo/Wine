from django.db import models

from stdimage.models import StdImageField


class Base(models.Model):
    criado = models.DateField('data de Criação', auto_now_add=True)
    modificado = models.DateField('data de Atualização', auto_now_add=True)
    ativo = models.BooleanField('ativo?', default=True)

    class Meta:
        abstract = True


class Vinho(Base):
    nome = models.CharField('Nome do Vinho',max_length=100)
    cor = models.CharField('Cor',max_length=20,default='Tinto', choices=(('T','Tinto'), ('R', 'Rose'), ('B', 'branco')))
    uva = models.CharField('Uva',max_length=20,default='Cabernet',
                           choices=(('CS', 'Cabernet Sauvignon'),
                                    ('CF', 'Cabernet Franc'),
                                    ('PN', 'Pinot Noir'),
                                    ('ME', 'Merlot'),
                                    ('MA', 'Malbec'),
                                    ('RS', 'Riesling'),
                                    ('TN', 'Tannat'),
                                    ('CH', 'Chardonnay')))
    acucar = models.CharField('Teor de Açucar',max_length=20, default='Seco',
                           choices=(('SC', 'Seco'),
                                    ('DS', 'Demi Sec'),
                                    ('SU', 'Suave'),
                                    ('DO', 'Doce'),
                                    ('NA', 'Nature'),
                                    ('EB', 'Extra Brut'),
                                    ('BR', 'Brut')))
    safra = models.IntegerField('Safra')
    nacionalidade = models.CharField('Nacionalidade',max_length=20, default='Brasil',
                           choices=(('BR', 'Brasil'),
                                    ('AR', 'Argentina'),
                                    ('UR', 'Uruguai'),
                                    ('CH', 'Chile'),
                                    ('PO', 'Portugal'),
                                    ('ES', 'Espanha'),
                                    ('FR', 'França'),
                                    ('IN', 'Inglaterra'),
                                    ('IT', 'Itália'),
                                    ('AL', 'Alemanha'),
                                    ('SU', 'Suiça'),
                                    ('EU', 'Estados Unidos'),
                                    ('AF', 'África do Sul'),
                                    ('AU', 'Austrália')))
    vinicula = models.CharField('Vinícula',max_length=20)
    alcool = models.DecimalField('Teor de Álcool', max_digits=3, decimal_places=1)
    volume = models.IntegerField('Volume')
    reserva = models.CharField('Reserva',max_length=20, default='Reserva',
                           choices=(('RE', 'Reserva'),
                                    ('NR', 'Não Reservado')))
    tonalidade = StdImageField('Tonalidade', upload_to='tonalidade', variations={'thumb': (124,124)})
    img_rotulo = StdImageField('Rótulo', upload_to='produto', variations={'thumb': (124,124)})
    img_garrafa = StdImageField('Garrafa', upload_to='garrafa', variations={'thumb': (256,256)})
    descricao = models.TextField('Descrição',blank=True, null=True)
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)
    promocao = models.DecimalField('Promoção', max_digits=8, decimal_places=2)
    estoque = models.IntegerField('Estoque')
    avaliacao = models.IntegerField('Avaliação')
    num_avaliacoes = models.IntegerField('Número de avaliações')
    destaque = models.BooleanField('Destaque', default=False)

    class Meta:
        db_table = 'vinho'

    def __str__(self):
        return self.nome


