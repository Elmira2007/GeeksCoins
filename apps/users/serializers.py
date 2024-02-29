from rest_framework import serializers
from apps.users.models import User

class UserUsernameSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ('id', 'username')
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'phone', 'age', 'direction', 'balance', 'wallet_adress')
        
class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length = 255,
        write_only = True
    )
    password2 = serializers.CharField(
        max_length = 255,
        write_only = True
    )
    
    class Meta:
        model = User
        fields = ('username', 'phone', 'age', 'direction', 'password', 'password2')
        
    def validate(self, attrs):
        if attrs['password'] != attrs ['password2']:
            raise serializers.ValidationError({'password2': "Пароли отличаются"})
        elif '+996' not in attrs['phone']:
            raise serializers.ValidationError({'phone': "Введеный номер не соответствует стандартам Кыргызтана (+996)"})
        elif len(attrs['password']) < 8 and len(attrs['password2']) < 8:
            raise serializers.ValidationError({'password_len': "Длина пароля меньше восьми символов!"})
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            phone = validated_data['phone'],
            age = validated_data['age'],
            direction = validated_data['direction'],
            password = validated_data['password']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    
class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'phone', 'age', 'direction', 'password', 'password2', 'balance')
        
        
class CoinInfoSerializer(serializers.Serializer):
    username = serializers.CharField(
        source = 'user.username'
    )
    balance = serializers.ImageField()
                
class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'confirm_password', 'phone', 'date_joined')
        