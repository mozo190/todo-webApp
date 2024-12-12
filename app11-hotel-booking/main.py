import pandas as pd

df = pd.read_csv('hotels.csv', dtype={'id': str})


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df['id'] == self.hotel_id, 'name'].squeeze()

    def book(self):
        """Book a hotel room by changing the availability status"""
        df.loc[df['id'] == self.hotel_id, 'available'] = "no"
        df.to_csv('hotels.csv', index=False)

    def available_rooms(self):
        """Check if rooms are available"""
        availability = df.loc[df['id'] == self.hotel_id, 'available'].squeeze()
        if availability == "yes":
            return True
        else:
            return False


class Reservation:
    def __init(self, customer_name, hotel):
        print("Generating reservation")

    def generate(self):
        content = f"Reservation for name at {hotel}"
        print(content)
        return content


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel_object = hotel_object
        print("Reservation ticket created")

    def generate(self):
        content = (f"""
                    Thank you for your reservation {self.customer_name} 
                    at {self.hotel_object.name}"""
                   )
        return content


print(df)
hotel_id = input("Enter hotel id: ")
hotel = Hotel(hotel_id)

if hotel.available_rooms():
    hotel.book()
    name = input("Enter customer name: ")
    reservation_ticket = ReservationTicket(customer_name=name, hotel_object=hotel)
    print(reservation_ticket.generate())
else:
    print("No rooms available")
