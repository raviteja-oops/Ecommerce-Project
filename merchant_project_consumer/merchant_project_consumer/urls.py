"""merchant_project_consumer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.views.generic import TemplateView

from merchant_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.showMerchantIndex,name='main'),
    path('login_check/',views.loginCheck,name='login_check'),
    path('change_password/',views.changePassword,name="change_password"),
    path('password_check/',views.passwordCheck,name='password_check'),
    path('logout/',views.logOut,name='logout'),

    path('homepage/',views.showHomepage,name='homepage'),
    path('add_product/',views.addProduct,name='add_product'),
    path('save_product/',views.saveProduct,name="save_product"),
    path('view_products/',views.viewProducts,name='view_products'),
    path('update_product/',views.updateProduct,name='update_product'),
    path('save_update_product/',views.saveUpdateProduct,name='save_update_product'),
    path('delete_one_product/',views.deleteProduct,name='delete_one_product')

]
