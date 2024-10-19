class Smartcard:
    """
    The Smartcard class represents an OV-chipkaart (public transport card) with personal information and balance.
    Each card has a unique card number, creation date, and personal data.
    """

    # Class variable for unique card numbers
    _card_number_counter = 0

    def __init__(self, voorletters, tussenvoegsels, achternaam):
        """
        Initializes a new Smartcard with personal data and creation date.

        Parameters:
            voorletters (str): Initials of the cardholder.
            tussenvoegsels (str): Prefixes in the cardholder's name.
            achternaam (str): Last name of the cardholder.
        """
        self.voorletters = voorletters
        self.tussenvoegsels = tussenvoegsels
        self.achternaam = achternaam

        # Increment the class counter and assign a unique card number
        Smartcard._card_number_counter += 1
        self.card_number = Smartcard._card_number_counter

        # Set creation date using datetime module
        from datetime import datetime
        self.creation_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Initialize balance to zero
        self.balance = 0.0

    def check_name(self):
        """
        Checks if the total number of characters in voorletters, tussenvoegsels, and achternaam
        does not exceed 26 characters.

        Returns:
            bool: True if valid (<=26 characters), False otherwise.
        """
        total_length = len(self.voorletters + self.tussenvoegsels + self.achternaam)
        return total_length <= 26

    def load(self, amount):
        """
        Adds money to the card balance.

        Parameters:
            amount (float): The amount of money to add.

        Returns:
            None
        """
        self.balance += amount

    def withdraw(self, amount):
        """
        Deducts money from the card balance.

        Parameters:
            amount (float): The amount of money to deduct.

        Returns:
            int: -1 if the operation would result in a negative balance, otherwise None.
        """
        if self.balance - amount < 0:
            return -1
        else:
            self.balance -= amount

    def __str__(self):
        """
        Returns the full name of the cardholder with spaces in the right places.

        Returns:
            str: A string representing the full name.
        """
        full_name = f"{self.voorletters} {self.tussenvoegsels} {self.achternaam}".replace("  ", " ").strip()
        return full_name
