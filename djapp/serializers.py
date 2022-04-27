from dataclasses import fields
from pyexpat import model
import re
from rest_framework import serializers
from .models import Student,Track
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'
    # def to_representation(self,instance):
    #     representation= super().to_representation(instance)
    #     representation['student_track']=instance.student_track.track_name
    #     return representation


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model=Track  
        fields= ('track_name',)