from accounts.serializers import UserSerializer

def my_jwt_response_handler(token, user=None, request=None):
    
    user = UserSerializer(user, context={'request' : request}).data

    data = {
        'token' : token,
        'user' : user['username']
    }
    return data

def my_jwt_get_username_from_payload_handler(payload):

    return payload.get('email')