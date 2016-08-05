import unittest
import os
from random import randint
from chapters import ch1


class MyChi1TestCase(unittest.TestCase) :
    def test_to_str(self) :
        test_bytes = '\x00' + ''.join(chr(randint(0,255)) for _ in range(10)) + '\x00'
        print(test_bytes)
        test_str = "This is a test string."
        result_str = ch1.to_str(test_str)
        result_bytes = ch1.to_str(test_bytes)
        print('result_str: ' + result_str)
        print('result_bytes: ' + result_bytes)



if __name__ == '__main__' :
    unittest.main()
