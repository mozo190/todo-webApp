import pandas as pd

df = pd.read_csv('hotels.csv')


class Hotel:
    def __init__(self, id):
        self.id = id
        print("Hotel object created")

    def book(self):
        print("Booking hotel")

    def available_rooms(self):
        print("Checking available rooms")


class Reservation:
    def generate(self):
        print("Generating reservation")

    def generate(self):
        content = f"Reservation for name at {hotel}"
        print(content)
        return content


class ReservationTicket:
    def __init__(self, customer_name, hotel):
        self.customer_name = customer_name
        self.hotel = hotel
        print("Reservation ticket created")

    def generate(self):
        print("Generating reservation ticket")


print(df)
id = input("Enter hotel id: ")
hotel = Hotel(id)

if hotel.available_rooms():
    hotel.book()
    customer_name = input("Enter customer name: ")
    reservation_ticket = ReservationTicket(customer_name, hotel)
    print(reservation_ticket.generate())
