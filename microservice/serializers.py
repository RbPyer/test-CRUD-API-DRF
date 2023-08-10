from rest_framework import serializers

from microservice.models import Microservice


class MicroserviceSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Microservice
        fields = "__all__"
