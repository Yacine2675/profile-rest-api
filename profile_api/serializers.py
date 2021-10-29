from rest_framework import serializers

from profile_api import models


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing out APIView"""
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """Seriliazes a user profile object"""  

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password') 
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}

            }
        } 

    def create(self, validate_data):
      """Create and return a new user"""
      user = models.UserProfile.objects.create_user(
          email=validate_data['email'],
          name=validate_data['name'],
          password=validate_data['password'], 
      )

      return user      






