from django.urls import path
from . import views


urlpatterns = [
   path('',views.home),
   path('about/',views.contact),
   path('purchaserequest/',views.pr),
   path('tracker/',views.tracker),

]