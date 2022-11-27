from django.urls import path

from .views import *

urlpatterns = [
	
	#path('', inicio, name='inicio'),
	path('', index , name='index'),
	path('HomeUsuario/', HomeUsuario, name='HomeUsuario'),


	path('login/', loginView, name='login'),
	path('logout_vista/', logout_vista, name='logout_vista'),
	path('registro/', registro, name='registro'),
	path('tablero/', tablero, name='tablero'),

	
	path('jugar/', jugar, name='jugar'),
	path('resultado/<int:pregunta_respondida_pk>/', resultado_pregunta, name='resultado'),
 
	path('p2/', p2, name='p2'),
	path('p3/', p3, name='p3'),
	path('p4/', p4, name='p4'),
	path('bars/', bars, name='bars'),

]