from django.urls import path
from . import views


urlpatterns = [
   path('',views.home),
   path('requester/',views.requester),
   path('products/',views.products),
   path('status/',views.status),

]