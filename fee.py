def get_user_input():
  
    monthly_fee = float(input("Enter the monthly fee: "))

    previous_fee = float(input("Enter the previous fee (if any): "))

    is_transportation_user = input("Is the student a transportation user? (yes/no): ").lower() == "yes"

    if is_transportation_user:
        transportation_fee = float(input("Enter the transportation fee: "))
    else:
        transportation_fee = 0

    return monthly_fee, previous_fee, is_transportation_user, transportation_fee

def calculate_school_fee(monthly_fee, previous_fee, is_transportation_user, transportation_fee):

    if is_transportation_user:
        total_fee = monthly_fee + transportation_fee
    else:
        total_fee = monthly_fee

    if previous_fee is not None:
        total_fee += previous_fee

    return total_fee

monthly_fee, previous_fee, is_transportation_user, transportation_fee = get_user_input()

total_fee = calculate_school_fee(monthly_fee, previous_fee, is_transportation_user, transportation_fee)
print(f"The total school fee is: {total_fee}")