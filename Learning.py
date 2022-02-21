class User:

    def __init__(self, first_name: str, last_name: str, phone_number: int, email_id: str, address: str):
        # Validation checks
        assert len(first_name) >= 3, "First Name should at least contain 3 letters"
        assert len(last_name) >= 3, "Last Name should at least contain 3 letters"
        assert len(str(phone_number)) == 10, f"The entered Phone Number {phone_number} is not equal to 10 digits"

        # Assign to self object
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email_id = email_id
        self.address = address

    def __repr__(self):
        return f"User('{self.first_name}', '{self.last_name}', {self.phone_number}, '{self.email_id}', '{self.address}')"



user1 = User("Bhuvan", "Teja", 9035827905, "tejabtr753@gmail.com", "Hebbal")

print(user1.first_name)
print(user1.last_name)
print(user1)
