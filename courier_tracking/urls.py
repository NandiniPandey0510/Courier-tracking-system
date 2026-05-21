"""courier_tracking URL Configuration

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
from courier.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('login',login,name='login'),
    path('logout',logout,name='logout'),
    path('admin_home',admin_home,name='admin_home'),
    path('signup',signup,name='signup'),
    path('view_users',view_users,name='view_users'),
    path('delete_user\<int:pid>', delete_user, name="delete_user"),
    path('change_passwordadmin',change_passwordadmin,name="change_passwordadmin"),
    path('change_passworduser',change_passworduser,name="change_passworduser"),
    path('user_home', user_home, name="user_home"),
    path('feedback',feedback,name="feedback"),
    path('view_feedback',view_feedback,name="view_feedback"),
    path('delete_feedback/<int:id>',delete_feedback,name="delete_feedback"),
    path('send_parcel',send_parcel,name="send_parcel"),
    path('view_my_parcel',view_my_parcel,name="view_my_parcel"),
    path('view_parcel_admin',view_parcel_admin,name="view_parcel_admin"),
    path('change_status<int:id>',change_status,name="change_status"),
    path('sender_detail<int:id>',sender_detail,name="sender_detail"),
    path('delete_parcel<int:id>',delete_parcel,name="delete_parcel"),
    path('check_status_user<int:pid>',check_status_user,name="check_status_user"),
    path('change_track_status<int:pid>',change_track_status,name="change_track_status"),
    path('visitor_track',visitor_track,name="visitor_track"),
    path('parsel_location',parsel_location,name="parsel_location"),
    path('pay_now/<int:id>',pay_now,name="pay_now"),
    path('invoice/<int:id>',invoice,name="invoice"),
    path('download/<int:id>',download,name="download"),
    path('edit_profile',edit_profile,name='edit_profile'),
    path('about',about,name='about')

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
