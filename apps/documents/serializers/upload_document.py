from rest_framework import serializers
from apps.documents.models import Document
from django.core.files.storage import FileSystemStorage
from django.conf import settings

class DocumentUploadSerializer(serializers.ModelSerializer):
    file = serializers.FileField()
    name = serializers.CharField(required=False)
    
    class Meta:
        model = Document
        fields = ['name', 'file', 'uploaded_on']
        
        
    def create(self, validated_data):
        user =  self.context['request'].user
        fs = FileSystemStorage()
        request_file = validated_data['file']
        file = fs.save(request_file.name, request_file)
        file_url = fs.url(file)
        document = Document.objects.create(name=request_file.name, file=file_url, owner=user)
        return document

    
    def destroy(self, validated_data):
        file_path = Document.objects.get(id=validated_data['id'])
        fs = FileSystemStorage()
        fs.delete(file_path)
        return file_path
        