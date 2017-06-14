"""bratzsoft URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from bratzsoft.core import urls


from bratzsoft.core import views as bratzsoft_views



urlpatterns = [
    url(r'^$', bratzsoft_views.home),
    url(r'^api/', include('bratzsoft.api.urls')),
    url(r'^core/', include('bratzsoft.core.urls')),
    url(r'^sap/', include('bratzsoft.sap.urls')),
    url(r'^admin/', admin.site.urls),




    #Django Rest Framework
    url(r'^api-auth/', include('rest_framework.urls')),
]
