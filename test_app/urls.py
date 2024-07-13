from django.contrib import admin
from django.urls import path 
from . import views
app_name='test_app'

urlpatterns = [
    path('',views.home,name='test'),
    path('api/',views.ApiHome.as_view(),name='api')
]
