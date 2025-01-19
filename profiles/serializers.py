"""
This module defines the ProfileSerializer class that is used to serialize the Profile model.
"""
from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    """
    This class defines how the Profile model should be serialized.
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """
        This class defines the fields that should be serialized.
        """
        model = Profile
        fields = [
            'id',
            'owner',
            'created_at',
            'updated_at',
            'name',
            'content',
            'image'
        ]
