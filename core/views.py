from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny
from .models import Wallet,Transaction
from .serializers import WalletSerializer,TransactionSerializer

# Create your views here.
class WalletListView(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = [AllowAny]
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer


class TransactionsView(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

   