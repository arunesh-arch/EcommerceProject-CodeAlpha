
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from decimal import Decimal
from django.contrib.auth.decorators import login_required
from django.db import transaction
from .models import Product, Order, OrderItem

from .models import Product


# Homepage
def home(request):
    products = Product.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'products': products})


# Product detail
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(
        request,
        'product_detail.html',
        {'product': product}
    )


# Add product to cart
@require_POST
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    try:
        quantity = int(request.POST.get('quantity', 1))
    except (ValueError, TypeError):
        messages.error(request, "Please enter a valid quantity.")
        return redirect('product_detail', product_id=product.id)

    if quantity < 1:
        messages.error(request, "Quantity must be at least 1.")
        return redirect('product_detail', product_id=product.id)

    cart = request.session.get('cart', {})
    product_key = str(product.id)

    try:
        current_quantity = int(cart.get(product_key, 0))
    except (ValueError, TypeError):
        current_quantity = 0

    if current_quantity < 0:
        current_quantity = 0

    if current_quantity + quantity > product.stock:
        messages.error(
            request,
            f"Only {product.stock} unit(s) of "
            f"{product.name} are available."
        )
    else:
        cart[product_key] = current_quantity + quantity
        request.session['cart'] = cart
        messages.success(
            request,
            f"{product.name} added to your cart."
        )

    return redirect('product_detail', product_id=product.id)


# View shopping cart
def view_cart(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0

    for product_id, quantity in cart.items():
        try:
            product = Product.objects.get(id=int(product_id))
            quantity = int(quantity)
        except (Product.DoesNotExist, ValueError, TypeError):
            continue

        if quantity < 1:
            continue

        subtotal = product.price * quantity
        total += subtotal

        cart_items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal,
        })

    return render(
        request,
        'cart.html',
        {
            'cart_items': cart_items,
            'total': total,
        }
    )


# Remove product from cart
@require_POST
def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    product_key = str(product_id)

    if product_key in cart:
        del cart[product_key]
        request.session['cart'] = cart

    return redirect('view_cart')


# Update cart quantity
@require_POST
def update_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get('cart', {})
    product_key = str(product_id)

    if product_key not in cart:
        return redirect('view_cart')

    try:
        quantity = int(request.POST.get('quantity', 1))
    except (ValueError, TypeError):
        messages.error(request, "Please enter a valid quantity.")
        return redirect('view_cart')

    if quantity < 1:
        del cart[product_key]
        messages.success(request, "Item removed from your cart.")

    elif quantity > product.stock:
        messages.error(
            request,
            f"Only {product.stock} unit(s) of "
            f"{product.name} are available."
        )

    else:
        cart[product_key] = quantity
        messages.success(request, "Cart quantity updated.")

    request.session['cart'] = cart
    return redirect('view_cart')


# User registration
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(
                request,
                "Account created successfully!"
            )
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})


# User login
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(
                request,
                "You are now logged in!"
            )
            return redirect('home')
    else:
        form = AuthenticationForm(request)

    return render(request, 'login.html', {'form': form})


# User logout - POST request only
@require_POST
def user_logout(request):
    logout(request)
    messages.success(
        request,
        "You have been logged out."
    )
    return redirect('home')

# Checkout
@login_required
@require_POST
def checkout(request):
    cart = request.session.get('cart', {})

    if not isinstance(cart, dict) or not cart:
        messages.error(request, "Your cart is empty.")
        return redirect('view_cart')

    try:
        with transaction.atomic():
            products = []

            # Validate products and quantities before creating the order.
            for product_id, quantity in cart.items():
                product = Product.objects.get(id=int(product_id))
                quantity = int(quantity)

                if quantity < 1:
                    raise ValueError("Invalid product quantity.")

                if quantity > product.stock:
                    raise ValueError(
                        f"Only {product.stock} unit(s) of "
                        f"{product.name} are available."
                    )

                products.append((product, quantity))

            if not products:
                raise ValueError("Your cart is empty.")

            # Calculate the total using database prices.
            total = sum(
                (product.price * quantity
                 for product, quantity in products),
                Decimal("0.00")
            )

            # Create the order.
            order = Order.objects.create(
                customer=request.user,
                total_amount=total
            )

            # Save order items and update stock.
            for product, quantity in products:
                OrderItem.objects.create(
                    order=order,
                    product=product,
                    product_name=product.name,
                    price=product.price,
                    quantity=quantity
                )

                product.stock -= quantity
                product.save(update_fields=['stock'])

        # Clear the cart only after the transaction succeeds.
        request.session['cart'] = {}
        messages.success(
            request,
            f"Order #{order.id} placed successfully!"
        )
        return redirect('order_confirmation', order_id=order.id)

    except (Product.DoesNotExist, ValueError, TypeError, OverflowError):
        messages.error(
            request,
            "Checkout failed. Please check your cart and available stock."
        )
        return redirect('view_cart')
@login_required
def order_confirmation(request, order_id):
    order = get_object_or_404(
        Order,
        id=order_id,
        customer=request.user
    )

    return render(
        request,
        'order_confirmation.html',
        {'order': order}
    )
# Customer order history
@login_required
def order_history(request):
    orders = Order.objects.filter(
        customer=request.user
    ).order_by('-created_at')

    return render(
        request,
        'order_history.html',
        {'orders': orders}
    )
def product_list(request):
    products = Product.objects.all().order_by('-created_at')
    return render(request, 'product_list.html', {
        'products': products
    })