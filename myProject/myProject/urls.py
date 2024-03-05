from django.contrib import admin
from django.urls import path , include
from myApp.views import *
from django.conf import settings
from django.conf.urls.static import static
import notifications.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', singupPage,name="singupPage"),
    path('singinPage/', singinPage,name="singinPage"),
    path('homePage/', homePage, name="homePage"),
    path('logoutPage/', logoutPage, name="logoutPage"),
    path('blogPage/', blogPage, name="blogPage"),
    path('viewblog/', viewblog, name="viewblog"),
    path('viewblogDeletePage/<str:id>', viewblogDeletePage, name="viewblogDeletePage"),
    path('editBlog/<str:id>', editBlog, name="editBlog"),
    path('search_results/', search_results, name="search_results"),
    path('profilePage/', profilePage, name="profilePage"),
    path('updateProfile/', updateProfile, name="updateProfile"),
    path('notificationPage/', notificationPage, name="notificationPage"),
    path('notifications/', include(notifications.urls, namespace='notifications')),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
