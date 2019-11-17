"""admin_project_provider URL Configuration

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

from admin_app import views
from merchant_app import views as merchant_views
from consumer_app import views as consumer_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="admin/admin_login.html"),name="logout"),
    path('admincheck/',views.showHomepage,name='admincheck'),
    path('homepage/',TemplateView.as_view(template_name="admin/homepage.html"),name='homepage'),
    path('register_merchant/',views.merchantRegistration,name="add_merchant"),
    path('save_merchant/',views.saveMerchant,name='save_merchant'),
    path('view_merchant/',views.ViewAllMerchants.as_view(),name='view_merchant'),
    path('delete_merchant/',views.deleteMerchant,name='delete_merchant'),

    #Requests from merchant
    path('check_details/<str:email>&<str:password>/',merchant_views.CheckMerchantLoginDetails.as_view(),name='check_details'),
    path('change_merchant_password/<str:email>&<str:password>/',merchant_views.ChangeMerchantPassword.as_view(),name='change_merchant_password'),
    path('save_product/',merchant_views.ProductDetails.as_view(),name='save_product'),
    path('view_all_products/<int:merchant_id>/',merchant_views.ProductDetails.as_view(),name='view_all_products'),
    path('getone/<int:product_id>/',merchant_views.ModifyProductDetails.as_view(),name='getone'),
    path('updateone/<int:p_no>/',merchant_views.ModifyProductDetails.as_view(),name="updateone"),
    path('delete_product/<int:p_no>/',merchant_views.ModifyProductDetails.as_view(),name="delete_product"),

    #Request from consumer
    path('get_last_consumer_id/',consumer_views.GetLastConsumerId.as_view(),name='view_consumers')
]
