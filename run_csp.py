from cs4300_csp_parser import parse_cs4300
from cs4300_csp import solve_backtracking, solve_mrv

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python3 run_csp.py <problem.csp>")
        sys.exit(1)
    csp = parse_cs4300(sys.argv[1])
    any_sol = False
    
    #solver_function = solve_mrv 
    solver_function = solve_backtracking

    for i, sol in enumerate(solver_function(csp), 1): 
        any_sol = True
        print(f"Solution #{i}: {sol}")

        print("  Grid View, blank if not sudoku:")
        for r in range(1, 5):
            row_str = "  "
            for c in range(1, 5):
                var_name = f"V_{r}{c}"
                value = sol.get(var_name, '.')
                row_str += f"{value} "
            print(row_str)
        
        print("-" * 20)

    if not any_sol:
        print("No solutions.")