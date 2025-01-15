from rest_framework import serializers
from .models import Member, FoodPost, FoodRequest, User

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'

class FoodPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodPost
        fields = '__all__'  # Include all fields in the serialized data
        extra_kwargs = {
            'id': {'required': False},  # Make the ID optional
            'quantity': {'required': False},  # Optional quantity field
            'posted_by': {'required': False},  # Optional posted_by field
            'expiration_date': {'required': False},  # Optional expiration_date
            'photo': {'required': False},  # Optional photo field
            'whatsapp_link': {'required': False},  # Optional whatsapp_link field
            'collection_point': {'required': False},  # Optional collection_point field
        }

class FoodRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodRequest
        fields = ['food_post']

    def create(self, validated_data):
        validated_data['requested_by'] = None
        return super().create(validated_data)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['firstname', 'lastname', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True},  # Ensure password is write-only
        }

    def create(self, validated_data):
        # Hash the password before saving the user
        validated_data['password'] = validated_data['password']
        print('created2')
        return super().create(validated_data)
    
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']