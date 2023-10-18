

from django.urls import path
from .views import HomePageView, NoteCreate, NoteListView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('notes_list/', NoteListView.as_view(), name='notes_list'),
    # path('notes_list/', note_list_view, name='note_list_view'),
    path('create/', NoteCreate.as_view(), name='create'),
]
