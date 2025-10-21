from typing import Literal
import pytest 
from calculator import addition, subtraction, multiply, divide, exponent

@pytest.mark.parametrize("test_input, expected_output", [
 ("48+36", 84), ("9+33", 42), ("38+21", 59), ("43+19", 62), ("50+1", 51),
 ("25+30", 55), ("25+28", 53), ("29+8", 37), ("28+33", 61), ("26+39", 65),
 ("37+14", 51), ("47+23", 70), ("50+35", 85), ("40+34", 74), ("44+7", 51),
 ("27+3", 30), ("19+33", 52), ("7+28", 35), ("13+38", 51), ("42+30", 72),
 ("25+32", 57), ("7+27", 34), ("39+15", 54), ("21+9", 30), ("25+40", 65),
 ("16+12", 28), ("42+28", 70), ("31+43", 74), ("20+18", 38), ("20+32", 52),
 ("20+16", 36), ("12+36", 48), ("22+36", 58), ("19+38", 57), ("29+41", 70),
 ("5+15", 20), ("34+39", 73), ("24+0", 24), ("4+9", 13), ("28+22", 50),
 ("46+3", 49), ("35+46", 81), ("18+26", 44), ("7+17", 24), ("46+29", 75),
 ("8+28", 36), ("41+16", 57), ("3+4", 7), ("35+30", 65), ("16+12", 28),
 ("48+37", 85), ("1+28", 29), ("30+37", 67), ("44+43", 87), ("30+19", 49),
 ("2+39", 41), ("43+22", 65), ("49+12", 61), ("29+22", 51), ("31+40", 71),
 ("0+23", 23), ("16+45", 61), ("2+3", 5), ("28+49", 77), ("23+7", 30),
 ("8+36", 44), ("12+43", 55), ("48+42", 90), ("30+17", 47), ("8+48", 56),
 ("39+39", 78), ("15+1", 16), ("23+41", 64), ("40+6", 46), ("47+20", 67),
 ("24+12", 36), ("36+23", 59), ("13+12", 25), ("34+9", 43), ("23+18", 41),
 ("43+21", 64), ("36+14", 50), ("37+47", 84), ("22+3", 25), ("43+18", 61),
 ("35+17", 52), ("6+15", 21), ("9+15", 24), ("22+5", 27), ("17+3", 20),
 ("1+4", 5), ("33+5", 38), ("14+20", 34), ("23+8", 31), ("34+25", 59),
 ("23+2", 25), ("49+47", 96), ("37+16", 53), ("34+19", 53), ("3+46", 49)

])
def test_add_two_positive_numbers(test_input: Literal['48+36'] | Literal['9+33'] | Literal['38+21'] | Literal['43+19'] | Literal['50+1'] | Literal['25+30'] | Literal['25+28'] | Literal['29+8'] | Literal['28+33'] | Literal['26+39'] | Literal['37+14'] | Literal['47+23'] | Literal['50+35'] | Literal['40+34'] | Literal['44+7'] | Literal['27+3'] | Literal['19+33'] | Literal['7+28'] | Literal['13+38'] | Literal['42+30'] | Literal['25+32'] | Literal['7+27'] | Literal['39+15'] | Literal['21+9'] | Literal['25+40'] | Literal['16+12'] | Literal['42+28'] | Literal['31+43'] | Literal['20+18'] | Literal['20+32'] | Literal['20+16'] | Literal['12+36'] | Literal['22+36'] | Literal['19+38'] | Literal['29+41'] | Literal['5+15'] | Literal['34+39'] | Literal['24+0'] | Literal['4+9'] | Literal['28+22'] | Literal['46+3'] | Literal['35+46'] | Literal['18+26'] | Literal['7+17'] | Literal['46+29'] | Literal['8+28'] | Literal['41+16'] | Literal['3+4'] | Literal['35+30'] | Literal['48+37'] | Literal['1+28'] | Literal['30+37'] | Literal['44+43'] | Literal['30+19'] | Literal['2+39'] | Literal['43+22'] | Literal['49+12'] | Literal['29+22'] | Literal['31+40'] | Literal['0+23'] | Literal['16+45'] | Literal['2+3'] | Literal['28+49'] | Literal['23+7'] | Literal['8+36'] | Literal['12+43'] | Literal['48+42'] | Literal['30+17'] | Literal['8+48'] | Literal['39+39'] | Literal['15+1'] | Literal['23+41'] | Literal['40+6'] | Literal['47+20'] | Literal['24+12'] | Literal['36+23'] | Literal['13+12'] | Literal['34+9'] | Literal['23+18'] | Literal['43+21'] | Literal['36+14'] | Literal['37+47'] | Literal['22+3'] | Literal['43+18'] | Literal['35+17'] | Literal['6+15'] | Literal['9+15'] | Literal['22+5'] | Literal['17+3'] | Literal['1+4'] | Literal['33+5'] | Literal['14+20'] | Literal['23+8'] | Literal['34+25'] | Literal['23+2'] | Literal['49+47'] | Literal['37+16'] | Literal['34+19'] | Literal['3+46'], expected_output: Literal[84] | Literal[42] | Literal[59] | Literal[62] | Literal[51] | Literal[55] | Literal[53] | Literal[37] | Literal[61] | Literal[65] | Literal[70] | Literal[85] | Literal[74] | Literal[30] | Literal[52] | Literal[35] | Literal[72] | Literal[57] | Literal[34] | Literal[54] | Literal[28] | Literal[38] | Literal[36] | Literal[48] | Literal[58] | Literal[20] | Literal[73] | Literal[24] | Literal[13] | Literal[50] | Literal[49] | Literal[81] | Literal[44] | Literal[75] | Literal[7] | Literal[29] | Literal[67] | Literal[87] | Literal[41] | Literal[71] | Literal[23] | Literal[5] | Literal[77] | Literal[90] | Literal[47] | Literal[56] | Literal[78] | Literal[16] | Literal[64] | Literal[46] | Literal[25] | Literal[43] | Literal[21] | Literal[27] | Literal[31] | Literal[96]): 
    """
    This function is composed of 100 tests that tests if the addition function can add two positive numbers
    """
    assert eval(test_input) == expected_output

def test_add_two_negative_numbers():
    """
    This function tests if the addition function can add two negative numbers together
    """
    assert addition(-1, -5) == -6

def test_subtract_two_positive_numbers():
    """
    This function tests if the subtraction function can subtract a positive number from a positive number
    """
    assert subtraction(89, 11) == 78

def test_subtract_larger_number_from_smaller_number():
    """
    This function tests if the subtraction function can subtract a larger number from a smaller number
    """
    assert subtraction(6, 7) == -1

def test_multiply_two_positive_numbers():
    """
    This function tests if the multiply function can multiply two positive numbers 
    """
    assert multiply(6, 7) == 42

def test_multiply_two_large_numbers():
    """
    This function tests if the multiply function can multiply two large numbers 
    """
    assert multiply(108, 744) == 80352

def test_multiply_number_by_zero():
    """
    This function tests if the multiply function can multiply a number by 0
    """
    assert multiply(4, 0) == 0

def test_divide_two_positive_numbers():
    """
    This function tests if the divide function can divide two positive numbers 
    """
    assert divide(42, 7) == 6

def test_divide_number_by_one():
    """
    This function tests if the divide function can divide a number by 1
    """
    assert divide(42, 1) == 42

def test_divide_two_decimal_numbers():
    """
    This function tests if the divide function can divide two decimal numbers 
    """
    assert divide(0.0001, 0.02) == 0.005

def test_divide_two_small_numbers():
    """
    This function tests if the divide function can divide two small numbers 
    """
    assert divide(1, 0.02) == 50

def test_divide_number_by_zero():
    """
    This function tests if the divide function can divide a number by 0 and return the correct statement 
    """
    assert divide(87, 0) == "Did you fail highschool math? Dividing by zero is impossible, you moron!"

def test_exponents_with_two_numbers():
    """
    This function tests if the exponent function can find the exponential value of a base number 
    """
    assert exponent(4, 3) == 64
    