from cs4300_csp_parser import parse_cs4300
from cs4300_csp import solve_backtracking, solve_mrv


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python3 run_csp.py <problem.csp>")
        sys.exit(1)
    csp = parse_cs4300(sys.argv[1])
    any_sol = False
    #alternate manually for now between solve_backtracking and solve_mrv
    for i, sol in enumerate(solve_mrv(csp), 1): 
        any_sol = True
        print(f"Solution #{i}: {sol}")
    if not any_sol:
        print("No solutions.")
