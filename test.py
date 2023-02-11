from main import RentalProperty, RentalCalc
import unittest

class TestRentalProperty(unittest.TestCase):
    def test_property_dict(self):
        self.rental = RentalProperty('123 Legacy Dr', 'Plano', 'Texas', 450000)
        self.assertEqual(self.rental.street_address, '123 Legacy Dr')
        self.assertEqual(self.rental.city, 'Plano')
        self.assertEqual(self.rental.state, 'Texas')
        self.assertEqual(self.rental.purchase_price, 450000)

class TestRentalCalc(unittest.TestCase):
    def test_income_from_property(self):
        self.rental_calc = RentalCalc()
        self.rental_calc.income_from_property(2000, 0, 0, 0)
        self.assertEqual(self.rental_calc.rent, 2000)
        self.assertEqual(self.rental_calc.income, 2000)

    def test_property_expenses(self):
        self.rental_calc = RentalCalc()
        self.rental_calc.rent = 2000
        self.rental_calc.vacancy = 100
        self.rental_calc.repairs = 200
        self.rental_calc.property_manage = 200
        self.rental_calc.property_expenses(150, 100, 0, 0, 0, 860, 0 )
        self.assertEqual(self.rental_calc.expenses, 1610)

    def test_property_cash_flow(self):
        self.rental_calc = RentalCalc()
        self.rental_calc.income_from_property(2000, 0, 0, 0)
        self.rental_calc.rent = 2000
        self.rental_calc.vacancy = 100
        self.rental_calc.repairs = 200
        self.rental_calc.property_manage = 200
        self.rental_calc.property_expenses(150, 100, 0, 0, 0, 860, 0 )
        self.rental_calc.property_cash_flow()
        self.assertEqual(self.rental_calc.cash_flow, 390)

    def test_cash_on_cash(self):
        self.rental_calc = RentalCalc()
        self.rental_calc.income_from_property(2000, 0, 0, 0)
        self.rental_calc.rent = 2000
        self.rental_calc.vacancy = 100
        self.rental_calc.repairs = 200
        self.rental_calc.property_manage = 200
        self.rental_calc.property_expenses(150, 100, 0, 0, 0, 860, 0 )
        self.rental_calc.property_cash_flow()
        self.rental_calc.cash_on_cash(40000, 3000, 7000, 0)
        self.assertAlmostEqual(self.rental_calc.roi, 9.36, 2)

unittest.main()