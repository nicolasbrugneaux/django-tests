from django import forms

class ContactForm(forms.Form):

	sujet = forms.CharField(max_length=100,required=True)
	sujet.widget.attrs.update({'class' : 'inputs'})

	message = forms.CharField(widget=forms.Textarea,required=True)
	message.widget.attrs.update({'class' : 'inputs'})

	envoyeur = forms.EmailField(label="Votre adresse mail",required=True)
	envoyeur.widget.attrs.update({'class' : 'inputs'})

	renvoi = forms.BooleanField(help_text="Cochez si vous souhaitez obtenir une copie du mail envoyé.", required=False)