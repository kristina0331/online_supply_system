from django.urls import path
from . import views


urlpatterns = [
   path('',views.homepage),
   path('requester/',views.requester),
   path('products/',views.products),
   path('status/',views.status),
   path('register/',views.register),
   path('login/',views.login, name='login'),

]