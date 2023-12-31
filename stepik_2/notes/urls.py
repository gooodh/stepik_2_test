

from django.urls import path
from .views import HomePageView, createpost, NoteListView


urlpatterns = [
    path('home', HomePageView.as_view(), name='home'),
    path('home/', HomePageView.as_view(), name='home'),
    path('notes', NoteListView.as_view(), name='notes'),
    path('notes/', NoteListView.as_view(), name='notes'),
    path('add_note', createpost, name='add_note'),
    path('add_note/', createpost, name='add_note'),
]
