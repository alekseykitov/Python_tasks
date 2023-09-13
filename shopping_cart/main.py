from collections import defaultdict

# class shoping_cart:
#     def __init__(self, product):


class Product:
    def __init__(
            self,
            product_name: str,
            price_per_unit: float,
            unit_of_mesurement: str,
            ):
        self.product_name = product_name
        self.price_per_unit = price_per_unit
        self.unit_of_mesurement = unit_of_mesurement

    def __hash__(self) -> int: # Хэш функция, преобразует объект в уникальное число (Дандер или магический метод)
        return hash((
            self.product_name,
            self.price_per_unit,
            self.unit_of_mesurement,
        ))
    

apple = Product(
    product_name='Green Apple',
    price_per_unit=1.0,
    unit_of_mesurement='kg'
)


class Cart:
    def __init__(self)-> None:
        self.shopping_cart: defaultdict[Product, int] = defaultdict(int) # x = defaultdict(int); x[product] += 5; return x[product_that_doesnt_exist]
    # add(self, product: Product, quantity: int)
    
    def add(self, product: Product, quantity: int) -> None:
        # if product not in self.shopping_cart:
        #     self.shopping_cart[product] = quantity
        # else:
        #     self.shopping_cart[product] += quantity
        self.shopping_cart[product] += quantity

    def remove(self, product: Product, quantity: int = 0) -> None:
        if product not in self.shopping_cart:
            return
        if quantity > 0:
            self.shopping_cart[product] -= quantity
        if quantity == 0 or self.shopping_cart[product] <= 0:
            self.shopping_cart.pop(product)
            
 
    def clear(self) -> None:
        self.shopping_cart.clear()

    @property #Преобразование в свойство
    def total_price(self) -> float:
        count = 0
        for product, quantity in self.shopping_cart.items():
            count += quantity * product.price_per_unit
        return count

    def __str__(self) -> str:
        lines = []
        for product, quantity in self.shopping_cart.items():
            # lines.append(
            #     f'{product.product_name} ${product.price_per_unit} '
            #     f'* {quantity}{product.unit_of_mesurement} '
            #     f'= {product.price_per_unit * quantity} ')
            lines.append('{name} ${price} * {qty}{units} = {total}'.format(
                name=product.product_name,
                price=product.price_per_unit,
                qty=quantity,
                units=product.unit_of_mesurement,
                total=product.price_per_unit * quantity
            ))
        lines.append(f'total = {self.total_price}')
        return '\n'.join(lines)


print(Cart().total_price)

