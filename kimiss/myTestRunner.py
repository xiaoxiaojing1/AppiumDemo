import unittestLogin
import unittest

#mysuite = unittest.TestSuite()
#mysuite.addTest(unittestLogin.MyTestCase("test_login"))
#mysuite.addTest(unittestLogin.MyTestCase("test_login"))
case1 = unittest.TestLoader().loadTestsFromTestCase(unittestLogin.MyTestCase)
mysuite = unittest.TestSuite([case1])
#mysuite.addTest(unittestLogin.MyTestCase("test_login"))

myrunner = unittest.TextTestRunner(verbosity=2)
myrunner.run(mysuite)

