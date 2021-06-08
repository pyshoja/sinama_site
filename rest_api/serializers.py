from rest_framework import serializers
from django.contrib.auth.models import User
from .models import testrest


class testrestserializers (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = testrest
        fields = '__all__'


class userrestserializers (serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "last_login",
            "is_active",
            "is_staff",
            "is_superuser",

        )
