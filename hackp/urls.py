"""hackp URL Configuration

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
from django.urls import path, include
import hackapp.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hackapp.views.start, name="start"),
    path('accounts/', include('allauth.urls')),
    path('create/', hackapp.views.create, name="create"),
    path('new/', hackapp.views.new, name="new"),
    path('post/<int:pk>/', hackapp.views.detail, name='detail'),
    path('<int:pk>/challenge/', hackapp.views.challenge, name="challenge"),
    path('<int:pk>/delete_challenge/', hackapp.views.delete_challenge, name="delete_challenge"),
    path('<int:pk>/like_toggle/', hackapp.views.like_toggle, name="like_toggle"),
    path('<int:pk>/like_challenge/', hackapp.views.like_challenge, name="like_challenge"),
    path('home/', hackapp.views.home, name="home"),
    
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
