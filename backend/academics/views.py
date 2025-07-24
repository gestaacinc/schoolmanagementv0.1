from rest_framework import generics
from .models import AcademicYear, AcademicOffering
from .serializers import AcademicYearSerializer, AcademicOfferingSerializer

class AcademicYearListCreateAPIView(generics.ListCreateAPIView):
    queryset = AcademicYear.objects.all()
    serializer_class = AcademicYearSerializer

class AcademicOfferingListCreateAPIView(generics.ListCreateAPIView):
    queryset = AcademicOffering.objects.all()
    serializer_class = AcademicOfferingSerializer