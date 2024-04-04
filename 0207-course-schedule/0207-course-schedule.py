class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        for current, pre in prerequisites:
            preMap[current].append(pre)

        
        visited = set()
        def dfs(current):
            if current in visited:
                return False
            if preMap[current] == []:
                return True
            
            visited.add(current)
            for pre in preMap[current]:
                if not dfs(pre):
                    return False
            visited.remove(current)
            preMap[current] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True



        