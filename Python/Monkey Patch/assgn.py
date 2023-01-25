import warnings
warnings.filterwarnings('ignore')

# List methods: insert, extend, find.

# import unittest
# from assgnTestFile import emp

# class TestListMethods(unittest.TestCase):
#     def test_insert_at_beginning(self):                   # Test 1 - Insert at beginning
#         l = [1, 2, 3, 4, 5]
#         l.insert(0, 0)
#         self.assertEqual(l, [0, 1, 2, 3, 4, 5])           
#     def test_insert_at_middle(self):                    # Test 2 - Insert at middle
#         l = [1, 2, 3, 4, 5]
#         l.insert(len(l)//2, 14)
#         self.assertEqual(l, [1, 2, 14, 3, 4, 5])        
#     def test_insert_at_end(self):                       # Test 3 - Insert at end
#         l = [1, 2, 3, 4, 5]
#         l.insert(len(l), 100)
#         self.assertEqual(l, [1, 2, 3, 4, 5, 100])
#     def test_extend(self):                              # Test 4 - Extend
#         l = [1, 2, 3]
#         l.extend([4, 5, 6])
#         self.assertEqual(l, [1, 2, 3, 4, 5, 6])
#     def test_find_at_beginning(self):                # Test 5 - Find at beginning       
#         l = [1, 2, 3]
#         self.assertEqual(l.index(1), 0)
#     def test_find_at_middle(self):                  # Test 6 - Find at middle
#         l = [1, 2, 3]
#         self.assertEqual(l.index(2), 1)
#     def test_find_at_end(self):                 # Test 7 - Find at end
#         l = [1, 2, 3]
#         self.assertEqual(l.index(3), 2)


# # Create a class emp with attributes id,name,salary. Bonus function increments the salary by 10%. Do unit testing for the same.

# class TestEmp(unittest.TestCase):
#     def test_bonus(self):                      # Test 8 - Bonus
#         e = emp(1, 'abc', 1000)
#         e.bonus_to_give(0.35)
#         self.assertEqual(e.gross_salary(), f"Gross Salary after Bonus of {str(e.bonus_to_give(0.35))} is: {e.bonus_to_give(0.35) * e.salary + e.salary}")

# if __name__ == '__main__':
#     unittest.main()


# Get output of unit test cases in a html file.

import unittest

import unittest

from html_test_runner import HTMLTestRunner
from assgnTestFile import emp

class TestListMethods(unittest.TestCase):
    def test_insert_at_beginning(self):                   # Test 1 - Insert at beginning
        l = [1, 2, 3, 4, 5]
        l.insert(0, 0)
        self.assertEqual(l, [0, 1, 2, 3, 4, 5])           
    def test_insert_at_middle(self):                    # Test 2 - Insert at middle
        l = [1, 2, 3, 4, 5]
        l.insert(len(l)//2, 14)
        self.assertEqual(l, [1, 2, 14, 3, 4, 5])        
    def test_insert_at_end(self):                       # Test 3 - Insert at end
        l = [1, 2, 3, 4, 5]
        l.insert(len(l), 100)
        self.assertEqual(l, [1, 2, 3, 4, 5, 100])
    def test_extend(self):                              # Test 4 - Extend
        l = [1, 2, 3]
        l.extend([4, 5, 6])
        self.assertEqual(l, [1, 2, 3, 4, 5, 6])
    def test_find_at_beginning(self):                # Test 5 - Find at beginning       
        l = [1, 2, 3]
        self.assertEqual(l.index(1), 0)
    def test_find_at_middle(self):                  # Test 6 - Find at middle
        l = [1, 2, 3]
        self.assertEqual(l.index(2), 1)
    def test_find_at_end(self):                 # Test 7 - Find at end
        l = [1, 2, 3]
        self.assertEqual(l.index(3), 2)


# Create a class emp with attributes id,name,salary. Bonus function increments the salary by 10%. Do unit testing for the same.

class TestEmp(unittest.TestCase):
    def test_bonus(self):                      # Test 8 - Bonus
        e = emp(1, 'abc', 1000)
        e.bonus_to_give(0.35)
        self.assertEqual(e.gross_salary(), f"Gross Salary after Bonus of {str(e.bonus_to_give(0.35))} is: {e.bonus_to_give(0.35) * e.salary + e.salary}")

# if __name__ == '__main__':
#     with open('testReport.html', 'w') as f:
#         runner = HTMLTestRunner(stream=f, title='Test Report', description='Unit Testing')
#         unittest.main(testRunner=runner)

# Now download this html page as a pdf and mail it to the specific mail id.

import os
import smtplib
import imghdr
from email.message import EmailMessage

EMAIL_ADDRESS = 'mobydiaz.instabiz@gmail.com'
EMAIL_PASSWORD = 'Library@31'

msg = EmailMessage()
msg['Subject'] = 'Test Report'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'srivastavajishnu.31@gmail.com'
msg.set_content('Test Report')

with open('testReport.html', 'rb') as f:
    file_data = f.read()
    file_type = imghdr.what(f.name)
    file_name = f.name

msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

# with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
#     smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
#     smtp.send_message(msg)
# try:
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
#     server.send_message(msg)
#     print('Email sent successfully')
# except Exception as e:
#     print(e)
#     print('Email not sent')