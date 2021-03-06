"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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

from blog import views as blog_views

urlpatterns = [
    url(r'^$', blog_views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^blog/article/(.*)', blog_views.view_article),
    url(r'starsIns/', blog_views.starsIns),
    url(r'^instagram/(.*)/', blog_views.instagram),
    url(r'^timetable/([0-9]{7})/([0-9]{2})/([0-9]{2})/', blog_views.timetable),
    url(r'studentID/', blog_views.studentID),
    url(r'^timetableTemp/(.*)/', blog_views.timetableTemp),
    url(r'wait/', blog_views.wait),
]



