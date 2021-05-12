from django.urls import path
from . import views

urlpatterns=[
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('home/<username>', views.home_view, name='home'),
    path('add_item', views.additem_view, name='add_item'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
]

# 