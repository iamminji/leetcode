from unittest import TestCase, main
from Coin_Change_2 import Solution


class LeetCodeTest(TestCase):
    def setUp(self):
        self.answer = Solution()

    def test_change(self):
        self.assertEqual(self.answer.change(5, [1, 2, 5]), 4)
        self.assertEqual(self.answer.change(10, [1, 2, 5]), 10)


if __name__ == "__main__":
    main()
