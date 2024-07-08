trig_derivatives = {
        'sin': 'cos',
        'cos': '-sin',
        'tan': 'sec^2',
        'cot': '-csc^2',
        '-sin': '-cos',
        '-cos': 'sin',
        '-tan': '-sec^2'
    }
user_input = input("Enter a term with a trigonometric function (e.g., '3sinx', '-cos(x)'): ")

found_func = None

for key in trig_derivatives:
    if key in user_input:
        found_func = key
        break
position = user_input.find(found_func)
prefix = user_input[:position]
dev = trig_derivatives[found_func]
print(dev)

