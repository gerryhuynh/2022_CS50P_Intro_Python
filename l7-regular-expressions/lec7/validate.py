import re

email = input("What's your email? ").strip()

if re.search("^\w+@\w+\.edu$", email):
  print("Valid")
else:
  print("Invalid")