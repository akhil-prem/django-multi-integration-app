from rest_framework import serializers
from .models import Account
from rest_framework_simplejwt.tokens import RefreshToken


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'first_name', 'email']


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        try:
            account = Account.objects.get(email=email)
        except Account.DoesNotExist:
            raise serializers.ValidationError("Account not found.")

        if not account.check_password(password):
            raise serializers.ValidationError("Incorrect password.")

        return data

    def get_token(self, account):
        refresh = RefreshToken.for_user(account)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
