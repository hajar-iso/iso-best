
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # path for automatis products 
    path("Automatismelast/",views.Automatismelast,name="Automatismelast"),
    path("Automatismelast/BorneEscamotable",views.BorneEscamotable,name="BorneEscamotable"),
    path("Automatismelast/Portails",views.Portails,name="Portails"),
    path("Automatismelast/Portes",views.Portes,name="Portes"),
    path("Automatismelast/RideauxMetalliquesMotorises",views.RideauxMetalliquesMotorises,name="RideauxMetalliquesMotorises"),
    path("Automatismelast/SystemesAutomatisationPergolas",views.SystemesAutomatisationPergolas,name="SystemesAutomatisationPergolas"),
    path("Automatismelast/SystemescontroleAcces",views.SystemescontroleAcces,name="SystemescontroleAcces"),
    path("Automatismelast/Systemesgestionparking",views.Systemesgestionparking,name="Systemesgestionparking"),
    path("Automatismelast/SystemesVoletsBattants",views.SystemesVoletsBattants,name="SystemesVoletsBattants"),
    path("Automatismelast/VoletsRoulants",views.VoletsRoulants,name="VoletsRoulants"),
    # MENUISERIE ALUMINIUM
    path("MENUISERIEALUMINIUM/",views.MENUISERIEALUMINIUM,name="MENUISERIEALUMINIUM"),
    path("MENUISERIEALUMINIUM/portesfenetre/",views.portesfenetre,name="portesfenetre"),
    path("MENUISERIEALUMINIUM/Brisesoleil/",views.Brisesoleil,name="Brisesoleil"),
    path("MENUISERIEALUMINIUM/CloturesPortails/",views.CloturesPortails,name="CloturesPortails"),
    path("MENUISERIEALUMINIUM/Fenetres/",views.Fenetres,name="Fenetres"),
    path("MENUISERIEALUMINIUM/alGardecorps/",views.alGardecorps,name="alGardecorps"),
    path("MENUISERIEALUMINIUM/Pergolas/",views.Pergolas,name="Pergolas"),
    path("MENUISERIEALUMINIUM/Portes/",views.Portes,name="Portes"),
    path("MENUISERIEALUMINIUM/portesfenetre/",views.portesfenetre,name="portesfenetre"),
    path("MENUISERIEALUMINIUM/Verrieres/",views.Verrieres,name="Verrieres"),
    path("MENUISERIEALUMINIUM/Volets/",views.Volets,name="Volets"),
    path("MENUISERIEALUMINIUM/Cloisonsamovibles/",views.Cloisonsamovibles,name="Cloisonsamovibles"),
    path("MENUISERIEALUMINIUM/baiesvitre/",views.baiesvitre,name="baiesvitre"),
    #MenuiserieFaçade
    path("MenuiserieFaçade/",views.MenuiserieFaçade,name="MenuiserieFaçade"),
    path("MenuiserieFaçade/Alucobond/",views.Alucobond,name="Alucobond"),
    path("MenuiserieFaçade/vea/",views.vea,name="vea"),
    path("MenuiserieFaçade/DoublePeau/",views.DoublePeau,name="DoublePeau"),
    path("MenuiserieFaçade/MurRideau/",views.MurRideau,name="MurRideau"),
    #MenuiserieMétalliquelast
    path("MenuiserieMétalliquelast/",views.MenuiserieMétalliquelast,name="MenuiserieMétalliquelast"),
    path("MenuiserieMétalliquelast/CloturesMetalliques",views.CloturesMetalliques,name="CloturesMetalliques"),
    path("MenuiserieMétalliquelast/CoupeFeu",views.CoupeFeu,name="CoupeFeu"),
    path("MenuiserieMétalliquelast/EscaliersMetalliques",views.EscaliersMetalliques,name="EscaliersMetalliques"),
    path("MenuiserieMétalliquelast/FenetresMetalliques",views.FenetresMetalliques,name="FenetresMetalliques"),
    path("MenuiserieMétalliquelast/Gardecorps",views.Gardecorps,name="Gardecorps"),
    path("MenuiserieMétalliquelast/PortailsMetalliques",views.PortailsMetalliques,name="PortailsMetalliques"),
    path("MenuiserieMétalliquelast/PortesMetalliques",views.PortesMetalliques,name="PortesMetalliques"),
    path("MenuiserieMétalliquelast/RideauxGrilles",views.RideauxGrilles,name="RideauxGrilles"),

    path("home/",views.home,name="home"),
    path("slidesfile/",views.slidesfile,name="slidesfile"),
    path("prod/",views.prod,name="prod"),
    path("about/",views.about,name="about"),
  

]