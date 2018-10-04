from django import forms
from .models import Message
from django.utils.translation import ugettext_lazy as _


class MessageForm(forms.ModelForm):
    name = forms.CharField(label='Имя')
    surname = forms.CharField(label='Фамилия')

    class Meta:
        model = Message
        fields = ('name', 'surname', 'email', 'subject', 'message')
        widgets = {
            'message': forms.Textarea(
                attrs={'rows': 4, 'placeholder': 'Введите сообщение', 'data-error': 'Текст сообщения важен для нас...'})
        }
        labels = {
            'name': _('Имя'),
            'surname': _('Фамилия'),
            'email': _('Email'),
            'subject': _('Тема'),
            'message': _('Сообщение'),
        }

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if self.fields[field_name].required:
                self.fields[field_name].label += " *"
