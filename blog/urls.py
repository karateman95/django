from django.urls import path
from . import views

urlpatterns = [
    path('accueil', views.home),
    path('article/<id_article>', views.view_article),
	path('article/<int:year>/<int:month>', views.list),
	path('date', views.date_actuelle),
	path('addition/<int:nombre1>/<int:nombre2>', views.addition),
]