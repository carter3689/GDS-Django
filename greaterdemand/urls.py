"""greaterdemand URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path

#Main views imports
from gdsmain import views

#Documents Views
from documents.views import get_upload,download_handler
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.HomePage.as_view(),name="index"),
    path('upload-documents/',get_upload,name = "document-upload"),
    re_path(r'^download-documents/(?P<pk>\d+)/$',download_handler,name = "document-download")
]
