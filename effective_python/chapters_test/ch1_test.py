import unittest
from chapters import ch1


class MyChi1TestCase(unittest.TestCase) :
    def test_to_str(self) :
        test_string = "This is a test string."
        result_string = ch1.to_str(test_string)
        print("testString: " + test_string)
        print("resultString: " + result_string)
        self.assertEqual(self, test_string, ch1.to_str(test_string))


if __name__ == '__main__' :
    unittest.main()
