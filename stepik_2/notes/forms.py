from .models import Note
from django.forms import ModelForm, TextInput


class NoteForm(ModelForm):

    class Meta:
        # Название модели на основе
        # которой создается форма
        model = Note
        # Включаем все поля с модели в форму
        fields = ['note_text',]
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Заметка',
                }),

        }
