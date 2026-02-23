MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# Fungsi untuk mengecek apakah stok bahan mencukupi resep
def is_resource_sufficient(drink):
    for item in drink["ingredients"]:
        if drink["ingredients"][item] > resources[item]:
            print(f"Sorry, no enough {item}")
            return False
    return True


# Fungsi untuk mengambil data menu berdasarkan input user
def pilihan(jawaban):
    if jawaban in MENU:
        return MENU[jawaban]
    else:
        print("Pilihan anda salah")


# Fungsi untuk menghitung total uang dari koin yang dimasukkan
def process_coins():
    print("Please insert coins.")
    quarters = 0.25 * int(input("How many quarters? "))
    dimes = 0.10 * int(input("How many Dimes? "))
    nickels = 0.05 * int(input("How many Nickels? "))
    pennies = 0.01 * int(input("How many Pennies? "))
    return quarters + dimes + nickels + pennies


# Fungsi untuk mengurangi stok bahan setelah kopi dibuat
def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


profit = 0


# Fungsi untuk validasi pembayaran, hitung kembalian, dan update profit
def is_transaction_successful(money_received, drink_cost):
    global profit
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


# --- LOGIKA UTAMA PROGRAM ---
is_on = True

while is_on:
    question = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if question == "off":
        is_on = False
        print("Machine turned off.")
    elif question == "report":
        print(f"Water : {resources['water']}ml")
        print(f"Milk : {resources['milk']}ml")
        print(f"Coffee : {resources['coffee']}g")
        print(f"Money : ${profit:.2f}")
    else:
        drink = pilihan(question)

        # Validasi awal sebelum memproses pembayaran
        if drink is None:
            continue

        if not is_resource_sufficient(drink):
            continue

        print("You selected:", question)
        print("Cost: $", drink["cost"])

        # Proses Pembayaran
        bayar = process_coins()

        # Eksekusi pembuatan kopi jika transaksi berhasil
        if is_transaction_successful(bayar, drink["cost"]):
            make_coffee(question, drink["ingredients"])