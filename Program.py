import random

booking_register = [
    "Amani Kamau", "Atieno Mwangi", "Akinyi Maina", "Kamau Njeri",
    "Mwangi Ochieng", "Maina Odhiambo", "Njeri Omondi", "Ochieng Wanjiku",
    "Odhiambo Wambui", "Omondi Wangechi", "Wanjiku Wanyama", "Wambui Wekesa",
    "Wangechi Amani", "Wanyama Atieno", "Wekesa Akinyi"
]

allowed_attendees = []

def check_attendee(booking_register, allowed_attendees):
    first_name = input("Enter your First Name: ").capitalize()
    last_name = input("Enter your Last Name: ").capitalize()
    full_name = f"{first_name} {last_name}"

    if full_name in booking_register:
        if full_name not in allowed_attendees:
            print("Welcome! You are on the booking register.")
            allowed_attendees.append(full_name)
            assign_seats([full_name])
        else:
            print("You have already been allowed in.")
    else:
        print("Sorry, your name is not on the booking register.")
        register_choice = input("Do you want to register? (yes/no): ").lower()
        if register_choice == "yes":
            booking_register.append(full_name)
            print(f"Thank you, {full_name}! You have been registered. Proceed to check in")
        else:
            print("Thank you. Goodbye.")

def assign_seats(attendees):
    if len(attendees) > 20:
        print("Event capacity reached. No more bookings allowed.")
        return

    print("\nAssigning random seating arrangements and chair numbers:")
    seating_arrangements = random.sample(attendees, len(attendees))

    for index, attendee in enumerate(seating_arrangements, start=1):
        chair_number = random.randint(1, 20)  # Assuming there are 20 chairs
        print(f"Seat {index}: {attendee} (Chair {chair_number})")

# Usage
check_attendee(booking_register, allowed_attendees) 