from unittest import TestCase, main
from project.trip import Trip


class TestTrip(TestCase):

    def setUp(self):
        self.trip = Trip(100_000, 10, True)

    def test_correct_init(self):
        self.assertEqual(100000, self.trip.budget)
        self.assertEqual(10, self.trip.travelers)
        self.assertEqual(True, self.trip.is_family)
        self.assertEqual({}, self.trip.booked_destinations_paid_amounts)

    def test_travelers_where_less_than_one(self):
        with self.assertRaises(ValueError) as ve:
            self.trip.travelers = 0

        self.assertEqual('At least one traveler is required!', str(ve.exception))

    def test_is_family_where_value_and_travelers_less_than_two(self):
        self.trip.travelers = 1
        self.trip.is_family = True
        self.assertEqual(False, self.trip.is_family)

    def test_is_family_where_not_value_and_travelers_more_than_two(self):
        self.is_family = False
        self.assertEqual(True, self.trip.is_family)

    def test_book_a_trip_where_destination_invalid(self):
        result = self.trip.book_a_trip("France")
        self.assertEqual('This destination is not in our offers, please choose a new one!', result)

    def test_book_a_trip_where_dest_valid_not_enough_budget_not_family(self):
        self.trip.budget = 4999
        self.trip.is_family = False
        result = self.trip.book_a_trip("Bulgaria")

        self.assertEqual('Your budget is not enough!', result)

    def test_book_a_trip_where_dest_valid_not_enough_budget_family(self):
        self.trip.budget = 4499
        result = self.trip.book_a_trip("Bulgaria")

        self.assertEqual('Your budget is not enough!', result)

    def test_book_a_trip_where_dest_valid_enough_budget_not_family(self):
        self.trip.is_family = False
        self.trip.budget = 75_000
        result = self.trip.book_a_trip("New Zealand")

        self.assertEqual(f'Successfully booked destination New Zealand! Your budget left is 0.00', result)

    def test_book_a_trip_where_dest_valid_enough_budget_family(self):
        self.trip.budget = 67_500
        result = self.trip.book_a_trip("New Zealand")

        self.assertEqual(f'Successfully booked destination New Zealand! Your budget left is 0.00', result)
        self.assertEqual({"New Zealand": 67_500.0}, self.trip.booked_destinations_paid_amounts)

    def test_booking_status_where_no_destinations(self):
        result = self.trip.booking_status()

        self.assertEqual(f'No bookings yet. Budget: {self.trip.budget:.2f}', result)

    def test_booking_status_where_two_destinations(self):
        dest_dict = {"New Zealand": 75_000.0, "Bulgaria": 5000.0}
        self.trip.is_family = False
        self.trip.book_a_trip("New Zealand")
        self.trip.book_a_trip("Bulgaria")

        self.assertEqual(dest_dict, self.trip.booked_destinations_paid_amounts)

        result = self.trip.booking_status()
        expected_result = (f"Booked Destination: Bulgaria\n"
                           f"Paid Amount: 5000.00\n"
                           f"Booked Destination: New Zealand\n"
                           f"Paid Amount: 75000.00\n"
                           f"Number of Travelers: 10\n"
                           f"Budget Left: 20000.00")

        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    main()
