import random

# Dictionary to store wallet balances
wallets = {}

def create_wallet():
    wallet_id = "W" + str(random.randint(1000, 9999))
    wallets[wallet_id] = 100  # Each new wallet starts with 100 coins
    print(f"✅ Wallet created successfully! Wallet ID: {wallet_id}, Balance: 100 coins")

def check_balance():
    wallet_id = input("Enter your wallet ID: ")
    if wallet_id in wallets:
        print(f"💰 Balance for {wallet_id}: {wallets[wallet_id]} coins")
    else:
        print("❌ Wallet not found!")

def transfer_coins():
    sender = input("Enter sender wallet ID: ")
    receiver = input("Enter receiver wallet ID: ")
    amount = int(input("Enter amount to transfer: "))

    if sender not in wallets or receiver not in wallets:
        print("❌ Invalid wallet ID(s).")
        return

    if wallets[sender] < amount:
        print("❌ Not enough balance to transfer.")
        return

    wallets[sender] -= amount
    wallets[receiver] += amount
    print(f"✅ {amount} coins transferred from {sender} to {receiver}.")

def mine_coins():
    wallet_id = input("Enter your wallet ID: ")
    if wallet_id in wallets:
        mined = random.randint(10, 50)
        wallets[wallet_id] += mined
        print(f"⛏️ You mined {mined} coins! New balance: {wallets[wallet_id]}")
    else:
        print("❌ Wallet not found!")

def show_all_wallets():
    print("\n📜 All Wallets and Balances:")
    for w, b in wallets.items():
        print(f"{w} -> {b} coins")

# Main Menu
while True:
    print("\n--- Simple Cryptocurrency Simulation ---")
    print("1. Create Wallet")
    print("2. Check Balance")
    print("3. Transfer Coins")
    print("4. Mine Coins")
    print("5. Show All Wallets")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_wallet()
    elif choice == "2":
        check_balance()
    elif choice == "3":
        transfer_coins()
    elif choice == "4":
        mine_coins()
    elif choice == "5":
        show_all_wallets()
    elif choice == "6":
        print("👋 Exiting... Thank you for using CryptoSim!")
        break
    else:
        print("❌ Invalid choice! Please try again.")
