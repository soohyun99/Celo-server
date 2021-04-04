from rest_framework import serializers
from server.models import *
from drf_writable_nested.serializers import WritableNestedModelSerializer
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ('id', 'name', 'location', 'desc', 'mainpic', 'pic1', 'pic2', 'pic3', 'clap')
        extra_kwargs = {'id': {'validators': []}}


class LoginSerializer(WritableNestedModelSerializer):
    store = StoreSerializer(many=True, required=False)
    class Meta:
        model = Login
        fields = ('id', 'pw', 'email', 'nickname', 'store')
        extra_kwargs = {'id': {'validators': []}}
