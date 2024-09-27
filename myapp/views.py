from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
# pages of Automatisme

def Automatismelast(request):
    return render(request, 'productsfiles/Automatismelast.html')

def BorneEscamotable(request):
    return render(request, 'productsfiles/sub-product/Automatisme/BorneEscamotable.html')
def Portails(request):
    return render(request, 'productsfiles/sub-product/Automatisme/Portails.html')
def Portes(request):
    return render(request, 'productsfiles/sub-product/Automatisme/Portes.html')
def RideauxMetalliquesMotorises(request):
    return render(request, 'productsfiles/sub-product/Automatisme/RideauxMetalliquesMotorises.html')
def SystemesAutomatisationPergolas(request):
    return render(request, 'productsfiles/sub-product/Automatisme/SystemesAutomatisationPergolas.html')
def SystemescontroleAcces(request):
    return render(request, 'productsfiles/sub-product/Automatisme/SystemescontroleAcces.html')
def Systemesgestionparking(request):
    return render(request, 'productsfiles/sub-product/Automatisme/Systemesgestionparking.html')
def SystemesVoletsBattants(request):
    return render(request, 'productsfiles/sub-product/Automatisme/SystemesVoletsBattants.html')
def VoletsRoulants(request):
    return render(request, 'productsfiles/sub-product/Automatisme/VoletsRoulants.html')

def testfile(request):
    return render(request, 'productsfiles/testfile.html')
# MENUISERIE ALUMINIUM
def MENUISERIEALUMINIUM(request):
    return render(request, 'productsfiles/MENUISERIEALUMINIUM.html')

def portesfenetre(request):
    return render(request, 'productsfiles/sub-product/MenuiserieAluminium/portesfenetre.html')
def baiesvitre(request):
    return render(request, 'productsfiles/sub-product/MenuiserieAluminium/baiesvitre.html')
def Brisesoleil(request):
    return render(request, 'productsfiles/sub-product/MenuiserieAluminium/Brisesoleil.html')
def Cloisonsamovibles(request):
    return render(request, 'productsfiles/sub-product/MenuiserieAluminium/Cloisonsamovibles.html')
def CloturesPortails(request):
    return render(request, 'productsfiles/sub-product/MenuiserieAluminium/CloturesPortails.html')
def Fenetres(request):
    return render(request, 'productsfiles/sub-product/MenuiserieAluminium/Fenetres.html')
def alGardecorps(request):
    return render(request, 'productsfiles/sub-product/MenuiserieAluminium/alGardecorps.html')
def Pergolas(request):
    return render(request, 'productsfiles/sub-product/MenuiserieAluminium/Pergolas.html')
def Portes(request):
    return render(request, 'productsfiles/sub-product/MenuiserieAluminium/Portes.html')
def Verrieres(request):
    return render(request, 'productsfiles/sub-product/MenuiserieAluminium/Verrieres.html')
def Volets(request):
    return render(request, 'productsfiles/sub-product/MenuiserieAluminium/Volets.html')
# pages of Menuiserie Façade
def MenuiserieFaçade(request):
    return render(request, 'productsfiles/MenuiserieFaçade.html')

def Alucobond(request):
    return render(request, 'productsfiles/sub-product/MenuiserieFaçade/Alucobond.html')
def vea(request):
    return render(request, 'productsfiles/sub-product/MenuiserieFaçade/vea.html')
def DoublePeau(request):
    return render(request, 'productsfiles/sub-product/MenuiserieFaçade/DoublePeau.html')
def MurRideau(request):
    return render(request, 'productsfiles/sub-product/MenuiserieFaçade/MurRideau.html')
#Menuiserie Métalliquelast
def MenuiserieMétalliquelast(request):
    return render(request, 'productsfiles/MenuiserieMétalliquelast.html')
def CloturesMetalliques(request):
    return render(request, 'productsfiles/sub-product/MenuiserieMetallique/CloturesMetalliques.html')
def CoupeFeu(request):
    return render(request, 'productsfiles/sub-product/MenuiserieMetallique/CoupeFeu.html')
def EscaliersMetalliques(request):
    return render(request, 'productsfiles/sub-product/MenuiserieMetallique/EscaliersMetalliques.html')
def FenetresMetalliques(request):
    return render(request, 'productsfiles/sub-product/MenuiserieMetallique/FenetresMetalliques.html')
def Gardecorps(request):
    return render(request, 'productsfiles/sub-product/MenuiserieMetallique/Gardecorps.html')
def PortailsMetalliques(request):
    return render(request, 'productsfiles/sub-product/MenuiserieMetallique/PortailsMetalliques.html')
def PortesMetalliques(request):
    return render(request, 'productsfiles/sub-product/MenuiserieMetallique/PortesMetalliques.html')
def RideauxGrilles(request):
    return render(request, 'productsfiles/sub-product/MenuiserieMetallique/RideauxGrilles.html')
def prod(request):
    return render(request, 'productsfiles/prod.html')
def slidesfile(request):
    return render(request, 'basefiles/slidesfile.html')
def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
