from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Web_final_Django_Project.web.urls')),
    path('auth/', include('Web_final_Django_Project.app_auth.urls'))
]
