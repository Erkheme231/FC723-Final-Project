class SeatBookingSystem:
    def __init__(self, rows, columns):
        # Initialize the floor plan with 'F' for free seats and 'X' for aisles
        self.rows = rows
        self.columns = columns
        self.floor_plan = []
        for i in range(self.rows):
            row = [f"{i + 1}{chr(j + 65)}" for j in range(self.columns)]
            self.floor_plan.append(row)

    def display_seats(self):
        # Display the current seating arrangement
        for row in self.floor_plan:
            print(' '.join(row))

    def book_seat(self, seat):
        # Book the given seat if available
        for row in self.floor_plan:
            if seat in row and row[row.index(seat)] == 'F':
                row[row.index(seat)] = 'R'
                print(f'Seat {seat} booked successfully.')
                return
        print(f'Sorry, seat {seat} is not available.')

    def free_seat(self, seat):
        # Free the given seat if booked
        for row in self.floor_plan:
            if seat in row and row[row.index(seat)] == 'R':
                row[row.index(seat)] = 'F'
                print(f'Seat {seat} freed successfully.')
                return
        print(f'No booking found for seat {seat}.')

    def show_booking_state(self):
        # Display the current booking state
        for row in self.floor_plan:
            print(' '.join(row))

    def check_availability(self, seat):
        # Check if the given seat is available
        for row in self.floor_plan:
            if seat in row and row[row.index(seat)] == 'F':
                print(f'Seat {seat} is available.')
                return
        print(f'Seat {seat} is not available.')


# Main function to drive the program
if __name__ == "__main__":
    rows = 6  # Number of rows
    columns = 10  # Number of columns

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
            seat_booking_system.book_seat(seat)
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
