from rest_framework import serializers, fields
from .models import Student
from datetime import date

class StudentSerializer(serializers.ModelSerializer):
    document = fields.DateTimeField(input_formats=None, default_timezone=None)

    def validate_document(self, dob):
        today = date.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        if (not(16 < age < 50)):
            raise serializers.ValidationError("You are no eligible for filling the form")
        return dob

    class Meta:
        model = Student
        fields = ('pk', 'name', 'email', 'document', 'phone', 'registrationDate')
