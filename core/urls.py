from django.urls import path

from .views import frontpage, signuppage, loginpage, logout_user

app_name = 'core'

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('signup/', signuppage, name='signup'),
    path('login/', loginpage, name='login'),
    path('logout/', logout_user, name='logout'),
]