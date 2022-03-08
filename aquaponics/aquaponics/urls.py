"""aquaponics URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from django.urls import re_path as url
from django.conf import settings
from django.conf.urls.static import static
import myapp.views

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('index/', myapp.views.index, name="index_url"),
                  path('adminindex/', myapp.views.adminindex, name="adminindex_url"),
                  path('adminaddcategory/', myapp.views.adminaddcat, name="adminaddcat_url"),
                  path('adminviewusers/', myapp.views.adminviewusers, name="adminviewusers_url"),
                  path('adminviewfarmers/', myapp.views.adminviewfarmers, name="adminviewfarmers_url"),
                  url(r'^farmerapprove/(?P<value>\d+)/$', myapp.views.farmerapprove, name='farmerapprove_url'),
                  url(r'^farmerreject/(?P<value>\d+)/$', myapp.views.farmerreject, name='farmerreject_url'),
                  path('adminviewsuppliers/', myapp.views.adminviewsuppliers, name="adminviewsuppliers_url"),
                  url(r'^supplierapprove/(?P<value>\d+)/$', myapp.views.farmerapprove, name='farmerapprove_url'),
                  url(r'^supplierreject/(?P<value>\d+)/$', myapp.views.farmerreject, name='farmerreject_url'),
                  path('adminviewcategory/', myapp.views.adminviewcategory, name="adminviewcategory_url"),
                  url(r'^editcategory/(?P<value>\d+)/$', myapp.views.editcategory, name='editcategory_url'),
                  url(r'^deletecategory/(?P<value>\d+)/$', myapp.views.deletecategory, name='deletecategory_url'),
                  path('adminupdatecategory/', myapp.views.adminupdatecategory, name="adminupdatecategory_url"),
                  path('adminaddguideline/', myapp.views.adminaddguideline, name="adminaddguideline_url"),
                  path('adminviewguideline/', myapp.views.adminviewguideline, name="adminviewguideline_url"),
                  url(r'^editguideline/(?P<value>\d+)/$', myapp.views.editguideline, name='editguideline_url'),
                  url(r'^deleteguideline/(?P<value>\d+)/$', myapp.views.deleteguideline, name='deleteguideline_url'),
                  path('userregistration/', myapp.views.userregistration, name="userregistration_url"),
                  path('farmerregistration/', myapp.views.farmerregistration, name="farmerregistration_url"),
                  path('supplierregistration/', myapp.views.supplierregistration, name="supplierregistration_url"),
                  path('userhome/', myapp.views.userhome, name="userhome_url"),
                  path('login/', myapp.views.login, name="login_url"),
                  path('farmerhome/', myapp.views.farmerhome, name="farmerhome_url"),
                  path('supplierhome/', myapp.views.supplierhome, name="supplierhome_url"),
                  path('sup_addmaterial/', myapp.views.sup_addmaterial, name="sup_addmaterial_url"),
                  path('sup_viewproduct/', myapp.views.sup_viewproduct, name="sup_viewproduct_url"),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += url(r'^$', myapp.views.index),
