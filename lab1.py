import unittest

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
# add_tax: float -> float
# determine amount of sales tax and adds it to the original price


def add_tax(price):
    pass

#* 2)
# item_price: string -> float
# determines price of an item by accepting the name of the item


def item_price(name):
    pass

#* 3)
# medium_income: string string -> int
# computes median income using a geographic region and given database


def median_income(region, database):
    pass

#* 4)
# overlapping_cities: string string -> string
# determines overlapping cities in an area


def overlapping_cities(region, database):
    pass

#* Section 4 (Test Cases)

#* 1)
# second_largest: num num num -> num
# takes three numbers and returns the second largest


def second_largest(num1, num2, num3):
    pass


def test_second_largest(self):
    self.assertEqual(second_largest(1, 2, 3), 2)
    self.assertEqual(second_largest(2, 4, 1), 2)

#* 2)
# no_caps: string -> boolean
# checks if a string has no capital letters


def no_caps(string):
    pass


def test_no_caps(self):
    self.assertEqual(no_caps("nate"), True)
    self.assertEqual(no_caps("Nate"), False)

#* 3)
# northernmost: string string -> string
# takes two states and return the northernmost


def northernmost(state1, state2):
    pass


def test_northernmost(self):
    self.assertEqual(northernmost("Oregon, California"), "Oregon")
    self.assertEqual(northernmost("Texas", "Washington"), "Washington")

#* Section 5 (Whole Functions)

#* 1)
# a Length is a length in feet
# f2m: float -> float
# takes a length in feet and returns it in meters


def f2m(length):
    return 0.3048 * length

#* 2)
# a Pitch is represented as a frequency in Hz
# a Duration is represented as a length in seconds
# a MusicalNote represents a musical note containing pitch and duration


class MusicalNote:
    def __init__(self, pitch, duration):
        self.pitch = pitch  # a Pitch
        self.duration = duration  # a Duration

    def __repr__(self):
        return "MusicalNote(%r, %r)" % (self.pitch, self.duration)

    def __eq__(self, other):
        return type(other) == MusicalNote \
               and self.pitch == other.pitch \
               and self.duration == other.duration

#* 3)
# up_one_octave: MusicalNote -> MusicalNote
# accepts a note and returns the note one octave higher


def up_one_octave(note):
    new_note = MusicalNote(note.pitch * 2, note.duration)
    return new_note

#* 4)
# up_one_octave_m: MusicalNote -> None
# accepts a note, doubles its frequency and returns None


def up_one_octave_m(note):
    note.pitch *= 2
    return None


class TestCases(unittest.TestCase):
    def test_f2m(self):
        self.assertEqual(f2m(1), 0.3048)
        self.assertEqual(f2m(2.5), 0.762)

    def test_up_one_octave(self):
        note1 = MusicalNote(100, 2)
        note2 = MusicalNote(410, 2.4)
        note1a = MusicalNote(200, 2)
        note2a = MusicalNote(820, 2.4)
        self.assertEqual(up_one_octave(note1), note1a)
        self.assertEqual(up_one_octave(note2), note2a)

    def test_up_one_octave_m(self):
        note1 = MusicalNote(100, 2)
        self.assertEqual(up_one_octave_m(note1), None)

if __name__ == "__main__":
    unittest.main()
