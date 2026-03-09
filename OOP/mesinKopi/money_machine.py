class MoneyMachine:
    def __init__(self):
        self.profit = 0

    def report(self):
        print(f"Money: ${self.profit}")

    def make_payment(self, cost):
        print("Please insert coins.")
        quarters = 0.25 * int(input("How many quarters? "))
        dimes = 0.10 * int(input("How many dimes? "))
        nickels = 0.05 * int(input("How many nickels? "))
        pennies = 0.01 * int(input("How many pennies? "))

        total = quarters + dimes + nickels + pennies

        if total >= cost:
            change = round(total - cost, 2)
            print(f"Here is ${change} in change.")
            self.profit += cost
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            return False