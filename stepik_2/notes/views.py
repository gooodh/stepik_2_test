from django.contrib.auth.mixins import (LoginRequiredMixin)
from django.http import Http404
from django.shortcuts import render
# from django.views.generic import CreateView  # new

from .models import Note

from .forms import NoteForm
from django.views.generic import TemplateView, ListView


class HomePageView(TemplateView):
    template_name = 'notes/home.html'


class NoteListView(LoginRequiredMixin, ListView):
    model = Note
    context_object_name = 'note_list'
    template_name = 'notes/note_list.html'
    login_url = 'login'

    def get_queryset(self):
        return Note.objects.filter(owner=self.request.user)


def createpost(request):
    if request.method == 'POST':
        if request.POST.get('note_text'):
            note = Note()
            note.note_text = request.POST.get('note_text')
            note.owner = request.user
            note.save()

            return render(request, 'notes/create.html')  

    else:
        return render(request, 'notes/create.html')

# class NoteCreate(LoginRequiredMixin, CreateView):
#     # Модель куда выполняется сохранение
#     model = Note
#     # Класс на основе которого будет валидация полей
#     form_class = NoteForm
#     # Выведем все существующие записи на странице
#     extra_context = {'notes': Note.objects.all()}
#     # Шаблон с помощью которого
#     # будут выводиться данные
#     template_name = 'notes/create.html'
#     # На какую страницу будет перенаправление
#     # в случае успешного сохранения формы
#     success_url = '/home/'
#     login_url = 'login'  # new
#     permission_required = 'notes.special_status'

#     def snippet_detail(request):
#         model = Note
#         form = NoteForm(request.POST)
#         print('snip')
#         if request.method == 'POST':
#             print('post')
#             if form.is_valid():
#                 print('valid')

#                 model.owner = request.user
#                 model.save()

