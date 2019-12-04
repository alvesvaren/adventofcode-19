from input_manager import get_input_data
import re
data = tuple(map(int, get_input_data(4).rstrip().split("-")))

# correct = 1196
passwords = set()
for password in range(*data):
    password = str(password)
    has_double=False
    does_not_decrease=True
    for i in range(len(password)-1):
        if password[i] == password[i+1]:
            has_double = True
        if password[i] > password[i+1]:
            does_not_decrease = False
        
    if has_double and does_not_decrease:
        passwords.add(password)

double_filtered_passwords = set()
for password in passwords:
    lens = {}
    for i in range(len(password)-1):
        if password[i] == password[i+1]:
            if password[i] in lens:
                lens[password[i]] +=  1
                
            else:
                lens[password[i]] = 2
    if (2 in lens.values()):
        double_filtered_passwords.add(password)

print(len(double_filtered_passwords))