from queue import Queue


# function AC-3(csp) returns false if an inconsistency is found and true otherwise
#     inputs: csp, a binary CSP with components (X, D, C)
#     local variables: queue, a queue of arcs, initially all the arcs in csp
#     while queue is not empty do
#         (Xi, Xj) ← REMOVE-FIRST(queue)
#         if REVISE(csp, Xi, Xj ) then
#             if size of Di = 0 then return false
#             for each Xk in Xi.NEIGHBOURS - {Xj} do
#                 add (Xk, Xi) to queue
#     return true

def ac3(csp, arcs):
    while not arcs.empty():
        xi, xj = arcs.get()
        if revise(csp, xi, xj):
            if len(xi.domain) == 0:
                return False
            xk_list = get_neighbours(xi, xj, arcs)
            for xk in xk_list:
                if (xk, xi) not in arcs.queue:
                    arcs.put((xk, xi))
    return True


# function REVISE(csp, Xi, Xj) returns true iff we revise the domain of Xi
#     revised ← false
#     for each x in Di do
#         if no value y in Dj allows (x ,y) to satisfy the constraint between Xi and Xj then
#             delete x from Di
#             revised ← true
#     return revised

def revise(csp, xi, xj):
    revised = False
    for x in xi.domain:
        if not any(csp.constraints(xi, xj, x, y) for y in xj.domain):  # if there is no value y in Dj that allows (x,y)
            xi.domain.remove(x)
            revised = True
    return revised


def get_neighbours(xi, xj, arcs: Queue):
    neighbours = set()
    for (xk, xl) in arcs.queue:
        if xl == xi and xk != xj:
            if xk != xi:
                neighbours.add(xk)
    return neighbours


#-----------------------------------------------------------------------------------------------------------------------
# MAC (Maintaining Arc Consistency) algorithm
# instead of a queue of all arcs in the CSP, we start with only the arcs (Xj,Xi) for all Xj that are unassigned
# variables that are neighbors of Xi

def mac(csp, var):
    arcs = Queue()
    neighbours = csp.get_unassigned_neighbours(var)
    for neighbour in neighbours:
        arcs.put((neighbour, var))
    return ac3(csp, arcs)


#-----------------------------------------------------------------------------------------------------------------------
# Forward checking
# Whenever a variable X is assigned, the forward-checking process establishes arc consistency for it: for each
# unassigned variable Y that is connected to X by a constraint, delete from Y’s domain any value that is inconsistent
# with the value chosen for X.

def forward_checking(csp, var):
    neighbours = csp.get_unassigned_neighbours(var)
    for neighbour in neighbours:
        for value in neighbour.domain:
            if not csp.constraints(var, neighbour, var.value, value):  # si no es consistente...
                neighbour.domain.remove(value)
        if len(neighbour.domain) == 0:
            return False
    return True


#-----------------------------------------------------------------------------------------------------------------------
# Inference

def inference(csp, var, inference_type=mac):
    return inference_type(csp, var)
