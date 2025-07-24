from django.db import models

class AcademicYear(models.Model):
    year = models.CharField(max_length=9, unique=True, help_text="e.g., 2025-2026")
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.year

class AcademicOffering(models.Model):
    class OfferingTypes(models.TextChoices):
        BASIC_ED = 'BASIC_ED', 'Basic Education'
        COLLEGE = 'COLLEGE', 'College / Tertiary'
        TVET = 'TVET', 'Technical-Vocational'

    name = models.CharField(max_length=200)
    offering_type = models.CharField(max_length=10, choices=OfferingTypes.choices)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name