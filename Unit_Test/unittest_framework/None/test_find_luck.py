# this code is in the test_find_luck.py
import unittest
from find_luck import find_luck


class TestFindLuck(unittest.TestCase):

    def test_strings_with_luck(self):
        # checks that find_luck finds 'luck' in all the strings with 'luck'
        strings_with_luck = [
            'luck',
            'hereluckthere',
            'hereluck',
            'luckhere',
            'luck is great but most of life is hard work'
        ]

        # write your test here
        for s in strings_with_luck:
            self.assertIsNotNone(find_luck(s))

    def test_strings_without_luck(self):
        # checks that find_luck returns None when there is no 'luck' in the string
        strings_without_luck = ['here', 'duck', 'four', 'uckl']

        # write your test here
        for s in strings_without_luck:
            self.assertIsNone(find_luck(s))


if __name__ == '__main__':
    unittest.main()
