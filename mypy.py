# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment]
    
    str1 = "hello"
str2 = "check"
str1 = "hello"
str1 = str1.lower()
str2 = str2.lower()


if(len(str1) == len(str2)):

    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)

    if(sorted_str1 == sorted_str2):
        print("TRUE")
    else:
        print("FALSE")

