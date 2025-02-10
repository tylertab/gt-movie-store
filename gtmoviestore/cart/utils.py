def calculate_cart_total(cart,movies_in_cart):
    total = 0
    for movie in movies_in_cart:
        quantity = cart[str(movie.id)]
        total += int(quantity) * movie.price
    return total

