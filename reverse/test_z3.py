from z3 import *

# Create a symbolic integer variable
x = Real('x')

# Define the constraint
equation =(x**2) -4 *x +4==7/2

# Create a Z3 solver
solver = Solver()

# Add the equation constraint to the solver
solver.add(equation)

# Check if the constraints are satisfiable
if solver.check() == sat:
    model = solver.model()
    value_of_x = model[x]
    print(f"x = {value_of_x}")
else:
    print("Unsatisfiable")
