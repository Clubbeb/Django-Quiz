from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import authenticate, login, logout

from .forms import RegistroFormulario, UsuarioLoginFormulario

from .models import QuizUsuario, Pregunta, PreguntasRespondidas

import matplotlib.pyplot as plt

import sqlite3

#from .nose import *
#print(feliz)
'''''
def inicio(request):

	context = {

		'bienvenido': 'Bienvenido'

	}

	return render(request, 'inicio.html', context)
'''''
def index(request):
	return render(request, 'nosotros/p1.html')
def p2(request):
	return render(request, 'nosotros/p2.html')
def p3(request):
	return render(request, 'nosotros/p3.html')
def p4(request):
	return render(request, 'nosotros/p4.html')

def HomeUsuario(request):

	return render(request, 'Usuario/home.html')


def tablero(request):
	total_usaurios_quiz = QuizUsuario.objects.order_by('-puntaje_total')[:10]
	contador = total_usaurios_quiz.count()

	context = {

		'usuario_quiz':total_usaurios_quiz,
		'contar_user':contador
	}

	return render(request, 'play/tablero.html', context)

def jugar(request):

	QuizUser, created = QuizUsuario.objects.get_or_create(usuario=request.user)

	if request.method == 'POST':
		pregunta_pk = request.POST.get('pregunta_pk')
		pregunta_respondida = QuizUser.intentos.select_related('pregunta').get(pregunta__pk=pregunta_pk)
		respuesta_pk = request.POST.get('respuesta_pk')

		try:
			opcion_selecionada = pregunta_respondida.pregunta.opciones.get(pk=respuesta_pk)
		except ObjectDoesNotExist:
			raise Http404

		QuizUser.validar_intento(pregunta_respondida, opcion_selecionada)

		return redirect('resultado', pregunta_respondida.pk)

	else:
		pregunta = QuizUser.obtener_nuevas_preguntas()
		if pregunta is not None:
			QuizUser.crear_intentos(pregunta)

		context = {
			'pregunta':pregunta
		}

	return render(request, 'play/jugar.html', context)



def resultado_pregunta(request, pregunta_respondida_pk):
	respondida = get_object_or_404(PreguntasRespondidas, pk=pregunta_respondida_pk)

	context = {
		'respondida':respondida
	}
	return render(request, 'play/resultados.html', context)

def loginView(request):
	titulo = 'login'
	form = UsuarioLoginFormulario(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		usuario = authenticate(username=username, password=password)
		login(request, usuario)
		return redirect('HomeUsuario')

	context = {
		'form':form,
		'titulo':titulo
	}

	return render(request, 'Usuario/login.html', context)

def registro(request):

	titulo = 'Crear una Cuenta'
	if request.method == 'POST':
		form = RegistroFormulario(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
	else:
		form = RegistroFormulario()

	context = {

		'form':form,
		'titulo': titulo

	}

	return render(request, 'Usuario/registro.html', context)


def logout_vista(request):
	logout(request)
	return redirect('/')

def bars(request):
    	
    feliz = 1
    triste = 1
    enojado = 1
    indiferente = 1
    x = []
    con = sqlite3.connect("C:/Users/clubb/OneDrive/Documentos/GitHub/Django-Quiz/db.sqlite3")
    cur = con.cursor()
    for row in cur.execute('SELECT * FROM Quiz_quizusuario'):
        x.append(row[1])
    con.close()
    for valor in x:
        if valor == 10:
            feliz += 1 
        elif valor == 5:
            triste += 1
        elif valor == 3:
            enojado += 1
        elif valor == 0:
            indiferente += 1
        elif valor == 15:
            feliz += 1
            triste += 1
        elif valor == 8:
            triste += 1
            enojado += 1
        elif valor == 13:
            feliz += 1
            enojado += 1
        elif valor == 18:
            feliz +=1
            triste +=1
            enojado +=1
    
    names = 'Triste', 'Enojado', 'Indiferente', 'Feliz',
    size = [triste, enojado, indiferente, feliz]
    fig = plt.figure()
    fig.patch.set_facecolor('#337294')
    plt.rcParams['text.color'] = 'white'
    plt.pie(size, labels=names)
    plt.title("Sentimientos Totales")
    plt.savefig("template/STATIC/grafico.png")
    return render(request,'charts.html')

def table(request):
  return render(request,"tablero.html")


