from rest_framework import serializers, generics
from django.contrib.auth.models import User
from .models import task

class TaskSerializer(serializers.ModelSerializer):
    '''Serializer for a task'''
    class Meta:
        model = task
        fields = ['id', 'title', 'description', 'completed', 'created_at', 'user']
        read_only_fields = ['user']

class RegisterSerializer(serializers.ModelSerializer):
    '''Serializer for a register'''
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password':{ 'write_only':True }}

    def create(self, validated_data):
        '''Create and return a new `User` instance, given the validated data.'''
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
        )
        return user