from django.db import models
from django.core.urlresolvers import reverse 

# Create your models here.
class Categorie(models.Model):
    nom = models.CharField(max_length=30)
 
    def __unicode__(self):
        return self.nom

class Article(models.Model):
    titre = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    auteur = models.CharField(max_length=42)
    contenu = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de parution")
    categorie = models.ForeignKey(Categorie)

    def __unicode__(self):
        return self.titre
    def __getID__(self):
        return self.id
    def get_absolute_url(self):
        path = reverse('read', args=[self.slug])
        return "http://%s%s" % (self.site, path)

class Comment(models.Model):
	auteur = models.CharField(max_length=42)
	contenu = models.TextField(null=True)
	date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date du commentaire")
	article = models.ForeignKey(Article)
