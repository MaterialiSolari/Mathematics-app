import math

trig_derivatives = {
        'sinx': 'cos(x)',
        'sin(x)': 'cos(x)',
        'cosx': '-sin(x)',
        'cos(x)': '-sin(x)',
        'tanx': 'sec^2(x)',
        'tan(x)': 'sec^2(x)',
        'cscx': '-csc(x)cot(x)',
        'csc(x)': '-csc(x)cot(x)',
        'secx': 'sec(x)tan(x)',
        'sec(x)': f'sec(x)tan(x)',
        'cotx': '-csc^2(x)',
        'cot(x)': '-csc^2(x)',
        '-sinx': '-cos(x)',
        '-sin(x)': '-cos(x)',
        '-cosx': 'sin(x)',
        '-cos(x)': 'sin(x)',
    }
    
trig = {
        'sin': 'cos',
        'cos': '-sin',
        'tan': 'sec^2',
        'cot': '-csc^2',
        '-sin': '-cos',
        '-cos': 'sin',
        '-tan': '-sec^2'
    }
    
user_input = input("Enter an equation: ")


found_func = None

for key in trig:
    if key in user_input:
        found_func = key
        break

equation = user_input
position = user_input.find(found_func)
prefix = user_input[:position]  # Extracting the prefix
user_input = user_input[position:] 
digit = ''
derivative = trig[found_func]
for char in user_input:
    if char.isdigit():
        digit += char
        print(digit)
       


print("Prefix:", prefix)
print("Updated User Input:", user_input)
print('digit: ', digit)
print('trig:', found_func)



if derivative.startswith('-'):
    product = f'{-int(prefix) * int(digit)}{derivative}({digit}x)'
    print(product)
elif digit not in equation and derivative.startswith('-'):
    product = f'{-prefix}{trig_derivatives[found_func]}'
    print(product)

else:
    product = f'{int(prefix) * int(digit)}{derivative}({digit}x)'
    print(product)
