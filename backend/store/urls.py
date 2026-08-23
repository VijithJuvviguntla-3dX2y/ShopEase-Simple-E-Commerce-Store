from django.urls import path  # type: ignore
from rest_framework_simplejwt.views import (  # type: ignore
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import (
    create_order,
    current_user,
    order_detail,
    order_list,
    product_detail,
    product_list,
    register,
)

urlpatterns = [

    # Products
    path(
        "products/",
        product_list,
        name="product-list"
    ),

    path(
        "products/<int:product_id>/",
        product_detail,
        name="product-detail"
    ),

    # Authentication
    path(
        "auth/register/",
        register,
        name="register"
    ),

    path(
        "auth/login/",
        TokenObtainPairView.as_view(),
        name="login"
    ),

    path(
        "auth/token/refresh/",
        TokenRefreshView.as_view(),
        name="token-refresh"
    ),

    path(
        "auth/user/",
        current_user,
        name="current-user"
    ),

    # Orders
    path(
        "orders/",
        order_list,
        name="order-list"
    ),

    path(
        "orders/create/",
        create_order,
        name="create-order"
    ),

    path(
        "orders/<int:order_id>/",
        order_detail,
        name="order-detail"
    ),
]

{  # noqa: B018
    "python.analysis.extraPaths": ["./path/to/compiled/modules"]
}