from rest_framework import serializers

from ..models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = (
            'id', 'username', 'first_name', 'last_name', 'email',
            'date_joined', 'last_login'
        )
        read_only_fields = (
            'id', 'username', 'date_joined', 'last_login',
        )


class PublicScopeAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = (
            'id', 'username', 'first_name', 'last_name', 'email'
        )
        read_only_fields = fields
