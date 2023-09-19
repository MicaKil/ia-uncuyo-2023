from agent import Agent
from search_algorithms import dfs
class DLSAgent(Agent):
    def search(self, limit):
        result = dfs(self, limit)
        if result is None:
            print("Solución no encontrada")
            print("Estados explorados: ", self.states_explored)
            self.env.plot_environment()
        return result

# function DEPTH-LIMITED-SEARCH(problem, limit ) returns a solution, or failure/cutoff
#    return RECURSIVE-DLS(MAKE-NODE(problem.INITIAL-STATE), problem, limit )
# function RECURSIVE-DLS(node, problem, limit ) returns a solution, or failure/cutoff
    # if problem.GOAL-TEST(node.STATE) then return SOLUTION(node)
    # else if limit = 0 then return cutoff
    # else
        # cutoff occurred?←false
        # for each action in problem.ACTIONS(node.STATE) do
            # child ←CHILD-NODE(problem, node, action)
            # result ←RECURSIVE-DLS(child , problem, limit − 1)
            # if result = cutoff then cutoff occurred?←true
            # else if result != failure then return result
        # if cutoff occurred? then return cutoff else return failure
        
    # def search(self, limit):
    #     #global explored
    #     #explored = set() # un set vacío 
    #     return self.recursive_dfs(Node(self.env), limit)
    
    # def recursive_dfs(self, node, limit):
    #     if self.env.goal_test(node.state):
    #         return node
    #     elif limit == 0:
    #         return "cutoff" #cutoff value indicates no solution within the depth limit

    #     cutoff_occurred = False
    #     #global explored

    #     for action in self.env.actions:
    #         child = node.child_node(action)
    #         self.states_explored += 1
    #         #if (child.state not in explored):
    #         result = self.recursive_dfs(child, limit - 1)
    #         if result == "cutoff":
    #             cutoff_occurred = True
    #         elif result != None:
    #             return result
                
    #     #explored.add(node.state)

    #     if cutoff_occurred:
    #         return "cutoff"
    #     else:
    #         return None

# iterative