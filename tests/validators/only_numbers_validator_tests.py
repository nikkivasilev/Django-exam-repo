from unittest import TestCase

from magazinslunce.common.validators import validate_only_numbers


class OnlyNumbersValidator(TestCase):

    def test_only_nums_validator_when_given_data_valid(self):
        validate_only_numbers('12345')

    def test_only_nums_validator_when_given_data_is_none(self):
        validate_only_numbers('')

    def test_only_nums_validator_when_given_data_contains_letters_expect_error(self):
        with self.assertRaises(Exception) as context:
            validate_only_numbers('abcde1234abcd')

        self.assertIsNotNone(context.exception)

    def test_only_nums_validator_when_given_data_contains_special_characters_expect_error(self):
        with self.assertRaises(Exception) as context:
            validate_only_numbers('1234@#$%5678')

        self.assertIsNotNone(context.exception)
