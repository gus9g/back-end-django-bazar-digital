from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('digitalbazar.urls'), name='digitalbazar'),
    path('user/', include('user.urls'), name='user')
]
