# Take equation as string input and convert to 2 lists of terms

def split_equation_terms(equation_string):
    equation_variable = ''
    for char in equation_string:
        if char.isalpha():
            if equation_variable == '' or equation_variable == char:
                equation_variable = char
            else:
                return 'Can not solve equation because there are multiple different variables'
    if equation_variable == '':
        return 'Can not solve equation because there is no variable'
    
    equation_string = equation_string.replace(equation_variable, 'x')
    
    equation_string = equation_string.replace('-', '+-')

    halved_equation = equation_string.split('=')
    left_side = halved_equation[0]
    right_side = halved_equation[1]
    
    left_side = left_side.split('+')
    try:
        left_side.remove('')
    except:
        pass
        
    right_side = right_side.split('+')
    try:
        right_side.remove('')
    except:
        pass
    
    return left_side, right_side