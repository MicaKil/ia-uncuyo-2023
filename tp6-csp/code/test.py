from n_queens_CSP import NQueensCSP
from backtracking_search import backtracking_search
from inference import mac, forward_checking

p1 = NQueensCSP(10)

s1, r1 = backtracking_search(p1, mac)

print(s1)
ss = [i.value for i in s1]
p1.print_board(ss)
print(r1)
