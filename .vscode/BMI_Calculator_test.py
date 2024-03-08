# Test file containing tests for the functiosn within BMI_Calculator.py

import BMI_Calculator   # The code to test
import unittest         # The test framework


class Test_TestCheckHeightFt(unittest.TestCase):

    # Perform three tests of positive integers of varying size; all should be accepted (return 1)
    def test_posInt1(self):
        self.assertEqual(BMI_Calculator.CheckHeightFt(3), 1)

    def test_posInt2(self):
        self.assertEqual(BMI_Calculator.CheckHeightFt(5), 1)

    def test_posInt3(self):
        self.assertEqual(BMI_Calculator.CheckHeightFt(35), 1)


    # Perform two tests of negative integers of different size; both should be rejected (return 0)
    def test_negInt1(self):
        self.assertEqual(BMI_Calculator.CheckHeightFt(-5), 0)

    def test_negInt2(self):
        self.assertEqual(BMI_Calculator.CheckHeightFt(-12), 0)


    # Perform one test on integer zero; should be accepted (return 1)
    def test_zeroInt(self):
        self.assertEqual(BMI_Calculator.CheckHeightFt(0), 1)


    # Perform five tests on non-integer values; all should be rejected (return 0)
    def test_nonInt1(self):
        self.assertEqual(BMI_Calculator.CheckHeightFt("five"), 0)

    def test_nonInt2(self):
        self.assertEqual(BMI_Calculator.CheckHeightFt("3and5"), 0)

    def test_nonInt3(self):
        self.assertEqual(BMI_Calculator.CheckHeightFt(";.#&"), 0)

    def test_nonInt4(self):
        self.assertEqual(BMI_Calculator.CheckHeightFt("5."), 0)

    def test_nonInt5(self):
        self.assertEqual(BMI_Calculator.CheckHeightFt("-eight"), 0)


if __name__ == '__main__':
    unittest.main()