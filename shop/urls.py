
from django.urls import path
from . import views

urlpatterns = [
    # Homepage and product listings
    path('', views.home, name='home'),
    path('products/', views.product_list, name='product_list'),

    # Product details
    path(
        'products/<int:product_id>/',
        views.product_detail,
        name='product_detail'
    ),

    # Shopping cart
    path('cart/', views.view_cart, name='view_cart'),
    path(
        'cart/add/<int:product_id>/',
        views.add_to_cart,
        name='add_to_cart'
    ),
    path(
        'cart/remove/<int:product_id>/',
        views.remove_from_cart,
        name='remove_from_cart'
    ),
    path(
        'cart/update/<int:product_id>/',
        views.update_cart,
        name='update_cart'
    ),

    # User authentication
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    # Checkout and orders
    path('checkout/', views.checkout, name='checkout'),
    path(
        'orders/<int:order_id>/confirmation/',
        views.order_confirmation,
        name='order_confirmation'
    ),
    path('my-orders/', views.order_history, name='order_history'),
   
]
