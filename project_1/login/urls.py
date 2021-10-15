from django.urls import path
from django.urls.resolvers import URLPattern
from  . import views
urlpatterns=[
    path('',views.signin,name='signin'),
    path('home',views.log,name='log'),
    path('logout',views.logout,name='logout')
]

