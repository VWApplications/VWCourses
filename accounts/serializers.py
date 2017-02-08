from rest_framework import serializers
from .models import User, Phone, Address

class PhoneSerializer(serializers.ModelSerializer):
  class Meta:
    model = Phone
    fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
  class Meta:
    model = Address
    fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
  phone = PhoneSerializer()
  address = AddressSerializer()

  class Meta:
    model = User
    fields = ('username', 'name', 'email', 'phone', 'address', 'is_staff', 'date_joined')
