import unittest

from nhs import validate


class test_validation(unittest.TestCase):

	def test_valid_numbers(self):
		"""
			Test to ensure validation works on a range of valid formats
		"""
		l = ['999 999 9468', '999-999-9484', ' 999 999 9514 ', '9999999565']
		for i in l:
			try:
				response = validate(i)
				self.assertTrue(response)
			except ValueError:
				self.fail('None of these tests should fail.')

	def test_validation_short(self):
		"""
			Tests to ensure validation works on short numbers
		"""
		l = '0123456'
		self.assertRaises(ValueError, validate, l)

	def test_validation_long(self):
		"""
			Tests to ensure validation works on long numbers
		"""
		l = '0101010101010'
		self.assertRaises(ValueError, validate, l)

	def test_validation_extra_chars(self):
		"""
			Tests to ensure the method can accept NHS numbers with
			hyphens or spaces.
		"""
		l = '012-012-0321'
		validate(l)
		self.assertTrue(True)

	def test_validation_alpha(self):
		"""
			Test to ensure validation fails on alpha characters
		"""
		l = '123456789a'
		self.assertRaises(ValueError, validate, l)

	def test_validation_checksum_digit(self):
		"""
			Test to ensure validation fails if checksum character is wrong and passes if it is correct
		"""
		base_num = '123-987-456'
		correct_check_digit = 1
		for last_digit in range(10):
			l = base_num + str(last_digit)
			response = validate(l)
			if last_digit != correct_check_digit:
				self.assertFalse(response)
			else:
				self.assertTrue(response)

	def test_validation_checksum_ten_fails(self):
		"""
		Test to ensure that validation fails if the checksum works out to be 10.
		This is actually an inevitable consequence of the way that the checksum is compared because if the
		checksum is '10' then it cannot possibly match the single digit last character
		"""
		checksum_is_ten = '1239874570'
		response = validate(checksum_is_ten)
		self.assertFalse(response)


if __name__ == '__main__':
	unittest.main()
