from .models import Cart,CartItem
from .views import __cart_id__

def counter(request):
    cart_count = 0
    if 'admin' in request.path:
        return{}
    else:
        try:
            cart = Cart.objects.filter(cart_id = __cart_id__(request))
            if request.user.is_authenticated:
                cart_items = CartItem.objects.all().filter(user=request.user)
            else:
                cart_items = CartItem.objects.all().filter(cart=cart[:1])
                
            for cart_item in cart_items:
                cart_count += cart_item.quantity
                
        except Cart.DoesNotExit:
            cart_count = 0
    return dict(cart_count = cart_count)