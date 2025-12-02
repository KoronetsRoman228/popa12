def validate_positive(func):
    """
    Декоратор для валідації даних - перевіряє, що всі аргументи є додатніми числами.
    """
    def wrapper(*args, **kwargs):
        # Перевіряємо всі позиційні аргументи
        for arg in args:
            if not isinstance(arg, (int, float)) or arg <= 0:
                raise ValueError(f"Аргумент {arg} повинен бути додатнім числом")
        
        # Перевіряємо всі іменовані аргументи
        for key, value in kwargs.items():
            if not isinstance(value, (int, float)) or value <= 0:
                raise ValueError(f"Аргумент {key}={value} повинен бути додатнім числом")
        
        # Якщо все добре, викликаємо оригінальну функцію
        return func(*args, **kwargs)
    
    return wrapper


