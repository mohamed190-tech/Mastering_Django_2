from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from my_site import settings
from . import views
from django.http import HttpResponse

app_name = "blog"




urlpatterns = [
    #path('', views.post_list,name='post_lis'),
    path('', views.PostListView.as_view(),name='post_lis'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',views.post_detal,name='post_detal'),
   
]



#if settings.DEBUG:
   # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
    #urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)