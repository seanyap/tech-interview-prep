class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #bruteforce solution
        #find all subarrays and their sum 
        #keep track the largest sum to return
        """
        maxSum, curSum = float('-inf'), 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                curSum += nums[j]
                maxSum = max(curSum, maxSum)
            curSum = 0
        return maxSum
        """
        #optimized solution
        #notice the repeated sum of the same window of subarray
        #we can use dynamic programming to optimized by caching the best sum so far
        #notice we are not caching every sum we calculate, but the best sum
        #best sum = any value that is positive / >0
        #format of sub-problem = maxSubArray(A, i) where A[0:i] is the best sum
        #sub-problem is related to the orginal problem by:
        # maxSubArray(A,i) = A[i] + (maxSubArray(A,i) > 0 ? maxSubArray(A,i) : 0)

        #we can eliminate this check because if the list contains only one item,
        #then our range function condition i<n will be false so it wouldn't run
        #and finally we return the item value bc we set our maxSum to it to begin
        # if len(nums) == 1:
        #     return nums[0]
        
        #initialize maxSum to first element instead of negative inf so we don't 
        #have to check it manually bc loop does the check for us
        maxSum, dp = nums[0], [0] * len(nums) 
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            # if dp[i-1] > 0:
            #     dp[i] = dp[i-1] #bring in the positive sum from prev subarray
            # dp[i] += nums[i]
            #above code can be replaced with this one line
            #make sure to surround ternary with parenthesis
            dp[i] = nums[i] + (dp[i-1] if dp[i-1]>0 else 0)
            maxSum = max(maxSum, dp[i])
        
        return maxSum
