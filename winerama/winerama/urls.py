"""winerama URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [

    # 一级boss最大，二级boss次之，以此类推

    # url 等价于 业务。因为用户的真实目的和需求，都是通过url，来与网站互作的。有什么url，就意味着网站能提供的业务。
    # 这里是 一级boss 统领总账（把全部url收集起来），仅仅是对二级boss手下的业务进行清点。

    # 跟 reviews 相关的 二级boss 之一： 所有与reviews相关的url都交由 reviews 这个 子app （二级boss）来统领
    # 具体看 它的脑子：reviews/urls.py 和 手脚：reviews/views.py
    url(r'^reviews/', include('reviews.urls', namespace="reviews")),

    # 跟 admin 相关的 二级boss 之一：
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls', namespace="auth")),

]
