# Create your views here.
#-*- coding: utf-8 -*-
from django.views.decorators.cache import cache_page

from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.shortcuts import redirect
from blog.models import *
from blog.forms import *
from django.views.generic import TemplateView

#@cache_page(60 * 15)
def faq(request):
	return render(request, 'blog/faq.html')

#@cache_page(60 * 15)
def read(request, id, slug):
	article = get_object_or_404(Article, id=id)
	return render(request, 'blog/view_article.html', {'article':article})

#@cache_page(60 * 15)
def contact(request):
	if request.method == 'POST':			# S'il s'agit d'une requête POST
		form = ContactForm(request.POST)	# On reprend les données
		if form.is_valid():					# On vérifie que les données envoyées sont valides
			# Ici on peut traiter les données du formulaire
			sujet = form.cleaned_data['subject']
			message = form.cleaned_data['message']
			envoyeur = form.cleaned_data['envoyeur']
			renvoi = form.cleaned_data['copy']

			destinataires = ['webmaster@example.com']
			if renvoi:
				destinataires.append(envoyeur)

			# On envoie le mail grâce à une fonction fourni par Django
			from django.core.mail import send_mail, BadHeaderError
			try:
				send_mail(sujet, message, envoyeur, destinataires)
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return HttpResponseRedirect('/')	# On redirige l'utilisateur vers une page de confirmation
		else:
			return render(request, 'blog/contact.html', {'form': form})
	else:	# Si c'est pas du POST, c'est probablement une requête GET
		form = ContactForm()	# On crée un formulaire vide

		return render(request, 'blog/contact.html', {'form': form,})	# On envoie le template avec le formulaire qu'on a construit plus haut

#@cache_page(60 * 15)
def home(request):
	articles = Article.objects.order_by('date').reverse()
	comments = Comment.objects.order_by('date','article').reverse()

	if request.method == 'POST':			# S'il s'agit d'une requête POST
		form = CommentForm(request.POST)	# On reprend les données
		if form.is_valid():					# On vérifie que les données envoyées sont valides
			# Ici on peut traiter les données du formulaire
			auteur = form.cleaned_data['author']
			comment = form.cleaned_data['comment']
			article_id = form.cleaned_data['article']

			Comment(auteur = auteur, contenu = comment, article = Article.objects.get(id=article_id)).save()
			form.cleaned_data['author'] = None
			form.cleaned_data['comment'] = None
			form.cleaned_data['article'] = None
			return HttpResponseRedirect('/')
		else:
			return render(request, 'blog/home.html', {'derniers_articles':articles, 'last':articles[0], 'comments':comments, 'form':form})
	else:	# Si c'est pas du POST, c'est probablement une requête GET
		form = CommentForm()	# On crée un formulaire vide

	return render(request, 'blog/home.html', {'derniers_articles':articles, 'last':articles[0], 'comments':comments, 'form':form})