def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None

# Примеры
print(safe_divide(10, 5))
print(safe_divide(5, 0))    # None
print(safe_divide(-4, 2))   # -2.0
print(safe_divide(0, 2))    # 0.0