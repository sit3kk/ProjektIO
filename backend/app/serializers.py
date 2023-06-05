from rest_framework.serializers import (
    ModelSerializer,
    PrimaryKeyRelatedField,
    SerializerMethodField,
)

from .models import Order, OrderItem, Product, Review, ShippingAddress


class ReviewSerializer(ModelSerializer):
    product = PrimaryKeyRelatedField(queryset=Product.objects, many=False)

    class Meta:
        model = Review
        fields = "__all__"

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret["_id"] = str(ret["_id"])
        ret["product"] = str(ret["product"])
        ret["user"] = str(ret["user"])
        return ret


class ProductSerializer(ModelSerializer):
    reviews = SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = "__all__"

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret["_id"] = str(ret["_id"])
        ret["user"] = str(ret["user"])
        return ret

    def get_reviews(self, obj):
        reviews = obj.review_set.all()
        serializer = ReviewSerializer(reviews, many=True)
        return serializer.data


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret["user"] = str(ret["user"])
        ret["_id"] = str(ret["_id"])
        return ret


class OrderItemSerializer(ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret["_id"] = str(ret["_id"])
        ret["product"] = str(ret["product"])
        ret["order"] = str(ret["order"])
        return ret


class ShippingAddressSerializer(ModelSerializer):
    order = OrderSerializer(read_only=True)

    class Meta:
        model = ShippingAddress
        fields = "__all__"

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret["_id"] = str(ret["_id"])
        return ret
