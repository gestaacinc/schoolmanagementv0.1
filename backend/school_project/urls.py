from django.contrib import admin
from django.urls import path, include # <-- Add 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('students.urls')),
    path('api/', include('faculty.urls')),    
    path('api/', include('academics.urls')),  
]