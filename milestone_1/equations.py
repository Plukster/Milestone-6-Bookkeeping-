
"""
Milestone 1: Back to School - Quadratic Equation Solver
"""

import cmath

def extract_coefficients(equation):
    """
    Extract coefficients from quadratic equation string
    Handles format like: 4x^2 +4x + (-8) = 0
    """
    # Clean the equation
    eq = equation.replace(' ', '').replace('^', '')
    
    # Remove equals sign
    if '=' in eq:
        eq = eq.split('=')[0]
    
    print(f"Processing: {eq}")
    
    # Simple approach - manually parse
    # Split by + and - signs (but be careful with negative signs)
    parts = []
    current = ""
    i = 0
    
    while i < len(eq):
        if eq[i] in '+-' and i > 0:
            if current:
                parts.append(current)
            current = eq[i]
        else:
            current += eq[i]
        i += 1
    
    if current:
        parts.append(current)
    
    print(f"Parts: {parts}")
    
    # Now extract coefficients
    a = b = c = 0
    
    for part in parts:
        if 'x2' in part:
            coeff = part.replace('x2', '')
            if coeff == '' or coeff == '+':
                a = 1
            elif coeff == '-':
                a = -1
            else:
                a = int(coeff)
        elif 'x' in part and 'x2' not in part:
            coeff = part.replace('x', '')
            if coeff == '' or coeff == '+':
                b = 1
            elif coeff == '-':
                b = -1
            else:
                b = int(coeff)
        elif part and part not in ['+', '-']:
            c = int(part)
    
    return a, b, c

def solve_quadratic(a, b, c):
    """
    Solve quadratic equation using the quadratic formula
    """
    print(f"Solving: {a}x² + {b}x + {c} = 0")
    
    # Calculate discriminant
    discriminant = b**2 - 4*a*c
    print(f"Discriminant (b² - 4ac) = {discriminant}")
    
    if discriminant >= 0:
        # Real solutions
        sqrt_discriminant = discriminant**0.5
        x1 = (-b + sqrt_discriminant) / (2*a)
        x2 = (-b - sqrt_discriminant) / (2*a)
        
        print(f"x1 = {x1}")
        print(f"x2 = {x2}")
        
        return x1, x2
    else:
        # Complex solutions
        sqrt_discriminant = cmath.sqrt(discriminant)
        x1 = (-b + sqrt_discriminant) / (2*a)
        x2 = (-b - sqrt_discriminant) / (2*a)
        
        print(f"x1 = {x1}")
        print(f"x2 = {x2}")
        
        return x1, x2

def main():
    """
    Main function to demonstrate the quadratic equation solver
    """
    # Test with your example
    eq = '4x^2 +4x + (-8) = 0'
    
    print("=== Quadratic Equation Solver ===")
    print(f"Input equation: {eq}")
    
    # Extract coefficients
    try:
        a, b, c = extract_coefficients(eq)
        print(f"Extracted coefficients: a={a}, b={b}, c={c}")
        
        # Solve the equation
        print("\nSolving...")
        solutions = solve_quadratic(a, b, c)
        
        print(f"\nSolutions: {solutions}")
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()

