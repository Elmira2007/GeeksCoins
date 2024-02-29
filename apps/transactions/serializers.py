from rest_framework import serializers
from apps.transactions.models import Transactions
from apps.users import models as user_models

from rest_framework import serializers
from .models import Transactions

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = ['from_user', 'to_user', 'amount', 'created_at', 'is_completed']

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        # Замените идентификаторы «from_user» и «to_user» на имя пользователя.
        from_user_id = representation.get('from_user')
        to_user_id = representation.get('to_user')

        if from_user_id:
            from_user = user_models.User.objects.get(id=from_user_id)
            representation['from_user'] = from_user.username

        if to_user_id:
            to_user = user_models.User.objects.get(id=to_user_id)
            representation['to_user'] = to_user.username

        return representation
    
    def create(self, validated_data):
        # Извлекаем «from_user» и «to_user» из validated_data
        from_user_data = validated_data.pop('from_user', None)
        to_user_data = validated_data.pop('to_user', None)

        # Создайте экземпляр Transactions без полей from_user и to_user.
        transaction = Transactions.objects.create(**validated_data)

        # Если указаны «from_user» и «to_user», установите их отдельно
        if from_user_data:
            from_user = user_models.User.objects.get(id=from_user_data['id'])
            transaction.from_user = from_user

        if to_user_data:
            to_user = user_models.User.objects.get(id=to_user_data['id'])
            transaction.to_user = to_user

        transaction.save()

        return transaction
        