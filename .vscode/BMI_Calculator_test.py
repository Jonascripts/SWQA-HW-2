# Test file containing tests for the functiosn within BMI_Calculator.py

import BMI_Calculator   # The code to test
import unittest         # The test framework


class Test_TestCheckHeightFt(unittest.TestCase):

    # Perform three tests of positive integers of varying size; all should be accepted (return 1)
    def test_posInt1(self):
        self.assertEqual(BMI_Calculator.CheckHeightFt("3"), 1)

    def test_posInt2(self):
        self.assertEqual(BMI_Calculator.CheckHeightFt("5"), 1)

    def test_posInt3(self):
        self.assertEqual(BMI_Calculator.CheckHeightFt("35"), 1)


    # Perform two tests of negative integers of different size; both should be rejected (return 0)
    def test_negInt1(self):
        self.assertEqual(BMI_Calculator.CheckHeightFt("-5"), 0)

    def test_negInt2(self):
        self.assertEqual(BMI_Calculator.CheckHeightFt("-12"), 0)


    # Perform one test on integer zero; should be accepted (return 1)
    def test_zeroInt(self):
        self.assertEqual(BMI_Calculator.CheckHeightFt("0"), 1)


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


class Test_TestCheckHeightIn(unittest.TestCase):

    # Perform four tests of positive integers of varying size; all no greater than 11 should be accepted (return 1)
    def test_posInt1(self):
        self.assertEqual(BMI_Calculator.CheckHeightIn("5"), 1)

    def test_posInt2(self):
        self.assertEqual(BMI_Calculator.CheckHeightIn("11"), 1)

    def test_posInt3(self):
        self.assertEqual(BMI_Calculator.CheckHeightIn("12"), 0)

    def test_posInt4(self):
        self.assertEqual(BMI_Calculator.CheckHeightIn("35"), 0)


    # Perform three tests of negative integers of different size; both should be rejected (return 0)
    def test_negInt1(self):
        self.assertEqual(BMI_Calculator.CheckHeightIn("-5"), 0)

    def test_negInt2(self):
        self.assertEqual(BMI_Calculator.CheckHeightIn("-12"), 0)

    def test_negInt3(self):
        self.assertEqual(BMI_Calculator.CheckHeightIn("-35"), 0)


    # Perform one test on integer zero; should be accepted (return 1)
    def test_zeroInt(self):
        self.assertEqual(BMI_Calculator.CheckHeightIn("0"), 1)


    # Perform five tests on non-integer values; all should be rejected (return 0)
    def test_nonInt1(self):
        self.assertEqual(BMI_Calculator.CheckHeightIn("five"), 0)

    def test_nonInt2(self):
        self.assertEqual(BMI_Calculator.CheckHeightIn("3and5"), 0)

    def test_nonInt3(self):
        self.assertEqual(BMI_Calculator.CheckHeightIn(";.#&"), 0)

    def test_nonInt4(self):
        self.assertEqual(BMI_Calculator.CheckHeightIn("5."), 0)

    def test_nonInt5(self):
        self.assertEqual(BMI_Calculator.CheckHeightIn ("-twelve"), 0)


class Test_TestCheckWeight(unittest.TestCase):

    # Perform six tests of positive integers of varying size; all should be accepted (return 1)
    def test_posInt1(self):
        self.assertEqual(BMI_Calculator.CheckWeight("3"), 1)

    def test_posInt2(self):
        self.assertEqual(BMI_Calculator.CheckWeight("5"), 1)

    def test_posInt3(self):
        self.assertEqual(BMI_Calculator.CheckWeight("35"), 1)

    def test_posInt4(self):
        self.assertEqual(BMI_Calculator.CheckWeight("155"), 1)

    def test_posInt5(self):
        self.assertEqual(BMI_Calculator.CheckWeight("287"), 1)

    def test_posInt6(self):
        self.assertEqual(BMI_Calculator.CheckWeight("9001"), 1)


    # Perform four tests of negative integers of different size; both should be rejected (return 0)
    def test_negInt1(self):
        self.assertEqual(BMI_Calculator.CheckWeight("-5"), 0)

    def test_negInt2(self):
        self.assertEqual(BMI_Calculator.CheckWeight("-12"), 0)

    def test_negInt3(self):
        self.assertEqual(BMI_Calculator.CheckWeight("-600"), 0)

    def test_negInt4(self):
        self.assertEqual(BMI_Calculator.CheckWeight("-9001"), 0)


    # Perform one test on integer zero; should be accepted (return 1)
    def test_zeroInt(self):
        self.assertEqual(BMI_Calculator.CheckWeight("0"), 1)


    # Perform six tests on non-integer values; all should be rejected (return 0)
    def test_nonInt1(self):
        self.assertEqual(BMI_Calculator.CheckWeight("five"), 0)

    def test_nonInt2(self):
        self.assertEqual(BMI_Calculator.CheckWeight("3and5"), 0)

    def test_nonInt3(self):
        self.assertEqual(BMI_Calculator.CheckWeight(";.#&"), 0)

    def test_nonInt4(self):
        self.assertEqual(BMI_Calculator.CheckWeight("5."), 0)

    def test_nonInt5(self):
        self.assertEqual(BMI_Calculator.CheckWeight("-eight"), 0)

    def test_nonInt6(self):
        self.assertEqual(BMI_Calculator.CheckWeight("over9000"), 0)


class Test_TestCalculateBMI(unittest.TestCase):

    # Perform five tests with different input values (all inputs can be assumed valid); all should be accepted (return 1)
    def test_calcBMI1(self):
        self.assertEqual(BMI_Calculator.CheckWeight(5, 0, 150), 30.0)

    def test_calcBMI2(self):
        self.assertEqual(BMI_Calculator.CheckWeight(4, 10, 125), 26.8)

    def test_calcBMI3(self):
        self.assertEqual(BMI_Calculator.CheckWeight(0, 1, 1), 720)

    def test_calcBMI4(self):
        self.assertEqual(BMI_Calculator.CheckWeight(6, 1, 1400), 189.2)

    def test_calcBMI5(self):
        self.assertEqual(BMI_Calculator.CheckWeight(100, 4, 10000), 5.0)


if __name__ == '__main__':
    unittest.main()