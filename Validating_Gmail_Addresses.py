import re
def is_valid_gmail(mail):
   pattern = r'^[a-z A-Z 0-9_]+@gmai.com$'
   return re.match(pattern,match) is not None
   maiil=input("enter your mail = ")

   if is_valid_gmail(mail):
      print("valid")
   else
      print("Not valid")
