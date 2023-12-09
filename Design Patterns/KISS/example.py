"""
The KISS principle, which stands for "Keep It Simple, Stupid," is a valuable guideline in software development. It encourages writing code that is:

    Simple: Easy to understand and maintain.
    Readble: Clearly communicates its purpose.
    Efficient: Uses resources effectively.
    Modular: Divided into reusable components.

Following the KISS principle can lead to code that is more reliable, less prone to bugs, and easier to work with.

Here are some examples of the KISS principle in action, with corresponding Python code:
"""

"""
    1. Using functions to avoid code duplication:
Instead of repeating the same logic for calculating the area of a rectangle multiple times, define a function that can be reused:
"""


def calculate_area(length, width):
    """Calculates the area of a rectangle."""
    return length * width


# Calculate the area of two rectangles
area1 = calculate_area(5, 10)
area2 = calculate_area(3, 7)

print(f"Area of rectangle 1: {area1}")
print(f"Area of rectangle 2: {area2}")

"""
    2. Using descriptive variable names:
Use clear and concise variable names that accurately reflect their purpose:
"""

price = 15.99
tax = 100
shipping_cost = price * tax

# Instead of using cryptic names like "a" or "b"
total_price = price + tax + shipping_cost

product_price = 999.99
sales_tax = total_price * product_price
delivery_fee = sales_tax // 2

# Use descriptive names like:
amount_due = product_price + sales_tax + delivery_fee

"""
    3. Avoiding unnecessary complexity:
Don't over-engineer your solution. Use simple and straightforward algorithms when possible:
"""
# Instead of using a complex sorting algorithm for a small list
sorted_numbers = sorted([5, 2, 8, 1])

# Use a simpler approach for small data sets
largest_number = max([5, 2, 8, 1])

"""
    4. Focusing on readability:
Use proper indentation, whitespace, and comments to make your code easier to read and understand:
"""


def calculate_average(numbers):
    """
    Calculates the average of a list of numbers.
    """
    total = sum(numbers)
    average = total / len(numbers)
    return average


"""
    5. Writing modular code:
Break down your code into smaller, self-contained units that are easier to understand and maintain:
"""


def calculate_discount(price, discount_rate):
    """Calculates the discounted price of a product."""
    discount_amount = price * discount_rate
    discounted_price = price - discount_amount
    return discounted_price


# Use the function in different parts of your program
original_price = 100
discount_rate = 0.2
final_price = calculate_discount(original_price, discount_rate)

"""By following the KISS principle, you can write cleaner, more maintainable, and more reliable Python code."""
