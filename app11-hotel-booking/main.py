import pandas as pd

df = pd.read_csv('hotels.csv', dtype={'id': str})
df_card = pd.read_csv('cards.csv', dtype=str).to_dict(orient='records')
df_cards_security = pd.read_csv('card_security.csv', dtype=str)


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


class SpaTicket(ReservationTicket):
    def generate(self):
        content = (f"""
                    Thank you for your SPA reservation {self.customer_name} !
                    at {self.hotel_object.name}
                    You have a free spa ticket!"""
                   )
        return content


class CreditCard:
    def __init__(self, number):
        self.number = number

    def validate(self, expiration_date, holder, cvc):
        card_data = {"number": self.number,
                     "expiration_date": expiration_date,
                     "holder": holder,
                     "cvc": cvc}
        if card_data in df_card:
            return True
        else:
            return False


class CreditCardSecurity(CreditCard):
    def authenticate(self, given_password):
        password = df_cards_security.loc[df_cards_security['number'] == self.number, 'password'].squeeze()
        return password == given_password


print(df)
hotel_id = input("Enter hotel id: ")
hotel = Hotel(hotel_id)

if hotel.available_rooms():
    credit_card = CreditCardSecurity(number="1234567890123456")
    if credit_card.validate(expiration_date="12/12", holder="JOHN SMITH", cvc="123"):
        if credit_card.authenticate(given_password="mypass"):
            hotel.book()
            name = input("Enter customer name: ")
            reservation_ticket = ReservationTicket(customer_name=name, hotel_object=hotel)
            print(reservation_ticket.generate())
            spa = input("Do you want to book a SPA? (yes/no): ")
            if spa == "yes":
                spa_ticket = SpaTicket(customer_name=name, hotel_object=hotel)
                print(spa_ticket.generate())
            else:
                print("No SPA booked, thank you!")
        else:
            print("Wrong password!")
    else:
        print("No valid creditcard!")
else:
    print("No rooms available")
