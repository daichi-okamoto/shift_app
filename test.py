from ortools.linear_solver import pywraplp

def main():
    # Create the mip solver with the SCIP backend.
    solver = pywraplp.Solver.CreateSolver('SCIP')
    if not solver:
        return

    # Data
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    num_items = len(weights)
    capacity = 5

    # Decision variables
    x = []
    for i in range(num_items):
        x.append(solver.IntVar(0, 1, 'x[%i]' % i))

    # Constraints
    # The total weight of the selected items cannot exceed the capacity.
    solver.Add(sum(x[i] * weights[i] for i in range(num_items)) <= capacity)

    # Objective
    # Maximize the total value of the selected items.
    solver.Maximize(solver.Sum(x[i] * values[i] for i in range(num_items)))

    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        print('Objective value =', solver.Objective().Value())
        for i in range(num_items):
            print('x[%i] = %i' % (i, x[i].solution_value()))
    else:
        print('The problem does not have an optimal solution.')

if __name__ == '__main__':
    main()
