def subset_sum(expenses, budget): #def used to declare a function in python that means define
    n = len(expenses) #Count of available items
    dp = [[False] * (budget + 1) for _ in range(n + 1)]  #Create the DP matrix
    dp[0][0] = True #Initialize base case — zero sum is possible with no items

    # Fill the DP table
    for i in range(1, n + 1):
        for j in range(budget + 1):
            if j < expenses[i - 1]['cost']:
                dp[i][j] = dp[i - 1][j] #If current budget j is smaller than current expense cost, we cannot include this expense.
            else:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - expenses[i - 1]['cost']]

    # Backtrack to find the selected expenses
    for j in range(budget, -1, -1):
        if dp[n][j]:
            result = []
            w = j
            for i in range(n, 0, -1):
                if w >= expenses[i - 1]['cost'] and not dp[i - 1][w]:
                    result.append(expenses[i - 1])
                    w -= expenses[i - 1]['cost']
            return result[::-1]  # Return in original order

    return []  # Return empty list if no valid subset is found