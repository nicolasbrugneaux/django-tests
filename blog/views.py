# Create your views here.
#-*- coding: utf-8 -*-
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.shortcuts import redirect
from blog.models import *
from blog.forms import *
from django.views.generic import TemplateView

def faq(request):
	return render(request, 'blog/faq.html')

def read(request, id, slug):
	article = get_object_or_404(Article, id=id)
	return render(request, 'blog/view_article.html', {'article':article})

def contact(request):
	if request.method == 'POST':			# S'il s'agit d'une requête POST
		form = ContactForm(request.POST)	# On reprend les données
		if form.is_valid():					# On vérifie que les données envoyées sont valides

			# Ici on peut traiter les données du formulaire
			sujet = form.cleaned_data['sujet']
			message = form.cleaned_data['message']
			envoyeur = form.cleaned_data['envoyeur']
			renvoi = form.cleaned_data['renvoi']

			destinataires = ['webmaster@localhost:8000']
		if renvoi:
			destinataires.append(envoyeur)

		# On envoie le mail grâce à une fonction fourni par Django
		from django.core.mail import send_mail
		send_mail(sujet, message, envoyeur, destinataires)

		return HttpResponseRedirect('/merci-contact/')	# On redirige l'utilisateur vers une page de confirmation
	else:	# Si c'est pas du POST, c'est probablement une requête GET
		form = ContactForm()	# On crée un formulaire vide

		return render(request, 'blog/contact.html', {'form': form,})	# On envoie le template avec le formulaire qu'on a construit plus haut


def home(request):
	articles = Article.objects.all()
	return render(request, 'blog/home.html', {'derniers_articles':articles})