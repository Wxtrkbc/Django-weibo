"""weibo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin

from UI.Controllers import accountView
from UI.Controllers import textViews
from UI.Controllers import weiboView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^test/', textViews.test),
<<<<<<< HEAD
    url(r'^login/', accountView.login),
    url(r'^userProfile/', accountView.userProfile),
    url(r'^index/', accountView.index),

    url(r'^publish_weibo/', weiboView.publish_wb),
    url(r'^get_weibo/(?P<user_queue_id>\d+)/$', weiboView.get_user_weibos),
=======
    url(r'^personalpage/', textViews.personal),
    url(r'^register/', textViews.register),
>>>>>>> 430f195f7c8db5a116d3955bc16b4dde03034ac8
]

