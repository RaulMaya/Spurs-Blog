from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude =['post']
        labels = {'user_name':"Name:",
        'user_email':"Email:",
        'text':'Comment:'}
        error_messages = {
            'user_name':{
                'required':'Your name must not be empty.',
                'max_length':'Please enter a shorter name.'
            },
            'user_email':{
                'required':'Your email must not be empty.',
                'max_length':'Please enter a shorter email.'
            },
            'text':{
                'required':'Please enter your comment.',
                'max_length':'You excede the length limit for the comments.'
            }
        }
