import pandas as pd

df = pd.read_csv('hotels.csv')


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        print("Hotel object created")

    def book(self):
        print("Booking hotel")

    def available_rooms(self):
        availability = df.loc[df['hotel_id'] == self.hotel_id, 'available'].squeeze()
        if availability:
            return True
        else:
            return False


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
hotel_id = input("Enter hotel id: ")
hotel = Hotel(hotel_id)

if hotel.available_rooms():
    hotel.book()
    customer_name = input("Enter customer name: ")
    reservation_ticket = ReservationTicket(customer_name, hotel)
    print(reservation_ticket.generate())
else:
    print("No rooms available")