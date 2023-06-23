from django.urls import path
from . import views
from .views import PostView


app_name='app1'

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
# Dynamic url
    path('icd/<slug:slugID>', views.iceCreamDetails, name='Ice_cream_details'),
    path('cartProduct/', views.cartProduct, name='cartProduct'),
    
# API url to GET data using function based View
    path('api/get/', views.get_all_IceCreams, name='get_api'),
# API url to POST data using Class based View
    path('api/post/', PostView.as_view(), name='post_api'),
    
]

