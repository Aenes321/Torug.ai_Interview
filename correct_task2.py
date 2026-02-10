# Write your corrected implementation for Task 2 here.
# Do not modify `task2.py`.
import string
letter_digits = set(string.ascii_letters + string.digits)
valid_char_local = letter_digits.union({'.','!','#','$','%','&','*','+','-','/','=','?','^','_','`','{','|','}','~',"'"}) 
valid_char_domain = letter_digits.union({'-','.'})
def is_valid(email):
    
    if(email.count("@") != 1):
        return False
    
    index = email.find("@")
    if(index == 0 or index == len(email)-1):
        return False
    
    local = email[:index]
    domain = email[index+1:]
    if(local[0] == '.' or local[-1] == '.'):
        return False
    if not set(local).issubset(valid_char_local):
        return False
    if not set(domain).issubset(valid_char_domain):
        return False
    if(len(local) > 64 or len(domain) > 255):
        return False
    if(domain[0] == '-' or domain[0] == '.' or domain[-1] == '-' or domain[-1] == '.'):
        return False
    if(".." in email):
        return False
    
    return True

def count_valid_emails(emails):
    count = 0
    for email in emails:
        if is_valid(email) :
            count += 1

    return count
