#-*- coding: utf-8 -*-
import os
os.environ['DJANGO_SETTINGS_MODULE']='myFirstProject.settings'
from blog.models import *

Comment(auteur = "Nicolas", contenu="", article=Article.objects.order_by('date').reverse()[0]).save()

"""
cat = Categorie(nom="TEST")
cat.save()

Article(auteur="Nicolas",titre="HelloWorld",slug="un-premier-article", contenu="'sup bros ?'", categorie=cat).save()
Article(auteur="Nicolas",titre="Nope",slug="image-no", contenu="<img src='NO.gif'/>",categorie=cat).save()
art = Article()
art.titre="plop"
art.auteur="Nicolas"
art.contenu="whoop"
art.slug="whoooop-whoooop"
art.categorie = cat
art.save()
"""