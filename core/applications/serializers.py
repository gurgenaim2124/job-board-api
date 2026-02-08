from rest_framework import serializers
from .models import Application

class ApplicationSerializer(serializers.ModelSerializer):
    applicant = serializers.ReadOnlyField(source='applicant.username')
    job_title = serializers.ReadOnlyField(source='job.title')

    class Meta:
        model = Application
        fields = (
            'id',
            'job',
            'job_title',
            'applicant',
            'cover_letter',
            'status',
            'created_at',
        )
        read_only_fields = ('status',)

class ApplicationSerializer(serializers.ModelSerializer):
    applicant = serializers.ReadOnlyField(source='applicant.username')

    class Meta:
        model = Application
        fields = (
            'id',
            'job',
            'applicant',
            'cover_letter',
            'status',
            'created_at',
        )
        read_only_fields = ('status',)

    def create(self, validated_data):
        validated_data['applicant'] = self.context['request'].user
        return super().create(validated_data)