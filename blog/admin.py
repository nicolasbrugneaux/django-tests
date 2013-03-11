# -*- coding:utf8 -*-
from django.contrib import admin
from blog.models import *
class CategorieAdmin(admin.ModelAdmin):
    # Configuration de la liste d'articles
    list_display   = ('nom','id')
    list_filter    = ('nom','id')
    search_fields  = ('nom','id')

class ArticleAdmin(admin.ModelAdmin):
 
    # Configuration de la liste d'articles
    list_display   = ('titre', 'categorie', 'auteur', 'date')
    list_filter    = ('auteur','categorie', )
    date_hierarchy = 'date'
    ordering       = ('date', )
    search_fields  = ('titre', 'contenu')
 
    # Configuration du formulaire d'édition
    fieldsets = (
        # Fieldset 1 : Meta-info (titre, auteur...)
       ('Général', {
            'classes': ['collapse',],
            'fields': ('titre', 'slug', 'auteur', 'categorie')
        }),
        # Fieldset 2 : Contenu de l'article
        ('Contenu de l\'article', {
           'description': 'Le formulaire accepte les balises HTML. Utilisez-les à bon escient !',
           'fields': ('contenu', )
        }),
    )
    prepopulated_fields = {'slug': ('titre', ), }
 
    # Colonnes personnalisées 
    def apercu_contenu(self, article):
        """ 
        Retourne les 40 premiers caractères du contenu de l'article. Si il
        y a plus de 40 caractères, on rajoute des points de suspension """
        text = article.contenu[0:40]
        if len(article.contenu) > 40:
            return '%s...' % text
        else:
            return text
 
    apercu_contenu.short_description = 'Aperçu du contenu'

class CommentAdmin(admin.ModelAdmin):
 
    # Configuration de la liste d'articles
    list_display   = ('article', 'auteur', 'date')
    list_filter    = ('article','date', )
    date_hierarchy = 'date'
    ordering       = ('date', )
    search_fields  = ('auteur', 'contenu')
 
 
    # Colonnes personnalisées 
    def apercu_contenu(self, comment):
        """ 
        Retourne les 40 premiers caractères du contenu du commentaire. Si il
        y a plus de 40 caractères, on rajoute des points de suspension """
        text = comment.contenu[0:40]
        if len(comment.contenu) > 40:
            return '%s...' % text
        else:
            return text
 
    apercu_contenu.short_description = 'Aperçu du contenu'

admin.site.register(Categorie, CategorieAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
