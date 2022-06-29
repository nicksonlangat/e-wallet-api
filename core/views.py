from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Wallet,Transaction
from .serializers import WalletSerializer,TransactionSerializer
from django.db.models import Q

# Create your views here.
class WalletListView(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = [AllowAny]
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['user__id']
    filterset_fields = ['user__id']


class TransactionsView(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['sender__id', 'recipient__id']
    filterset_fields = ['sender__id', 'recipient__id']

    def get_queryset(self):
        try:
            user = self.request.query_params['user']
            qs = self.queryset.filter(Q(sender=user) | Q(recipient=user))
        except Exception as e:
            qs = self.queryset
        return qs


   