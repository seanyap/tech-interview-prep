# Problem => https://leetcode.com/problems/minimum-window-substring/

class Solution:
  def minWindow(self, s: str, t: str) -> str:
    """
    FRAMEWORK  
    1) problem category: string
    
    2) brute force solution
    - generate all window substrings
        - for each window, check if the window contains all of T string chars
        - if yes => check if the length is shorter than what we have seen 
    - return the window substring if we found it else an empty string
    O(N^3) => O(N^2) for generating all the substrings, O(N) check for each 
              window if it contains all characters of T
    
    3) optimized solution (idea)
    - string category can take advantage of 2 pointers to generate all 
      window substrings O(N) time complexity
    - instead of the previous O(N) check to see if current window contains all
      characters in T, we can make use of HASHMAP/dictionary + variable keeping
      track of remainingChars our window still needs to achieve O(1) lookup
      
    4) algorithm pseudocode
    - verify that S is at least length of T
    - 2 pointers: start(left) and end(right)[our for loop ptr]
    - remainingChars variable
    - hashmap of T string => (key: letter, value: frequency) (keep forgeting)
    - iterate over S string
        - check if hashmap contains char at right pointer 
            - reduce 1 from hashmap 
            - check if the value of the character is greater than or 
              equal to 0 
                - reduce 1 from remainingChars
        - repeatedly check(while loop) if we still have a valid window AND
          is still within BOUNDS
            - bring start pointer closer to end
            - update hashmap and remainingChar 
    - return the substring if we found it, else return empty string
    """
    if len(s) < len(t):
        return ""

    start, result_window, remChars = 0, None, len(t)
    letters = {}
    # populate hashmap with letters in T
    for letter in t:
        letters[letter] = letters.get(letter, 0) + 1

    for end, letter in enumerate(s):
        if letter in letters:
            letters[letter] -= 1
            if letters[letter] >= 0:
                remChars -= 1
        # repeatedly check if we still have a valid window after reducing it
        while remChars == 0 and end >= start:
            # when we are inside of this while loop, that means our current
            # window (end-start+1) is valid
            if result_window is None or end-start+1 < len(result_window):
                # slice the smaller valid string
                result_window = s[start:end+1]
            
            # important to check because we only keep track of only letters 
            # in T string, make sure we check s[start] and not our var 
            # "letter" bc we keep reducing start (you always forget)
            if s[start] in letters: 
                letters[s[start]] += 1
                # reduce the window and check if it is still valid
                if letters[s[start]] > 0:
                    remChars += 1
            start += 1
            
    return result_window if result_window is not None else ""

  """
  5) Review after reading other people's code
  - the while loop on like 54 is running the checks (if statements) on line 57 & 64
    each iteration, which is unnecessary work
    - instead, we could have the while loop sole responsiblity be to find the smallest
      START pointer that still forms a valid window
    - then, we only have to check once if the current window is smaller than the one
      we have so far
  - another slight inefficiency is that my code is slicing the string for each valid
    window. this means my code is copying a new string because string in python is 
    immutable. 
    - a workaround could be storing the start and end pointers for the smallest window
      we have seen and when we exit the loop, we slice the substring and return it.
      this way we only copy the string once, instead of for each valid window we encountered
  - instead of manually populating a hashmap of the characters in T, we can use 
    built-in python library to help us => collections.Counter(input)
  """
  # solution from https://leetcode.com/problems/minimum-window-substring/discuss/26804/12-lines-Python/1079619
  def betterMinWindow(self, s: str, t: str) -> str:
    # hash table to store the required char frequency
    need = collections.Counter(t)            
    # total character count we need to care about
    missing = len(t)                         
    # windowStart and windowEnd pointers for the smallest valid window we've seen
    windowStart, windowEnd = 0, 0
    # i and j are the pointers for current window we are iterating 
    i = 0

    # iterate over s starting over index 1
    for j, char in enumerate(s, 1):          
      # if char is required then decrease missing
      if need[char] > 0:                   
        missing -= 1

      # decrease the freq of char from need (may be negative - which basically denotes
      # that we have few extra characters which are not required but present within current window)
      need[char] -= 1  
                          
      # we found a valid window
      if missing == 0:                     
        # chars from start to find the real windowStart & boundary check 
        while i < j and need[s[i]] < 0:  
          need[s[i]] += 1
          i += 1

        # if it's only one char case or curr window is smaller, then update window
        if windowEnd == 0 or j-i < windowEnd-windowStart:  
          windowStart, windowEnd = i, j

        # now resetting the window to make it invalid
        # make sure the first appearing char satisfies need[char]>0
        need[s[i]] += 1          

        # missed this first char, so add missing by 1
        missing += 1                     

        #update i to windowStart+1 for next window
        i += 1                          

    # slice from our pointers to copy a new string (windowEnd char is exclusive?)
    return s[windowStart:windowEnd]