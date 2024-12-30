"""
URL configuration for Vacationjob project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from nass import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('login/',views.login1,name='login1'),
    path('register/',views.register_view,name='register_view'),
    path('admin_dash/', views.admin_dashboard, name='admin_dashboard'),
    path('user/', views.user_dashboard, name='user_dashboard'),
    path('verify/', views.verify_dashboard, name='verify_dashboard'),
    path('userprofile/',views.profile_view, name='profile_view'),
    path('logout/',views.Logout, name='Logout'),
    path('AC/',views.Account, name='Account'),
    path('bankDetail/',views.Bank_Details, name='BankDetails'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('Jobs/', views.JobList, name='JobList'),
    path('submit-task/<int:task_id>/', views.submit_task, name='submit_task'),
    path('track-task/<int:task_id>/', views.track_and_redirect, name='track_task'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
