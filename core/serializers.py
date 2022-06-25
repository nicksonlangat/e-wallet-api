from rest_framework import serializers
from .models import Wallet,Transaction
from accounts.serializers import UserSerializer

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = [
            'id',
            'user',
            'account_number',
            'wallet_balance',
            'date_created'
        ]

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["user"] = UserSerializer(instance.user).data
        return rep


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = [
            'id','sender','recipient',
            'transaction_type','amount',
            'transaction_code','transaction_date','is_successful'
        ]
    def create(self, validated_data):
        type = validated_data['transaction_type']
        sender = validated_data['sender']
        recipient = validated_data['recipient']
        amount = validated_data['amount']
        sender_wallet = Wallet.objects.get(user=sender)
        if type == 'Deposit':
            if amount <= 0:
                raise serializers.ValidationError(f'You cannot deposit {amount} as it is below the minimum. Please try a bigger amount.')
            sender_wallet.wallet_balance += amount
            sender_wallet.save(update_fields=["wallet_balance"])
        elif type == 'Withdrawal':
            recipient_wallet = Wallet.objects.get(user=recipient)
            if amount > sender_wallet.wallet_balance:
                raise serializers.ValidationError(f'Your balance of {sender_wallet.wallet_balance} is insufficient to send {amount}. \
                    Please top up or try a smaller amount.')
            elif amount <= 0:
                raise serializers.ValidationError(f'You cannot send {amount} as it is below the minimum. \
                        Please try a bigger amount.')
            else:
                sender_wallet.wallet_balance -= amount
                sender_wallet.save(update_fields=["wallet_balance"])
                recipient_wallet.wallet_balance += amount
                recipient_wallet.save(update_fields=["wallet_balance"])
        return Transaction.objects.create(**validated_data)

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["sender"] = UserSerializer(instance.sender).data
        rep["recipient"] = UserSerializer(instance.sender).data
        return rep

