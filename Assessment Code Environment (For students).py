"""
Algorithms 1 Solution
-------------------------------------------------------------------------------------------------------------------------
"""

def isValidAnagram(stringA2, stringB2):
    if sorted(stringA2) == sorted(stringB2):
        print("True")
    else:
        print("False")


stringA2 = "code"
stringB2 = "cardeo"
print(isValidAnagram(stringA2, stringB2))

# Some test cases are included in order to help you test your solution
# Please note that these are not exhaustive - more will be used during marking, these are only a select few given to help you
# As a result, make sure to think up some on your own and test your code as well!

# Sample Tests for Algorithms 1
print ("\nAlgorithms 1 Tests")
# ---------------------------------------------------------

stringA = "code"
stringB = "odec"
print(isValidAnagram(stringA, stringB))  # TRUE

stringA2 = "code"
stringB2 = "cardeo"
print(isValidAnagram(stringA2, stringB2))  # FALSE

stringA3 = "exercise"
stringB3 = "exorcise"
print(isValidAnagram(stringA3, stringB3))  # FALSE

"""Time Complexity: O(n log (n))

Space Complexity: O(n)"""


"""
Algorithms 2 Solution
-------------------------------------------------------------------------------------------------------------------------
def isSequenceDistinct(sequence):
    pass

# Some test cases are included in order to help you test your solution
# Please note that these are not exhaustive - more will be used during marking, these are only a select few given to help you
# As a result, make sure to think up some on your own and test your code as well!

# Sample Tests for Algorithms 2
print ("\nAlgorithms 2 Tests")
# ---------------------------------------------------------

array1 = ["a", "b", "c", "a"]
print(isSequenceDistinct(array1))  # FALSE

array2 = ["a", 1, 2, "b", 3]
print(isSequenceDistinct(array2))  # TRUE

"""