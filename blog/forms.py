from django import forms

class ContactForm(forms.Form):

	subject = forms.CharField(max_length=100,required=True)
	subject.widget.attrs.update({'class' : 'first'})

	message = forms.CharField(widget=forms.Textarea,required=True)

	envoyeur = forms.EmailField(label="E-mail",required=True)

	copy = forms.BooleanField(help_text="Check if you want to have a copy of the message", required=False)
	copy.widget.attrs.update({'class' : 'checkbutton'})

class CommentForm(forms.Form):
		article = forms.CharField( widget = forms.HiddenInput, max_length=10, required=True)
		article.widget.attrs.update({'class' : 'post_com', 'id':'post_com'})

		author = forms.CharField(max_length=40,required=True)
		author.widget.attrs.update({'class' : 'first'})

		comment = forms.CharField(widget = forms.Textarea, required=True)

	
