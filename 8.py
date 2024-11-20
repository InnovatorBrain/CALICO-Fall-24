from collections import defaultdict
import decimal

# Set the precision to ensure accuracy
decimal.getcontext().prec = 50

def dfs(node, graph, memo, visited):
    if node in memo:
        return memo[node]

    if node in visited:
        return decimal.Decimal(0)

    visited.add(node)
    
    # If the node is a leaf (no children), the expected steps are 0
    if not graph[node]:
        memo[node] = decimal.Decimal(0)
        visited.remove(node)
        return decimal.Decimal(0)

    # Calculate the expected value recursively for all children
    total_steps = decimal.Decimal(0)
    num_children = len(graph[node])
    
    for child in graph[node]:
        total_steps += (dfs(child, graph, memo, visited) + decimal.Decimal(1))
    
    # The expected number of steps is the average over all children
    expected_value = total_steps / num_children
    
    memo[node] = expected_value
    visited.remove(node)
    
    return expected_value

def solve():
    T = int(input())  # Read number of test cases
    for _ in range(T):
        N, S, E = map(int, input().split())  # Read N, S, E
        parents = list(map(int, input().split()))  # Read parent vertices
        
        # Build the graph as an adjacency list
        graph = defaultdict(list)
        
        for i in range(2, N + 1):
            graph[parents[i - 2]].append(i)
        
        # Add the edge from S to E (last edge)
        graph[S].append(E)
        
        # Memoization dictionary
        memo = {}
        visited = set()
        
        # Start DFS from node 1 (root node)
        result = dfs(1, graph, memo, visited)
        
        # Print the result with high precision
        print(f"{result:.16f}".rstrip('0').rstrip('.'))

if __name__ == "__main__":
    solve()
