from django.urls import path

from .views import frontpage, signuppage

app_name = 'core'

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('signup/', signuppage, name='signup')
]