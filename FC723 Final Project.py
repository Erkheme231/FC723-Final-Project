import uuid
import random
import string

class SeatBookingSystem:
    def __init__(self, rows, columns):
        # Initialize the floor plan with 'F' for free seats and 'X' for aisles
        self.rows = rows
        self.columns = columns
        self.available_seats = [f"{i+1}{chr(j+65)}" for i in range(self.rows) for j in range(self.columns)]
        self.booked_seats = {}
        self.passenger_details = {}  # Store traveler details in a dictionary

    def display_seats(self):
        # Display the current seating arrangement
        for i in range(0, len(self.available_seats), self.columns):
            print(' '.join(self.available_seats[i:i+self.columns]))

    def book_seat(self, seat, passport_number, first_name, last_name):
        # Book the given seat if available
        seat = seat.upper()  # Convert seat to uppercase
        if not self._is_valid_seat(seat):
            print(f'Invalid seat format. Please enter the seat in the format "RowLetter" (e.g., "1A", "2B", etc.).')
            return
        if seat not in self.available_seats:
            print(f'Sorry, seat {seat} is not available.')
        elif seat in self.booked_seats:
            print(f'Seat {seat} is already booked.')
        else:
            booking_reference = self.generate_booking_reference()  # Generate booking reference
            self.available_seats.remove(seat)
            self.booked_seats[seat] = booking_reference  # Store booking reference
            # Store traveler details
            self.passenger_details[booking_reference] = {
                'passport_number': passport_number,
                'first_name': first_name,
                'last_name': last_name,
                'seat_row': int(seat[:-1]),  # Extract row number from seat
                'seat_column': seat[-1]  # Extract column letter from seat
            }
            print(f'Seat {seat} booked successfully. Booking reference: {booking_reference}')

    def free_seat(self, seat):
        # Free the given seat if booked
        if seat in self.booked_seats:
            self.available_seats.append(seat)
            self.available_seats.sort()  # Ensure seats are sorted after adding
            booking_reference = self.booked_seats.pop(seat)  # Remove booking reference
            # Remove traveler details
            self.passenger_details.pop(booking_reference, None)
            print(f'Seat {seat} freed successfully.')
        else:
            print(f'No booking found for seat {seat}.')

    def show_booking_state(self):
        # Display the current booking state
        print("Available seats:")
        self.display_seats()
        print("\nBooked seats:")
        for seat, reference in self.booked_seats.items():
            print(f"Seat {seat} - Booking Reference: {reference}")
            # Print traveler details
            details = self.passenger_details.get(reference, {})
            if details:
                print(f"  Passenger: {details['first_name']} {details['last_name']}")
                print(f"  Passport Number: {details['passport_number']}")
                print(f"  Seat Row: {details['seat_row']}, Seat Column: {details['seat_column']}")

    def check_availability(self, seat):
        # Check if the given seat is available
        if seat.upper() in self.available_seats:  # Convert seat to uppercase
            print(f'Seat {seat} is available.')
        elif seat.upper() in self.booked_seats:
            print(f'Seat {seat} is already booked.')
        else:
            print(f'Seat {seat} is not available.')

    def generate_booking_reference(self):
        """
        Generate a random and unique booking reference with exactly eight alphanumeric characters.

        Returns:
            str: A unique booking reference.
        """
        while True:
            # Generate a random reference with alphanumeric characters
            reference = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
            # Check if reference is unique
            if reference not in self.booked_seats.values():
                return reference

    def _is_valid_seat(self, seat):
        # Check if the seat format is valid (e.g., "1A", "2B", ..., "80F")
        row = seat[:-1]
        column = seat[-1].upper()

        # Check if row is a digit and within the range of available rows
        if row.isdigit() and 1 <= int(row) <= self.rows:
            # Check if column is an uppercase letter and within the range of available columns
            if column.isalpha() and column in [chr(i) for i in range(65, 65 + self.columns)]:
                return True

        # If the format is invalid, return False
        return False


# Main function to drive the program
if __name__ == "__main__":
    rows = 80 # Number of rows
    columns = 6 # Number of columns

    # Initialize seat booking system
    seat_booking_system = SeatBookingSystem(rows, columns)

    # Menu-driven interface
    while True:
        print("\nWelcome to Apache Airlines Seat Booking System")
        print("1. Check availability of seat")
        print("2. Book a seat")
        print("3. Free a seat")
        print("4. Show booking state")
        print("5. Exit program")

        choice = input("Enter your choice: ")

        if choice == "1":
            seat = input("Enter the seat you want to check availability for (e.g., 1A): ")
            seat_booking_system.check_availability(seat)
        elif choice == "2":
            seat = input("Enter the seat you want to book (e.g., 1A): ")
            passport_number = input("Enter passenger's passport number: ")
            first_name = input("Enter passenger's first name: ")
            last_name = input("Enter passenger's last name: ")
            seat_booking_system.book_seat(seat, passport_number, first_name, last_name)
        elif choice == "3":
            seat = input("Enter the seat you want to free (cancel booking for): ")
            seat_booking_system.free_seat(seat)
        elif choice == "4":
            seat_booking_system.show_booking_state()
        elif choice == "5":
            print("Thank you for using Apache Airlines Seat Booking System. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")
