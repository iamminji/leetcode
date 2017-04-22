from Largest_Number import Solution
import unittest


class TestCase(unittest.TestCase):
    def setUp(self):
        self.answer = Solution()

    def test_largest_number(self):
        self.assertEqual(self.answer.largestNumber([93, 51, 65, 84, 91, 78, 99, 71, 97, 9]),
                         "9999793918478716551")
        self.assertEqual(self.answer.largestNumber([74, 21, 33, 51, 77, 51, 90, 60, 5, 56]),
                         "9077746056551513321")
        self.assertEqual(self.answer.largestNumber([1, 2, 2, 2]),
                         "2221")
        self.assertEqual(self.answer.largestNumber([3, 30, 34, 5, 9]),
                         "9534330")
        self.assertEqual(self.answer.largestNumber([0, 0]),
                         "0")


if __name__ == "__main__":
    unittest()
