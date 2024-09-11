import requests
import hashlib
import sys
def request_api_data(query_char):
    url='https://api.pwnedpasswords.com/range/'+query_char
    res= requests.get(url)
    if res.status_code!= 200:
        raise RuntimeError(f'check the api and try again: error {res.status_code}')
    return res
def get_password_leaks_response(hashes, hash_to_check):
    hashes=(line.split(':') for line in hashes.text.splitlines())
    for h, count  in hashes:
        #print(h, count) this  generates the whole list of hashes with the first 5 letters same with the count
        #of how many times the password has been breached
        if h==hash_to_check:
            return count
    return 0

def pwned_api_check(password):
    sha1password= hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail=sha1password[:5],sha1password[5:]
    response= request_api_data(first5_char)#requesting the first 5 characters from the api
    print(response)
    return get_password_leaks_response(response,tail)
pwned_api_check('123')

def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password } was  found {count} times you should think of changing the password ')
        else:
            print(f"{password}was not found. carry on ")

    return 'done'
main(sys.argv[1:])
