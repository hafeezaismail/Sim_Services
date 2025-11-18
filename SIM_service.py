balance = 500

def check_balance():
    print(f"\nYour current balance is: Rs {balance}\n")

def recharge_balance():
    global balance
    amount = int(input("\nEnter amount to recharge: Rs "))
    if amount > 0:
        balance += amount
        print(f"Recharge successful! New balance: Rs {balance}\n")
    else:
        print("Invalid amount!\n")

def subscribe_internet_package():
    global balance
    print("\nAvailable Internet Packages:")
    print("1. 1GB - Rs 100")
    print("2. 3GB - Rs 250")
    print("3. 10GB - Rs 600")

    choice = input("Select package (1-3): ")

    if choice == "1":
        cost = 100
    elif choice == "2":
        cost = 250
    elif choice == "3":
        cost = 600
    else:
        print("Invalid choice!\n")
        return

    if balance >= cost:
        balance -= cost
        print(f"Package subscribed successfully! Remaining balance: Rs {balance}\n")
    else:
        print("Insufficient balance!\n")
def call_packages():
    global balance
    print("\nAvailable Call Packages:")
    print("1. 100 Minutes - Rs 50")
    print("2. 500 Minutes - Rs 200")
    print("3. Unlimited (Daily) - Rs 80")

    choice = input("Select package (1-3): ")

    if choice == "1":
        cost = 50
    elif choice == "2":
        cost = 200
    elif choice == "3":
        cost = 80
    else:
        print("Invalid choice!\n")
        return

    if balance >= cost:
        balance -= cost
        print(f"Call package activated! Remaining balance: Rs {balance}\n")
    else:
        print("Insufficient balance!\n")

def sim_info():
    print("\nSIM Details")
    print("Network: Zong 4G")
    print("Type: Prepaid")
    print("Account Status: Active\n")

def main_menu():
    while True:
        print("--- WELCOME TO SIM SERVICE CARE ---")
        print("1. Check Balance")
        print("2. Recharge SIM")
        print("3. Internet Packages")
        print("4. Call Packages")
        print("5. SIM Information")
        print("6. Exit")

        user_choice = input("Select a service (1-6): ")

        if user_choice == "1":
            check_balance()
        elif user_choice == "2":
            recharge_balance()
        elif user_choice == "3":
            subscribe_internet_package()
        elif user_choice == "4":
            call_packages()
        elif user_choice == "5":
            sim_info()
        elif user_choice == "6":
            print("\nThank you for using SIM Service Care!\n")
            break
        else:
            print("\nInvalid option! Please select 1–6.\n")
main_menu()