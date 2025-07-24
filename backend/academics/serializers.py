from rest_framework import serializers
from .models import AcademicYear, AcademicOffering

class AcademicYearSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicYear
        fields = ['id', 'year', 'start_date', 'end_date']

class AcademicOfferingSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicOffering
        fields = ['id', 'name', 'offering_type', 'description']