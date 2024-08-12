# coffee-machine-code
This project is a simple and fun simulation of a coffee machine built using Python. The goal is to mimic the operations of a real coffee machine, where the user can select from different types of coffee, and the machine checks if there are enough resources and money to complete the purchase.

The project is an excellent example of using nested dictionaries to manage resources and requirements efficiently. It's perfect for beginners who want to learn about dictionary operations, user input handling, and basic algorithm design in Python.

Features
Resource Management: The coffee machine uses a nested dictionary to manage its resources, including water, coffee, and milk.

Coffee Selection: The machine offers different types of coffee, each with specific resource requirements.

Money Handling: The machine asks the user to input the amount of money they have in coins and calculates whether they have enough to make a purchase.

Transaction Handling: If the user has enough money and the resources are available, the machine will dispense the coffee; otherwise, it will provide appropriate feedback.

How It Works

Resources Available: The machine has a dictionary that tracks the available resources such as water, coffee, and milk.

Coffee Recipes: Another nested dictionary holds the required resources for each type of coffee (e.g., espresso, latte, cappuccino).

User Interaction: The user is prompted to select a coffee type and input the amount of money they have.

Resource Check: The machine checks if it has enough resources to make the selected coffee.

Transaction Check: The machine checks if the user has provided enough money to purchase the coffee.

Dispense or Reject: Based on the checks, the machine either dispenses the coffee or provides feedback if the transaction cannot be completed.

Example
Espresso Recipe: Requires 50ml of water and 18ml of coffee.

User Interaction: The user selects espresso and inputs $1.00. The machine checks if the resources are sufficient and if the money is enough, then dispenses the coffee.

Requirements
Python 3.x

How to Run

Clone the repository:
Copy code

Navigate to the project directory:
Copy code
cd coffeemachine

Run the Python script:
Copy code
python coffee_machine.py

Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.

This README should give a clear and concise overview of your project and help others understand and use it.
