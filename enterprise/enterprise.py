from rest_framework import serializers
from enterprise.models import Enterprise


class EnterpriseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enterprise
        fields = ('id', 'name', 'address', 'phone', 'nit')
