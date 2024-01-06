from django.contrib import admin
from django.urls import path
from blog_app import views

app_name = 'blog'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.post_list, name='post_list'),
    path('<int:id>/', views.post_detail, name='post_detail')
]
