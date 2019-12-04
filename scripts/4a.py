from input_manager import get_input_data
data = tuple(map(int, get_input_data(4).rstrip().split("-")))

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

print(len(passwords))