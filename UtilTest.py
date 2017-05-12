from Utils import *
import unittest


class TestUtils(unittest.TestCase):

    def test_extract_email(self):
        email1 = "abc@gmail.com"
        email2 = "abc@126.com"

        test1 = (email1, [email1])
        test2 = (email1+" "+email2, [email1, email2])
        test3 = ("", [])

        tests = [test1, test2, test3]

        for test in tests:
            ret = extract_email(test[0])
            print ret,test[1]
            assert len(ret) == len(test[1])
            for i, r in enumerate(ret):
                assert r == test[1][i]

if __name__ == '__main__':
    unittest.main()

