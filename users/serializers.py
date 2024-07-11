from rest_framework.exceptions import ValidationError
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from users.models import User, Payments


class UserSerializer(ModelSerializer):
    payments = SerializerMethodField()

    def get_payments(self, obj):
        return [
            f"{p.date_of_payment}-({p.payment_amount}, наличные: {p.payment_method_is_cash}),"
            for p in Payments.objects.filter(user=obj).order_by("date_of_payment")
        ]

        # return [
        #     f"{p.date_of_payment}-({p.course if p.course else p.lesson}, {p.payment_amount}, наличные: {p.payment_method_is_cash} )"
        #     for p in Payments.objects.filter(user=obj).order_by('date_of_payment')
        # ]

    """date_of_payment = models.DateTimeField(auto_now_add=False, **NULLABLE, verbose_name="Дата оплаты",
                                           help_text="Укажите дату оплаты")

    course = models.ForeignKey(Course, on_delete=models.CASCADE, **NULLABLE, related_name='course')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, **NULLABLE, related_name='lesson')

    payment_amount = models.IntegerField(verbose_name='введите сумму оплаты')

    payment_method_is_cash = models.BooleanField(verbose_name='способ оплаты - наличные', help_text='Укажите признак оплаты наличными')"""

    class Meta:
        model = User
        fields = "__all__"


class PaymentsSerializer(ModelSerializer):
    class Meta:
        model = Payments
        fields = "__all__"

    def create(self, validated_data):
        if validated_data.get("course") and validated_data.get("lesson"):
            raise ValidationError(
                "You can choose 'course' or 'lesson', but not both at the same time"
            )
        elif (
            validated_data.get("course") is None
            and validated_data.get("lesson") is None
        ):
            raise ValidationError("You must choose 'course' or 'lesson'")

        payment_item = Payments.objects.create(**validated_data)
        return payment_item

    def update(self, instance, validated_data):
        if validated_data.get("course") and validated_data.get("lesson"):
            raise ValidationError(
                "You can choose 'course' or 'lesson', but not both at the same time"
            )
        elif (
            validated_data.get("course") is None
            and validated_data.get("lesson") is None
        ):
            raise ValidationError("You must choose 'course' or 'lesson'")

        payment_item = Payments.objects.create(**validated_data)
        return payment_item
