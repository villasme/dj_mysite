"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
# from django.contrib import admin
import xadmin
from django.urls import path, include, re_path
from django.views.static import serve
from rest_framework import routers, documentation

from goods import views as good_views
from mysite.settings import MEDIA_ROOT


router = routers.DefaultRouter()
router.register(r'goodsinfo', good_views.GoodInfoView, base_name='goods-info')


urlpatterns = [
    re_path(r'^', include(router.urls)),
    path('polls/', include('polls.urls', namespace='polls')),
    re_path(r'xadmin/', xadmin.site.urls),
    re_path(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    # re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # re_path(r'docs/', documentation.include_docs_urls(title='我的服务API')),
]
