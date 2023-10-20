

from django.urls import path
from .views import SignupPageView, LogoutPageView


urlpatterns = [
    path('reg/', SignupPageView.as_view(), name='reg'),
    path('logout/', LogoutPageView.as_view(), name='logout'),
]
