def derive_expression(expression):
    def derivative(term):
        term = term.strip()
        if 'x' not in term:
            return '0'
        if term == 'x':
            return '1'
        if term == '-x':
            return '-1'
        if "x^" in term:
            coeff, exp = term.split('x^')
            coeff = coeff if coeff else '1'
            coeff = coeff.replace('+', '')  # removing '+' if present
            coeff = -1 if coeff == '-' else int(coeff)  # converting to int
            exp = int(exp)
            new_coeff = coeff * exp
            new_exp = exp - 1
            if new_exp == 1:
                return f"{new_coeff}x"
            elif new_exp == 0:
                return str(new_coeff)
            else:
                return f"{new_coeff}x^{new_exp}"
        else:  # handling linear terms
            coeff = term.replace('x', '')
            coeff = 1 if coeff == '' else int(coeff)
            coeff = -1 if coeff == '-' else coeff
            return str(coeff)
        
    def split_terms(expression):
        # Properly split the expression into terms, handling both positive and negative signs
        terms = []
        current_term = ''
        i = 0
        while i < len(expression):
            char = expression[i]
            if char in ['+', '-'] and (i == 0 or expression[i - 1] not in ['+', '-']):
                if current_term:
                    terms.append(current_term)
                current_term = char
            else:
                current_term += char
            i += 1
        if current_term:
            terms.append(current_term)
        return terms
    
    def polynomial_derivation(expression):
        terms = split_terms(expression.replace(" ", ""))

        derived_terms = []
        for term in terms:
            if term in ['+', '-']:
                continue
            if term[0] == '-':
                derived_terms.append('-' + derivative(term[1:]))
            else:
                derived_terms.append('+' + derivative(term) if derived_terms else derivative(term))
        
        # Combine derived terms into a final result, cleaning up extra '+-' or '--'
        derivative_expression = ''.join(derived_terms)
        derivative_expression = derivative_expression.replace("+-", "-").replace("--", "+")
        if derivative_expression[0] == '+':
            derivative_expression = derivative_expression[1:]

        return derivative_expression
    
    def trigonometric_derivation(expression):
        # Dictionary with trigonometric functions and their derivatives
        trig_derivatives = {
            'sinx': 'cosx',
            'sin(x)': 'cos(x)',
            'cosx': '-sinx',
            'cos(x)': '-sin(x)',
            'tanx': 'sec^2(x)',
            'tan(x)': 'sec^2(x)',
            'cscx': '-cscxcotx',
            'csc(x)': '-csc(x)cot(x)',
            'secx': 'secx * tanx',
            'sec(x)': 'sec(x)tan(x)',
            'cotx': '-csc^2(x)',
            'cot(x)': '-csc^2(x)',
            '-sinx': '-cosx',
            '-sin(x)': '-cos(x)',
            '-cosx': 'sinx',
            '-cos(x)': 'sin(x)',
        }
        
        found_func = None

        for key in trig_derivatives:
            if key in expression:
                found_func = key
                break    
        if found_func is not None:
            # Find the prefix
            position = expression.find(found_func)
            prefix = expression[:position]
            derivative = trig_derivatives[found_func]

            if prefix == '':
                adjusted_derivative = derivative 
            else:
                prefix = int(prefix)  

                if derivative.startswith('-'):
                    adjusted_derivative = f'{-prefix}{derivative[1:]}'                
                else:
                    adjusted_derivative = f'{prefix}{derivative}'
            
            return adjusted_derivative
        return None

    # Check if the expression contains trigonometric functions
    trig_result = trigonometric_derivation(expression)
    if trig_result:
        return trig_result
    
    # Otherwise, assume it's a polynomial expression
    return polynomial_derivation(expression)

# Example usage
expression = input("Enter an equation: ")
print(derive_expression(expression))
