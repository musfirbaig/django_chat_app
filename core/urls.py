from django.urls import path

from .views import frontpage

app_name = 'core'

urlpatterns = [
    path('', frontpage, name='frontpage')
]