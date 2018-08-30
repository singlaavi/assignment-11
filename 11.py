#Q.1- Find a Valid Email Address From a Text
import re
email=input('Enter ID')
a=re.fullmatch('^[a-zA-Z][_a-zA-z0-9.]*(@)(gmail.com|yahoo.com)',email)
if a:
    print('VALID')
else:
    print('NOT VALID')
  


#Find a Valid Indian Phone Number From a Text
import re
x=input('Enter Indian Phone number:')

match=re.fullmatch('(\+91-)[6-9][0-9]{9}',x)
if a:
    print('VALID')
else:
    print('NOT VALID')
  
