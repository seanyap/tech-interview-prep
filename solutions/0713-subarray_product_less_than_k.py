class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        #bruteforce
        #idea: find every possible subarray and find the product of all nums in each subarray
        #   to see if they are less than target. 
        #implement: two nested loops to create all possible subarray, for each subarray find the
        #   product of all nums, which require another loop
        #analysis: generating subarray TC: O(n^2), for each subarray, get its num product TC: O(n)
        #   total TC: O(n^3). Space: O(1)
        #optimal solution
        #idea: find the product of nums from start to each of the indexes of our given input arr
        #   and store them in an array. then iterate over all nums, and find all windows starting
        #   at cur index to all possible remaining index whose product is less than target. since
        #   we have cached the product of nums from start to cur index, we could simply compute the
        #   product of our given subarray by dividing cur index product by the product at start-1. 
        #implement: run a loop to iterate over all nums, for each num, we run a loop to find all the
        #   window end that has a product that is less than target. 
        #logic(performed each loop iteration): if cur product divided by start-1 product is less than
        #   target, add 1 to count, else break inner loop and continue to next num in outer loop
        #analysis: looping once to find the product so far take O(n), running two nested loop that
        #   to find all subarrays take O(n^2). TC: O(n^2). Space: O(n)
        """
        count, products_from_start = 0, [nums[0]]
        n = len(nums)
        for i in range(1, n):
            prev, cur = products_from_start[i-1], nums[i]
            products_from_start.append(prev * cur)
        for start in range(n):
            for end in range(start, n):
                if start == 0: 
                    if products_from_start[end] < k:
                        count += 1
                    else:
                        break
                else: #start is 1,2,3,...,n-1; we need this to prevent index out of bounds when calculating start-1
                    if (products_from_start[end] / products_from_start[start-1]) < k:
                        count += 1
                    else:
                        break
        return count
        """ 
        #above solution is still too baby for leetcode (TLE)
        #idea: we are looking for the "number" of subarrays, not the max/min, therefore we need to keep
        #   track of the count for each window that is valid (product of all elements is less than k)
        #logic: if current window is valid, we need to count the size of our window(end-start+1) and
        #   add it to the "number" of subarrays. think of each count as the number of possible subarrays
        #   that can be created with end as the element that presents on each of those subarrays
        #   (notice end is at the start)
        #   ex: [2,3,4] -> 3 possible subarray with num 4(end) present -> [3], [3,2], [3,2,1] 
        #        ^   ^
        #        s   e
        #   when window is invalid, divide current product until it becomes valid, THEN count the "number"
        #   of subarrays present in this window (if we dont count now, when we increase the window, it becomes
        #   difficult to count, unless using a formula. but we can gradually count it so we dont need the formula)
        #   (remember the combination formula originates from count step by step like in this case)
        #   (when REVIEWING this question, try to imagine how the subarray count builds from size 1 at end 
        #   all the way to actual count)
        #observation: remember we are dealing with everything that is LESS THAN k, so the "number" ranges
        #   from size 1 (one element product), all the way to n (if the product of all elements are less than k)
        start, product, combinations = 0, 1, 0
        for end in range(len(nums)):
            product *= nums[end]
            while start <= end and product >= k:
                product /= nums[start]
                start += 1
            combinations += end-start+1
        return combinations

if __name__ == "__main__":
    solution = Solution()
    result = solution.numSubarrayProductLessThanK([10, 5, 2, 6], 100)
    print(result) #expect 8