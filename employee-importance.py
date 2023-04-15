"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        adj_list = defaultdict(list)

        for employee in employees:
            adj_list[employee.id] = [employee.importance, employee.subordinates]

        visited = set()


        def dfs(val):
            
            visited.add(val)
            neighbours = adj_list[val]
            importance_value = neighbours[0]

            for neighbour in neighbours[1]:
                if neighbour not in visited:
                    importance_value += dfs(neighbour)

            return importance_value
 
        return dfs(id)