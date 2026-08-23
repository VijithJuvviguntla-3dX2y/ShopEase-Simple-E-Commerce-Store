from django.contrib.auth.models import User  # type: ignore
from rest_framework import serializers  # type: ignore

from .models import Order, OrderItem, Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product

        fields = [  # noqa: RUF012
            "id",
            "name",
            "description",
            "price",
            "category",
            "image",
            "stock",
            "created_at",
        ]

class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True,
        min_length=6
    )

    class Meta:
        model = User

        fields = [  # noqa: RUF012
            "username",
            "email",
            "password",
        ]

    def create(self, validated_data):

        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )

        return user


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User

        fields = [  # noqa: RUF012
            "id",
            "username",
            "email",
        ]


class OrderItemSerializer(serializers.ModelSerializer):

    product_name = serializers.CharField(
        source="product.name",
        read_only=True
    )

    class Meta:
        model = OrderItem

        fields = [  # noqa: RUF012
            "id",
            "product",
            "product_name",
            "quantity",
            "price",
        ]


class OrderSerializer(serializers.ModelSerializer):

    items = OrderItemSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Order

        fields = ["id",  # noqa: RUF012
            "user",
            "items",
            "total_amount",
            "status",
            "name",
            "email",
            "phone",
            "address",
            "city",
            "state",
            "pincode",
            "created_at",
        ]

        read_only_fields = [  # noqa: RUF012
            "user",
            "total_amount",
            "status",
        ]