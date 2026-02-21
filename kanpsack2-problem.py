# Corrected Knapsack using recursion + memoization
dp = [[]]

def solve(weight, value, currW, currI):
    global dp
    
    # Base case
    if currI == 0 or currW == 0:
        return 0
    
    # If already computed
    if dp[currI][currW] != -1:
        return dp[currI][currW]
    
    # If current item can't be included
    if weight[currI-1] > currW:
        dp[currI][currW] = solve(weight, value, currW, currI-1)
        return dp[currI][currW]
    
    # Either include or exclude the current item
    include = value[currI-1] + solve(weight, value, currW - weight[currI-1], currI-1)
    exclude = solve(weight, value, currW, currI-1)
    
    dp[currI][currW] = max(include, exclude)
    return dp[currI][currW]

def knapsack(totalW, weight, value):
    global dp
    n = len(weight)
    dp = [[-1 for i in range(totalW+1)] for i in range(n+1)]
    return solve(weight, value, totalW, n)

# Example usage
weight = [1, 2, 3]
value = [6, 10, 12]
targetW = 5
print(knapsack(targetW, weight, value))  # Expected output: 22