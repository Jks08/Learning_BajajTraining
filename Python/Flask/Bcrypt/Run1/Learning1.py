from flask_bcrypt import Bcrypt
from werkzeug.security import generate_password_hash, check_password_hash

# bcrypt = Bcrypt() #Creates Hash function to encrypt passwords

# hashed_parse = bcrypt.generate_password_hash('mypasword')
# print(hashed_parse)

# check1 = bcrypt.check_password_hash(hashed_parse, 'mypass')
# print(check1)

# check2 = bcrypt.check_password_hash(hashed_parse, 'mypasword')
# print(check2)

# check_3 = bcrypt.check_password_hash(hashed_parse, 'mepassword')
# print(check_3)

hashed_parse = generate_password_hash('mypasword')
print(hashed_parse)

check1 = check_password_hash(hashed_parse, 'wrong_pass')
print(check1)

check2 = check_password_hash(hashed_parse, 'mypasword')
print(check2)
