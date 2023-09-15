from django.urls import path
from . import views


urlpatterns = [
   path('',views.home),
<<<<<<< HEAD
   path('requester/<str:pk_test>/',views.requester),
=======
   path('requester/',views.requester),
>>>>>>> 482a44bbb6f4fe1d3fa277c70959bb206efebc6b
   path('products/',views.products),
   path('status/',views.status),

]