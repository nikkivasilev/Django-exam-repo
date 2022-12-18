from unittest import TestCase

from magazinslunce.common.validators import validate_file_size


class Objwithsize:
    def __init__(self, size):
        self.size = size


class FileSizeValidator(TestCase):
    SIZE_LIMIT = 5 * 1024 * 1024

    def test_file_size_validator_when_size_correct(self):
        obj = Objwithsize
        obj.size = self.SIZE_LIMIT - 20
        validate_file_size(obj)

    def test_file_size_validator_when_size_exact_limit(self):
        obj = Objwithsize
        obj.size = self.SIZE_LIMIT
        validate_file_size(obj)

    def test_file_size_validator_when_size_incorrect(self):
        obj = Objwithsize
        obj.size = self.SIZE_LIMIT + 20

        with self.assertRaises(Exception) as context:
            validate_file_size(obj.size)

        self.assertIsNotNone(context.exception)
