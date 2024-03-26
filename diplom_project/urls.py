"""
URL configuration for diplom_project project.

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
from django.urls import path, include
from django_rest_passwordreset.views import reset_password_request_token, reset_password_confirm
from rest_framework.routers import DefaultRouter

from diplom_app.views import RegisterAccount, ConfirmAccount, AccountDetails, LoginAccount, CategoryView, ShopView, \
    ProductInfoView, OrderView, BasketView, ContactView

router = DefaultRouter()
router.register('products/', ProductInfoView.as_view(), basename='products')
router.register('user/register', RegisterAccount.as_view(), basename='user-register')
router.register('user/register/confirm', ConfirmAccount.as_view(), basename='user-register-confirm')
router.register('user/details', AccountDetails.as_view(), basename='user-details')
router.register('user/contact', ContactView.as_view(), basename='user-contact')
router.register('user/login', LoginAccount.as_view(), basename='user-login')
router.register('user/password_reset', reset_password_request_token, basename='password-reset')
router.register('user/password_reset/confirm', reset_password_confirm, basename='password-reset-confirm')
router.register('categories/', CategoryView.as_view(), basename='categories')
router.register('shops/', ShopView.as_view(), basename='shops')
router.register('basket/', BasketView.as_view(), basename='basket')
router.register('order/', OrderView.as_view(), basename='order')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include(router.urls)),
    path('user/register', include(router.urls)),
    path('user/register/confirm', include(router.urls)),
    path('user/details', include(router.urls)),
    path('user/contact', include(router.urls)),
    path('user/login', include(router.urls)),
    path('user/password_reset', include(router.urls)),
    path('user/password_reset/confirm', include(router.urls)),
    path('categories/', include(router.urls)),
    path('shops/', include(router.urls)),
    path('products/', include(router.urls)),
    path('basket/', include(router.urls)),
    path('order/', include(router.urls)),

]
