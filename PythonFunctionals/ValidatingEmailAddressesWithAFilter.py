'''
Created on 15 de dez de 2017

@author: Romulo
'''
def fun(s):
        emailDiv = s.replace('@', " ", 1).replace(".", " ", 1).split()
        if(len(emailDiv) != 3): return False
        if(len(list(filter(lambda letra: letra.isdigit()
                                         or letra.isalpha()
                                         or letra == "-" 
                                         or letra == "_", list(emailDiv[0])))) != len(emailDiv[0])):  # emailDiv0 = string before "@"
            return False
        if(len(list(filter(lambda letra: letra.isdigit() 
                                         or letra.isalpha(), list(emailDiv[1])))) != len(emailDiv[1])):  # emailDiv[1] is a string 
                                                                                                        # after '@' and before the
                                                                                                        # "."
            return False
        if(len(emailDiv[2]) > 3):
            return False
        return True
    
def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':  # main
    n = int(input())
    emails = [] #
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
