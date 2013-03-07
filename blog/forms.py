from django import forms

class ContactForm(forms.Form):
	sujet = forms.CharField(max_length=100,required=True)
	message = forms.CharField(widget=forms.Textarea,required=True)
	envoyeur = forms.EmailField(label="Votre adresse mail",required=True)
	renvoi = forms.BooleanField(help_text="Cochez si vous souhaitez obtenir une copie du mail envoyé.", required=False)