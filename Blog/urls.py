from django.contrib import admin
from django.urls import path, include
from blog_app import views

app_name = 'blog'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog_app.urls', namespace='blog_app'))

]