from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from users.models import User, Payments


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class PaymentsSerializer(ModelSerializer):
    class Meta:
        model = Payments
        fields = "__all__"

    def create(self, validated_data):
        if validated_data.get('course') and validated_data.get('lesson'):
            raise ValidationError("You can choose 'course' or 'lesson', but not both at the same time")
        elif validated_data.get('course') is None and validated_data.get('lesson') is None:
            raise ValidationError("You must choose 'course' or 'lesson'")

        payment_item = Payments.objects.create(**validated_data)
        return payment_item

    def update(self, instance, validated_data):
        if validated_data.get('course') and validated_data.get('lesson'):
            raise ValidationError("You can choose 'course' or 'lesson', but not both at the same time")
        elif validated_data.get('course') is None and validated_data.get('lesson') is None:
            raise ValidationError("You must choose 'course' or 'lesson'")

        payment_item = Payments.objects.create(**validated_data)
        return payment_item
