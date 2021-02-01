import requests
import hashlib 
import sys


def pwned_api_check(password):
    url='https://api.pwnedpasswords.com/range/'+password
    response = requests.request("GET", url)
    
    if response.status_code!=200:
        return 'Something is not right !!!'
    return response

def leaked_password_count(response,password):
    password_list=response.text.splitlines()
    matched_list=[i.split(':') for i in password_list]

    for i in matched_list:
        if i[0]==password:
            return i[1]
    return False

def genrate_hash(password):
    #genrating SHA1 HASH 
    result = hashlib.sha1(password.encode()) 
    #Converting the Hash String and then To Upper case 
    result=result.hexdigest().upper()
    return result

def final(password):
    # Genrating Hashes
    hash=genrate_hash(password)
    head,tail=hash[:5],hash[5:]
    response=pwned_api_check(head)
    password_count=leaked_password_count(response,tail)
    if password_count:
        print(f'{password} was found to be hacked {password_count} time. So consider changing it.')
    else:
        print(f'{password} was not found to be hacked you can continue using it...')

# Using Command Line Arguments 
if __name__=='__main__':
    password_list=[i for i in sys.argv]
    if len(password_list)>0:
        for i in range(1,len(password_list)):
            final(password_list[i])                             
    else:
        print('Try to tye password..')