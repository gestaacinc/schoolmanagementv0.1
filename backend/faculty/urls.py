from django.urls import path
from .views import FacultyListCreateAPIView

urlpatterns = [
    path('faculty/', FacultyListCreateAPIView.as_view(), name='faculty-list-create'),
]