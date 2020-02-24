# Install Sympy and import all with sym
import sympy as sym
import numpy as np

class MaximaExamples:
    def __init__(self):
        """[Constructor] Declare symbolic variables"""
        self.x, self.y, self.z, self.H, self.R = sym.symbols('x y z H R')

    def solve(self):
        """1. EXAMPLE solve(x^2=2,x)"""
        result = sym.solveset(
            sym.Add(
                sym.Pow(
                    self.x, 
                    sym.Integer(2)
                ), 
                sym.Integer(-2)
            ), 
            self.x
        )
        return result

    def area_volume(self):
        """
        2. EXAMPLE (R: 2, H: 3)$ A : 2*%pi*R*(R + H); V : %pi*R^2*H 
        If you want evaluate expression you need to sentence pi.evalf(num)
        instead of pi, and argument 'num' is the amount of decimals of pi to
        calculate. Also, you can use float(pi)."""
        area = sym.Mul(
            sym.Integer(2), 
            sym.pi, 
            self.R, 
            sym.Add(self.R, self.H)
        )
        volume = sym.Mul(
            sym.pi.evalf(30), 
            sym.Pow(
                self.R, 
                sym.Integer(2)
            ), 
            self.H
        )
        return area, volume

    
    def functions(self):
        """
        3. EXAMPLE A(H, R) := 2*%pi*R(R+H); V(R, H) := %pi*R^2*H
        Function inside function for educational porposes.
        Insert ratio and hegith evaluated dinamically."""
        def area(ratio, height): 
            result = sym.Mul(
                sym.Integer(2), 
                float(sym.pi), 
                sym.Rational(ratio), 
                sym.Add(sym.Rational(ratio), 
                sym.Rational(height))
            )
            return result
        def volume():
            result = sym.Mul(
                sym.pi, 
                sym.Pow(self.R, sym.Integer(2)), 
                self.H
            ) 
            return result
        # Instanciate area and volume functions with arguments
        area = area(2, 3)
        volume = volume()
        # The same logic as example 2 on separate functions()
        return area, volume
    
    def maxima_expressions(self):
        """4. MAXIMA EXAMPLE of maxima expressions"""
        def arithmetic_operations():
            pass
        pass
            


def print_examples():
    """Print function"""
    """Instanciate functions inside dictionary"""
    examples = MaximaExamples()
    functions_dictionary = {
        'maxima_1': examples.solve(),
        'maxima_2': examples.area_volume(),
        'maxima_3': examples.functions()
    }
    # Iterate functions dictionary and print result
    for key, value in functions_dictionary.items():
        print(key + ' -->', value)



if __name__ == '__main__':
    # Execute print function
    print(4 * '\n')
    print('\t ~ MAXIMA TO SYMPY ~')
    print('\t-------------------------------')
    print('\n')
    print_examples()
    print(4 * '\n')
