def validate_equation(equation_string):
    '''Ensures the inputted equation follows the format guidlines'''
    
    # Check for illegal characters
    for char in equation_string:
        if char.isalpha() or char.isnumeric() or char in ['+', '-', '*', '/', '.', '=']:
            pass
        else:
            return False
    
    # Make sure only 1 variable exists
    equation_variable = ''
    for char in equation_string:
        if char.isalpha():
            if equation_variable == '' or equation_variable == char:
                equation_variable = char
            else:
                return False
    
    # Make sure there is exactly 1 equals sign
    if not equation_string.count('=') == 1:
        return False
    
    return True

def split_equation_terms(equation_string):
    '''Converts an equation string into two strings (left and right side).'''
    
    # Make sure only 1 variable exists
    equation_variable = ''
    for char in equation_string:
        if char.isalpha():
            if equation_variable == '' or equation_variable == char:
                equation_variable = char
            else:
                raise Exception('Too many variables (more than 1)')
    
    # Set all instances of the variable to 'x' for simplicity
    equation_string = equation_string.replace(equation_variable, 'x')
    
    # Replace all instances of - to +- for simplicity
    equation_string = equation_string.replace('-', '+-')
    

    # Split the equation in two
    halved_equation = equation_string.split('=')
    left_side = halved_equation[0]
    right_side = halved_equation[1]
    
    
    # Split each half into terms using the + sign
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
    
    # Return the two sides of the equation
    return left_side, right_side