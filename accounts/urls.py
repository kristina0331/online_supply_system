from django.urls import path
from . import views


urlpatterns = [
   path('',views.home),
   path('requester/<str:pk_test>/',views.requester),
   path('products/',views.products),
   path('status/',views.status),

]