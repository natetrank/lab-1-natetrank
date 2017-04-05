#* Section 1 (Git)
# persnickety
#* Section 2 (Data Definitions)

#* 1)
# a CelsiusTemp is a number representing the temperature in Celsius
# a FahrenheitTemp is a number representing the temperature in Fahrenheit
#* 2)
# a Price is a float representing an item in cents
#* 3)
# a Price is a float
# a Name is a string


# a PriceRecord represents an item in a store database
class PriceRecord:
    def __init__(self, price, name):
        self.price = price  # a Price
        self.name = name  # a Name

    def __repr__(self):
        return ("PriceRecord(%r, %r)" % (self.name, self.price))

    def __eq__(self, other):
        return type(other) == PriceRecord and self.price == other.price and self.name == other.name
#* 4)
# a URL is a string
# a Load_Date is a string representing the date in the form "Month Day, Year"


# an OpenTab represents a Tab that is open in a web browser
class OpenTab:
    def __init__(self, url, load_date):
        self.url = url  # a URL
        self.load_date = load_date  # a LoadDate

    def __repr__(self):
        return("OpenTab(%r, %r)"%(self.url, self.load_date))

    def __eq__(self, other):
        return type(other) == OpenTab and self.url == other.url and self.load_date == other.load_date

#* Section 3 (Signature, Purpose Statements, Headers)

#* 1)

#* 2)

#* 3)

#* 4)

#* Section 4 (Test Cases)

#* 1)

#* 2)

#* 3)

#* Section 5 (Whole Functions)

#* 1)

#* 2)

#* 3)

#* 4)

