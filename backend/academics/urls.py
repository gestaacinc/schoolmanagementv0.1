from django.urls import path
from .views import AcademicYearListCreateAPIView, AcademicOfferingListCreateAPIView

urlpatterns = [
    path('years/', AcademicYearListCreateAPIView.as_view(), name='academicyear-list-create'),
    path('offerings/', AcademicOfferingListCreateAPIView.as_view(), name='academicoffering-list-create'),
]