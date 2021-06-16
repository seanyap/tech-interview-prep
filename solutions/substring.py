# write a function that takes in two strings and returns true if the second
# string is substring of the first, false otherwise

def substring(large_str, potential_substr):
    substr_len = len(potential_substr)

    # iterate through larger str for its length minus substr length
    for i in range(len(large_str) - substr_len):
        # iterate through potential substr  
        for j in range(substr_len):
            # if chars match in both string
            if large_str[i + j] == potential_substr[j]: 
                # if at the end of substring, return true
                if j == (substr_len - 1):
                    return True
                # else do nothing and continue looping
            else:
                break

    # did not find substring
    return False

print(substring("CATDOG", "ATDO")) # return True
print(substring("CATDOG", "ATDOGE")) # return False