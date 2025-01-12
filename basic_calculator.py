class BasicCalculator():
    def __init__(self, *args):
        self.arguments = args[0]
    
    def __repr__(self):
        return f"BasicCalculator({self.arguments})"

    def add(self):
        print(self.arguments)
        return sum(self.arguments)
    
    def subtract(self):
        subtract = self.arguments[0] - sum(self.arguments[1:])
        return subtract
    
    def multiply(self):
        multiply = 1
        for i in self.arguments:
            multiply *= i
        return multiply
    
    def divide(self):
        divide = self.arguments[0]
        for i in self.arguments[1:]:
            divide /= i
        return divide
    

    
    
    