from django.urls import path
from module1.views import *
urlpatterns=[
    path('',home,name='home'),
    path('about',about,name='about'),
    path('contact',contact,name='contact'),
    path('login',login,name='login'),
    path('profile',profile,name='profile'),
    path('alumini',alumini,name='alumnipage'),
    path('register',register,name='register'),
    path('staff',staff,name='staff'),
    path('moreview',moreview,name='more'),
    path('delete/<int:rid>',delete,name='delete'),
    path('logout',logoutv,name='logout'),
    path('update/<int:rid>',update,name='update'),
]