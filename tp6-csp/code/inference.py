from queue import Queue


# function AC-3(csp) returns false if an inconsistency is found and true otherwise
#     inputs: csp, a binary CSP with components (X, D, C)
#     local variables: queue, a queue of arcs, initially all the arcs in csp
#     while queue is not empty do
#         (Xi, Xj) ← REMOVE-FIRST(queue)
#         if REVISE(csp, Xi, Xj ) then
#             if size of Di = 0 then return false
#             for each Xk in Xi.NEIGHBORS - {Xj} do
#                 add (Xk, Xi) to queue
#     return true

def ac3(csp, arcs):
    while not arcs.empty():
        xi, xj = arcs.get()
        #print("     get xi: ", xi.index, " xj: ", xj.index)
        if revise(csp, xi, xj):
            #print("     revised: ", xi, xj)
            if len(xi.domain) == 0:
                return False
            xk_list = get_neighbors(xi, xj, arcs)
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
        #print("     xi: ", xi.index, "x: ", x)
        #print("     ", [csp.constraints(xi, xj, x, y) for y in xj.domain])
        if not any(csp.constraints(xi, xj, x, y) for y in xj.domain):  # if there is no value y in Dj that allows (x,y)
            xi.domain.remove(x)
            revised = True
    return revised


def get_neighbors(xi, xj, arcs: Queue):
    neighbors = set()
    for (xk, xl) in arcs.queue:
        if xl == xi and xk != xj:
            if xk != xi:
                neighbors.add(xk)
    return neighbors


#-----------------------------------------------------------------------------------------------------------------------
# MAC (Maintaining Arc Consistency) algorithm
# instead of a queue of all arcs in the CSP, we start with only the arcs (Xj,Xi) for all Xj that are unassigned
# variables that are neighbors of Xi

def mac(csp, var):
    arcs = Queue()
    neighbors = csp.get_unassigned_neighbors(var)
    #print("     neighbors: ", neighbors)
    for neighbor in neighbors:
        arcs.put((neighbor, var))
    return ac3(csp, arcs)


#-----------------------------------------------------------------------------------------------------------------------
# Inference

def inference(csp, var, inference_type=mac):
    return inference_type(csp, var)
