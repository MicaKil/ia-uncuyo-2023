# Minimum Remaining Values (MRV) heuristic
# chooses the variable with the fewest legal values
def mrv(assignment, csp):
    assignment_indexes = [var.index for var in assignment]
    unassigned = [var for var in csp.variables if var.index not in assignment_indexes]
    return min(unassigned, key=lambda var: len(var.domain))


def select_unassigned_variable(assignment, csp, select_type=mrv):
    return select_type(assignment, csp)


# from n_queens_CSP import NQueensCSP
# nq = NQueensCSP(4)
# nq.variables[2].domain = [1, 2, 3]
# assigment = set()
# assigment.add(nq.variables[0])
# print(assigment)
# var = select_unassigned_variable(assigment, nq)
# print(var)

# ----------------------------------------------------------------------------------------------------------------------
# Least Constraining Value (LCV) heuristic
# chooses the value that rules out the fewest choices for the neighboring variables in the constraint graph

def lcv(var, assignment, csp):
    return sorted(var.domain, key=lambda val: csp.nconflicts(var, val, assignment))


def order_domain_values(var, assignment, csp, order_type=lcv):
    return order_type(var, assignment, csp)
