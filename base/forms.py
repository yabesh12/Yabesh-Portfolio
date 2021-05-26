from django import forms
from django.forms import ModelForm



from .models import Post, Signup

class PostForm(ModelForm):
 	
 	class Meta:
 		model = Post
 		fields = '__all__'

 		widgets = {

 			'tags': forms.CheckboxSelectMultiple(),
 		}	 


class SignupForm(forms.ModelForm):

	class Meta:
		model = Signup
		fields = [
				'username',
				'password',
			]
