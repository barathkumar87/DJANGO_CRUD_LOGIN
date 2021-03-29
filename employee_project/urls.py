from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('',include('authentication.urls')),
    path('admin/', admin.site.urls),
    path('employee/', include('employee_register.urls')),
    
    
]
