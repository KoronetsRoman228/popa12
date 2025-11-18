shop = {
    "молоко": 35.50,
    "хліб": 22.00,
    "яйця": 58.75,
    "масло": 120.00,
    "сир": 95.30,
    "цукор": 42.15
}


def format_price(price):
    """Форматує ціну: 100 -> 'ціна: 100.00 грн'"""
    return f"ціна: {price:.2f} грн"


def check_availability(*products):
    """Перевіряє наявність товарів, повертає {товар: True/False}"""
    return {product: product in shop for product in products}


def show_products():
    """Показує список всіх товарів"""
    print("\nТОВАРИ В МАГАЗИНІ:")
    print("-" * 35)
    for product, price in shop.items():
        print(f"  {product}: {format_price(price)}")
    print("-" * 35)


def process_order(*items):
    """Обробляє замовлення та показує ціну"""
    # Перевірка наявності
    availability = check_availability(*items)
    
    if not all(availability.values()):
        print("\nТоварів немає в наявності:")
        for item, available in availability.items():
            if not available:
                print(f"  - {item}")
        return None
    
    # Підрахунок ціни
    total = sum(shop[item] for item in items)
    print("\nВаше замовлення:")
    for item in items:
        print(f"  {item}: {format_price(shop[item])}")
    print(f"\nВсього: {format_price(total)}")
    return total


# Головна програма
print("=" * 35)
print("ЛАСКАВО ПРОСИМО ДО МАГАЗИНУ!")
print("=" * 35)

while True:
    print("\n МЕНЮ:")
    print("1 - Переглянути товари")
    print("2 - Переглянути ціну")
    print("3 - Купити")
    print("0 - Вийти")
    
    choice = input("\nВаш вибір: ").strip()
    
    if choice == "0":
        print("\n Дякуємо! До побачення!")
        break
    
    elif choice == "1":
        show_products()
    
    elif choice in ["2", "3"]:
        show_products()  # Показуємо товари перед замовленням
        order = input("\nВведіть товари через кому: ").strip()
        
        if order:
            items = [item.strip() for item in order.split(",")]
            total = process_order(*items)
            
            if choice == "3" and total:
                confirm = input("\nПідтвердити покупку? (так/ні): ").lower()
                if confirm in ["так", "т", "yes", "y"]:
                    print(f"\nПокупку оформлено!")
                    print(f"До сплати: {format_price(total)}")
                else:
                    print("\nПокупку скасовано")
        else:
            print("Ви нічого не ввели!")
    
    else:
        print("Невірний вибір! Оберіть 0-3")
