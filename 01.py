import pulp

if __name__ == "__main__":
    # Define the problem
    problem = pulp.LpProblem("Production_Optimization", pulp.LpMaximize)

    # Define variables
    lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')
    fruit_juice = pulp.LpVariable('Fruit_Juice', lowBound=0, cat='Integer')

    # Objective function: Maximize total production of lemonade and fruit juice
    problem += lemonade + fruit_juice, "Total Production"

    # Constraints based on resource availability
    problem += 2 * lemonade + 1 * fruit_juice <= 100, "Water Constraint"
    problem += 1 * lemonade <= 50, "Sugar Constraint"
    problem += 1 * lemonade <= 30, "Lemon Juice Constraint"
    problem += 2 * fruit_juice <= 40, "Fruit Puree Constraint"

    # Solve the problem
    problem.solve()

    # Retrieve results
    lemonade_production = pulp.value(lemonade)
    fruit_juice_production = pulp.value(fruit_juice)
    total_production = pulp.value(problem.objective)

    print(f"Lemonade Production: {lemonade_production}")
    print(f"Fruit Juice Production: {fruit_juice_production}")
    print(f"Total Production: {total_production}")