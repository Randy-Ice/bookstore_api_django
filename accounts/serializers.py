from djoser.serializers import UserCreatePasswordRetypeSerializer

class UserRegistrationRetypePasswordSerializer(UserCreatePasswordRetypeSerializer):
    class Meta(UserCreatePasswordRetypeSerializer.Meta):
        fields = [
            'first_name', 'last_name','username', 'email', 'password'
        ]