
from django.urls import path
from .views import SignupPageView, logout_view


urlpatterns = [
    path('reg/', SignupPageView.as_view(), name='reg'),
    path('logout/', logout_view, name='logout'),
]
