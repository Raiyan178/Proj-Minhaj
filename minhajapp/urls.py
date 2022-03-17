
from unicodedata import name
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('package/',views.package,name='package'),
    path('signin/',views.signin,name='signin'),
    path('signup/',views.signup,name='signup'),
    path('profile/',views.profile,name='porfile'),
    path('logout/',views.signout,name='signout'),
    path('profilemap/',views.profilemap,name='profilemap'),
    path('packages/<str:slug>',views.pak,name='packages'),
    path('order/<str:slug>',views.order,name='order'),
    path('search/',views.search,name='search')
]
