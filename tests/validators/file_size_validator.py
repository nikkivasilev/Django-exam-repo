from unittest import TestCase

from magazinslunce.common.validators import validate_file_size


class FileSizeValidator(TestCase):
    SIZE_LIMIT = 5 * 1024 * 1024

    def test_file_size_validator_when_size_correct(self):
        validate_file_size(self.SIZE_LIMIT - 20)

    def test_file_size_validator_when_size_exact_limit(self):
        validate_file_size(self.SIZE_LIMIT)

    def test_file_size_validator_when_size_incorrect(self):
        with self.assertRaises(Exception) as context:
            validate_file_size(self.SIZE_LIMIT + 20)

        self.assertIsNotNone(context.exception)
