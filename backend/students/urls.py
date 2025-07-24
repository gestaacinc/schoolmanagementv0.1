from django.urls import path
from .views import StudentListCreateAPIView

urlpatterns = [
    path('students/', StudentListCreateAPIView.as_view(), name='student-list-create'),
]