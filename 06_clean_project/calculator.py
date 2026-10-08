def add(first_number: float, second_number: float) -> float:
    return first_number + second_number

def multiply(first_number: float, second_number: float) -> float:
    return first_number * second_number

def calculate_total(price: float, quantity: int) -> float:
    if price < 0 or quantity < 0:
        raise ValueError("Price and quantity must be non-negative")
    return price * quantity

if __name__ == "__main__":
    print(add(10, 20))
    print(multiply(5, 4))
