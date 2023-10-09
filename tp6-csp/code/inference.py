from queue import *


# function REVISE(csp, Xi, Xj ) returns true iff we revise the domain of Xi
#     revised ← false
#     for each x in Di do
#         if no value y in Dj allows (x ,y) to satisfy the constraint between Xi and Xj then
#             delete x from Di
#             revised ← true
#     return revised

def revise(csp, xi, xj):
    revised = False
    for x in xi.domain:
        if not any(csp.constraints(xi, xj, x, y) for y in xj.domain):
            xi.domain.remove(x)
            revised = True
    return revised


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

def ac3(csp, queue):
    while not queue.empty():
        xi, xj = queue.get()
        if revise(csp, xi, xj):
            if len(xi.domain) == 0:
                return False
            xk_list = get_neighbors(xi, xj, queue)
            for xk in xk_list:
                queue.put((xk, xi))
    return True


def get_neighbors(xi, xj, queue):
    neighbors = set()
    len_queue = queue.qsize()
    for i in range(len_queue):
        xk, xl = queue[i]
        if xl == xi and xk != xj:
            if xk != xi:
                neighbors.add(xk)
    return neighbors
