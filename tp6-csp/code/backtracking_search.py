from variable_and_value_ordering import select_unassigned_variable, order_domain_values


# function BACKTRACKING-SEARCH(csp) returns a solution, or failure
#   return BACKTRACK({ }, csp)

# function BACKTRACK(assignment, csp) returns a solution, or failure
#   if assignment is complete then return assignment
#   var ← SELECT-UNASSIGNED-VARIABLE(csp)
#   for each value in ORDER-DOMAIN-VALUES(var, assignment, csp) do
#       if value is consistent with assignment then
#           add {var = value} to assignment
#           inferences ← INFERENCE(csp, var , value)
#           if inferences != failure then
#               add inferences to assignment
#               result ← BACKTRACK(assignment, csp)
#               if result != failure then
#                   return result
#       remove {var = value} and inferences from assignment
#   return failure


def backtrack_nquenns(assignment: set, csp):
    if len(assignment) == len(csp.variables):
        return assignment

    var = select_unassigned_variable(assignment, csp)
    sorted_domain = order_domain_values(var, assignment, csp)
    for value in sorted_domain:
        if csp.is_consistent(value, assignment, csp):
            var.value = value
            assignment.add(var)
            inferences = inference(csp, var, value)
            if inferences != None:
                assignment.update(inferences)
                result = backtrack(assignment, csp)
                if result != None:
                    return result
        del assignment[var]
        for inference in inferences:
            del assignment[inference]
    return None
