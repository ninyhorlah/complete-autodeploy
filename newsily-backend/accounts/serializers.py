from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from rest_framework.validators import UniqueValidator
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.models import update_last_login

User = get_user_model()


JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', )


class UserRegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'username')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class UserLoginSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(required=True, write_only=True)
    password = serializers.CharField(required=True, write_only=True)
    token = serializers.CharField(read_only=True, allow_blank=False)

    class Meta:
        model = User
        fields = ('email', 'password', 'token')

    
    def validate(self, attrs):
        email = attrs.get('email', None)
        password = attrs.get('password', None)

        if not email or not password:
            raise serializers.ValidationError("Please enter email address or password")
            
        user = authenticate(email=email, password=password)

        if not user:
            raise serializers.ValidationError("Wrong Credentials")
        
        if not user.is_active:
            raise serializers.ValidationError("User is not active, Please contact administrator")
            
        try:
            payload = JWT_PAYLOAD_HANDLER(user)
            jwt_token = JWT_ENCODE_HANDLER(payload)
            update_last_login(None, user)
        except User.DoesNotExist:
            raise serializers.ValidationError('User with given email and password does not exists')
        
        data = {
            'username' : user.username,
            'token' : jwt_token
        }

        return data
