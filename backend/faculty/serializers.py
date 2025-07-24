from rest_framework import serializers
from .models import Faculty

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = ['id', 'first_name', 'last_name', 'email', 'phone_number', 'department']