price = float(input("Введите стоимость товара: "))
if price > 1500:
    discount = 20
elif price > 1000:
    discount = 15
elif price > 500:
    discount = 10
elif price > 100:
    discount = 5
amount = price * discount / 100
price_with_discount = price - amount
print(f"Цена товара со скидкой", discount, "%:", price_with_discount)
