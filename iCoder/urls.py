from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('123/',include('home.urls')),
    path('',include('blog.urls')),
]
