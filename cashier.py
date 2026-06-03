class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        print("Please insert coins.")
        total = int(input("how many large dollars?: ")) * 1.0
        total += int(input("how many half dollars?: ")) * 0.5
        total += int(input("how many quarters?: ")) * 0.25
        total += int(input("how many nickels?: ")) * 0.05
        return round(total, 2)

    def transaction_result(self, coins, cost):
        if coins < cost:
            print("Sorry that's not enough money. Money refunded.")
            return False
        print(f"Here is ${round(coins - cost, 2)} in change.")
        return True