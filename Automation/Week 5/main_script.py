from Smartcard import Smartcard

# Function to get user input for a smartcard
def get_smartcard_input():
    voorletters = input("Enter voorletters (initials): ")
    tussenvoegsels = input("Enter tussenvoegsels (prefixes): ")
    achternaam = input("Enter achternaam (last name): ")
    return voorletters, tussenvoegsels, achternaam

# Get input for first smartcard
print("Creating first smartcard (personal_ov_1):")
voorletters1, tussenvoegsels1, achternaam1 = get_smartcard_input()
personal_ov_1 = Smartcard(voorletters1, tussenvoegsels1, achternaam1)

# Get input for second smartcard
print("\nCreating second smartcard (personal_ov_2):")
voorletters2, tussenvoegsels2, achternaam2 = get_smartcard_input()
personal_ov_2 = Smartcard(voorletters2, tussenvoegsels2, achternaam2)

# Step 5: Print last name and creation date of each smartcard
print(f"\nPersonal OV 1 - Last Name: {personal_ov_1.achternaam}, Creation Date: {personal_ov_1.creation_date}")
print(f"Personal OV 2 - Last Name: {personal_ov_2.achternaam}, Creation Date: {personal_ov_2.creation_date}")

# Step 6: Call check_name for each user and print the result
check_name_result_1 = personal_ov_1.check_name()
print(f"\nName check for Personal OV 1 ({personal_ov_1}): {check_name_result_1}")

check_name_result_2 = personal_ov_2.check_name()
print(f"Name check for Personal OV 2 ({personal_ov_2}): {check_name_result_2}")

# Deposit 10 euros on both cards
personal_ov_1.load(10)
personal_ov_2.load(10)

# Withdraw 5 euros from the first card
withdraw_result_1 = personal_ov_1.withdraw(5)
if withdraw_result_1 == -1:
    print(f"\nCannot withdraw 5 euros from {personal_ov_1} due to insufficient balance.")
else:
    print(f"\nWithdrew 5 euros from {personal_ov_1}. New balance: {personal_ov_1.balance:.2f} euros.")

# Withdraw 15 euros from the second card
withdraw_result_2 = personal_ov_2.withdraw(15)
if withdraw_result_2 == -1:
    print(f"\nCannot withdraw 15 euros from {personal_ov_2} due to insufficient balance.")
else:
    print(f"\nWithdrew 15 euros from {personal_ov_2}. New balance: {personal_ov_2.balance:.2f} euros.")
