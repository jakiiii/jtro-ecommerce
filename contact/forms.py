from django import forms

from .models import UserMessage


class UserMessageCreationForm(forms.ModelForm):

    class Meta:
        model = UserMessage
        fields = [
            'full_name',
            'email',
            'message',
        ]
        labels = {
            'full_name': 'Name',
            'email': 'Email',
            'message': 'Message',
        }
