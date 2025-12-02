from validators import validate_positive


@validate_positive
def calculate_area(width, height):
    """Обчислює площу прямокутника"""
    return width * height


@validate_positive
def calculate_discount(price, discount_percent):
    """Обчислює ціну зі знижкою"""
    discount = price * (discount_percent / 100)
    return price - discount


def main():
    print("Тестування декоратора валідації даних\n")
    
    # Тест 1: Коректні дані
    print("Тест 1: Коректні додатні числа")
    try:
        area = calculate_area(5, 10)
        print(f"✓ Площа (5, 10): {area}")
    except ValueError as e:
        print(f"✗ Помилка: {e}")
    
    # Тест 2: Від'ємне число
    print("\nТест 2: Від'ємне число")
    try:
        area = calculate_area(-5, 10)
        print(f"✓ Площа (-5, 10): {area}")
    except ValueError as e:
        print(f"✗ {e}")
    
    # Тест 3: Нульове значення
    print("\nТест 3: Нульове значення")
    try:
        area = calculate_area(0, 10)
        print(f"✓ Площа (0, 10): {area}")
    except ValueError as e:
        print(f"✗ {e}")
    
    # Тест 4: Знижка
    print("\nТест 4: Розрахунок знижки")
    try:
        price = calculate_discount(1000, 15)
        print(f"✓ Ціна зі знижкою 15%: {price} грн")
    except ValueError as e:
        print(f"✗ {e}")
    
    # Тест 5: Від'ємна знижка
    print("\nТест 5: Від'ємна знижка")
    try:
        price = calculate_discount(1000, -10)
        print(f"✓ Ціна зі знижкою -10%: {price} грн")
    except ValueError as e:
        print(f"✗ {e}")


if __name__ == "__main__":
    main()
