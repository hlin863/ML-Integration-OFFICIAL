from django.urls import path
from django.contrib import admin
from django.urls import re_path
from workflow import views
# import static from django.conf.urls.static
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'), # workflow index
    path('testfolder/', views.testbutton, name='testbutton'), # workflow testbutton
]