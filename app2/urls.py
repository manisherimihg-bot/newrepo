from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('app1.urls')),
    path('profile',include('app1.urls')),
    path('expression',include('app1.urls'))
]
