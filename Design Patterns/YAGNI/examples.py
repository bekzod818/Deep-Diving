"""
YAGNI, which stands for "You Aren't Gonna Need It," is a software development principle that emphasizes avoiding unnecessary code and features. The core idea is to focus on the essential functionality required for the current moment, leaving future enhancements for later when they are actually needed.

Here are some examples of YAGNI in action, with corresponding Python code:
"""

"""
    1. Implementing features only when required:
Instead of implementing a complex login system during the initial development phase, consider using a simpler solution like a temporary token:
"""
# Initial version
user_id = "guest"

# Later, implement a proper login system when needed

"""
    2. Avoiding premature optimization:
Focus on writing clean and functional code initially, and only optimize performance when it becomes a bottleneck:
"""

# Simple, readable code for calculating the sum of numbers
total = sum([1, 2, 3, 4, 5])

# Later, optimize for performance if necessary

"""
    3. Designing flexible code for future needs:
Instead of predicting all future requirements, write code that is flexible and adaptable to change:
"""

# Use generic data structures like dictionaries or lists
data = {"key": "value"}

# Implement logic to handle different data types dynamically

"""
    4. Avoiding overengineering solutions:
Use simple algorithms and data structures when possible, and only add complexity when necessary:
"""

# Use built-in functions for common tasks like file handling
with open("file.txt") as f:
    lines = f.readlines()

# Instead of writing custom functions

"""
    5. Refactoring and removing unused code:
Regularly review your codebase and remove unnecessary features or code that is no longer used:
"""


# Remove unused functions or variables
def unused_function(x):
    pass


# Later, remove the function if it's not used

"""
By following the YAGNI principle, you can focus on delivering working software quickly and efficiently, avoiding unnecessary complexity and wasted effort. It's important to balance YAGNI with other principles like DRY and KISS to ensure code remains maintainable and readable.
"""
