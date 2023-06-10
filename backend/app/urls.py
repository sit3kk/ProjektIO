from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    APIRootView,
    OrderItemViewSet,
    OrderViewSet,
    ProductViewSet,
    ReviewViewSet,
)


# Create your urls here.
class Router(DefaultRouter):
    APIRootView = APIRootView


router = Router()
router.register(r"products", ProductViewSet, basename="product")
router.register(r"reviews", ReviewViewSet, basename="review")
router.register(r"orders", OrderViewSet, basename="order")
router.register(r"order-items", OrderItemViewSet, basename="order-item")


urlpatterns = [path("", include(router.urls))]
