from decimal import Decimal

from django.contrib.auth.models import User  # type: ignore  # noqa: F401
from django.db import transaction  # type: ignore
from rest_framework import status  # type: ignore
from rest_framework.decorators import (  # type: ignore
    api_view,
    permission_classes,
)
from rest_framework.permissions import (  # type: ignore
    AllowAny,
    IsAuthenticated,
)
from rest_framework.response import Response  # type: ignore

from .models import Order, OrderItem, Product
from .serializers import (
    OrderSerializer,
    ProductSerializer,
    RegisterSerializer,
    UserSerializer,
)


@api_view(["GET"])
@permission_classes([AllowAny])
def product_list(request):

    products = Product.objects.all().order_by("-created_at")

    serializer = ProductSerializer(
        products,
        many=True,
        context={"request": request}
    )

    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([AllowAny])
def product_detail(request, product_id):

    try:
        product = Product.objects.get(
            id=product_id
        )

    except Product.DoesNotExist:

        return Response(
            {
                "error": "Product not found."
            },
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = ProductSerializer(
        product,
        context={"request": request}
    )

    return Response(serializer.data)


@api_view(["POST"])
@permission_classes([AllowAny])
def register(request):

    serializer = RegisterSerializer(
        data=request.data
    )

    if serializer.is_valid():

        user = serializer.save()

        return Response(
            {
                "message": "Registration successful.",
                "user": UserSerializer(user).data,
            },
            status=status.HTTP_201_CREATED
        )

    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def current_user(request):

    serializer = UserSerializer(
        request.user
    )

    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def order_list(request):

    orders = Order.objects.filter(
        user=request.user
    ).prefetch_related(
        "items"
    ).order_by(
        "-created_at"
    )

    serializer = OrderSerializer(
        orders,
        many=True
    )

    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def order_detail(request, order_id):

    try:

        order = Order.objects.prefetch_related(
            "items"
        ).get(
            id=order_id,
            user=request.user
        )

    except Order.DoesNotExist:

        return Response(
            {
                "error": "Order not found."
            },
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = OrderSerializer(order)

    return Response(serializer.data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
@transaction.atomic
def create_order(request):

    data = request.data

    customer = data.get(
        "customer",
        {}
    )

    items = data.get(
        "items",
        []
    )

    if not items:

        return Response(
            {
                "error": "Cart is empty."
            },
            status=status.HTTP_400_BAD_REQUEST
        )

    required_fields = [
        "name",
        "email",
        "phone",
        "address",
        "city",
        "state",
        "pincode",
    ]

    for field in required_fields:

        if not customer.get(field):

            return Response(
                {
                    "error": f"{field} is required."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

    total_amount = Decimal("0.00")

    validated_items = []

    for item in items:

        product_id = item.get("id")
        quantity = item.get("quantity")

        try:

            quantity = int(quantity)

        except (TypeError, ValueError):

            return Response(
                {
                    "error": "Invalid quantity."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        if quantity <= 0:

            return Response(
                {
                    "error": "Quantity must be greater than zero."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        try:

            product = Product.objects.select_for_update().get(
                id=product_id
            )

        except Product.DoesNotExist:

            return Response(
                {
                    "error": f"Product {product_id} not found."
                },
                status=status.HTTP_404_NOT_FOUND
            )

        if product.stock < quantity:

            return Response(
                {
                    "error": (
                        f"Only {product.stock} "
                        f"units of {product.name} are available."
                    )
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        item_total = product.price * quantity

        total_amount += item_total

        validated_items.append(
            {
                "product": product,
                "quantity": quantity,
                "price": product.price,
            }
        )

    order = Order.objects.create(
        user=request.user,
        total_amount=total_amount,
        name=customer["name"],
        email=customer["email"],
        phone=customer["phone"],
        address=customer["address"],
        city=customer["city"],
        state=customer["state"],
        pincode=customer["pincode"],
    )

    for item in validated_items:

        product = item["product"]
        quantity = item["quantity"]

        OrderItem.objects.create(
            order=order,
            product=product,
            quantity=quantity,
            price=item["price"],
        )

        product.stock -= quantity
        product.save(
            update_fields=["stock"]
        )

    serializer = OrderSerializer(order)

    return Response(
        {
            "message": "Order created successfully.",
            "order": serializer.data,
        },
        status=status.HTTP_201_CREATED
    )