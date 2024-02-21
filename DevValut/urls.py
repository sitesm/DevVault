"""
URL configuration for DevValut project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from home_page import views as home_views # always need to import the views
from SCDL import views as scdl_views # always need to import the views


urlpatterns = [
    path("", home_views.home, name="home"), # home_page
    path("SCDL/", scdl_views.main, name="SCDL"), # Main SCDL page
    path("SCDL/download", scdl_views.download, name="SCDL_download"), # SCDL downlaod page (redirs back to main SCDL)
    path("admin/", admin.site.urls),
]
