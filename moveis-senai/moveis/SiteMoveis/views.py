from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    #verificar linha banner
    banner = Banner.objects.get()
    main = ConteudoMain.objects.get()
    card = CardProduct.objects.all()
    segundo = ConteudoSegundoMain.objects.get()
    card_segundo = CardSegundoMain.objects.all()
    tmain = ConteudoTerceiroMain.objects.get()
    tcard = CardTerceiroMain.objects.all()
    ct = CardTerceiro.objects.all()
    test = Testemunho.objects.all()
    return render(request,'index.html',{"banner": banner, "main": main, "produtos":card,\
        "segundo":segundo,"card":card_segundo,"tmain":tmain,"tcard":tcard,"ct":ct,"testemunho":test,"num":1})