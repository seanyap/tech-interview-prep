class Solution:
  def threeSumSmaller(self, nums: List[int], target: int) -> int:
    #brute force
    #idea: find all 3 nums pair whose sum is less than target, return the count
    #implement: run 3 nested loop, referencing every possible three numbers pair
    #   using 3 pointers, and keep track of the count of the sums that are less 
    #   than given target
    #logic: nums[i] + nums[j] + nums[k] < target -> count += 1
    #analysis: TC: O(n^3) SC: O(1)
    #optimal approach
    #key observation: despite the condition of i<j<k, we can still sort the 
    #   nums array bc we can treat each of the three nums either as nums[i],
    #   or nums[j] or nums[k], as long as we dont reuse the same number at.
    #idea: sort the integer array, for each number from start to end-2, use two
    #   pointer to find the pair of number that exceed target. 3 conditions:
    #   start ptr didnt move: we want to get the distance between start and end(inclusive);
    #   end ptr didnt move: get the distance from i+1 to start(exclusive); 
    #   both start and end ptr moved: get the distance of subarray length we 
    #   started with our left and right minus the distance of start(inclusive)
    #   and end(inclusive). once we get the distance we count the number of 
    #   combinations and add to count 
    #logic: check the sum of left and right, if sum > target: condition of two 
    #   pointers loop -> while sum is greater than target reduce right; if sum <= target:
    #   condition of two pointers loop -> while sum is less than or equal to target 
    #   increase left. handle duplicate by checking if cur left and right are not 
    #   equal to prev else keep increasing/decreasing left and right respectively
    #how do we find the combinations? (I didn't think of this as I thought I was
    #   going to use a library function... but it could be broken down so the num
    #   of combinations can be more easily found)
    #clean solution below (notice how we break down the problem of finding combinations
    #   adding the number of pairs that our window can form when we found out that
    #   the max - min is less than target, we know that all the pairs from max-min,
    #   (max-1)-min, (max-2)-min, ... down to ... (min+1)-min) are all valid pairs,
    #   therefore, we have a total of max minus min pairs (we have one less because
    #   we need two numbers and start is not inclusive) then we raise the bar by
    #   adding left by 1, which would make the sum larger and check if the sum is
    #   still smaller than target and so on until left and right meet which means
    #   it's time to stop bc they both are referencing 1 num which cannot form
    #   2 num pair.
    #using above clean solution, we don't have to actually visit all possible 2
    #   num pair by using the sorted subarray and count how many possible 2 num
    #   pair there are for a window which min and max satisfy the condition of sum
    #   less than target.
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) < 3:
      return 0

    sums = 0
    nums.sort()
    for i in range(len(nums) - 2):
      sums += self.__twoSumSmaller(nums[i+1:], target - nums[i])

    return sums

    def __twoSumSmaller(self, nums, target):
      sums = 0
      left, right = 0, len(nums) - 1
      while left < right:
        if nums[left] + nums[right] < target:
          sums += right - left
          left += 1
        else:
          right -= 1

      return sums

