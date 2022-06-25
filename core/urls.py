from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"wallets", views.WalletListView, basename="wallets")
router.register(r"transactions", views.TransactionsView, basename="transactions")

urlpatterns = [
] + router.urls
