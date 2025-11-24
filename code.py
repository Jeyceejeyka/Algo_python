# 1. Reverse a String (No built-ins allowed except loops)

# Write a function that takes "hello" and returns "olleh" without using .reverse() or slicing tricks.

def reverse(s):
    result = ""
    for char in s:
        result = char + result
    return result
print(reverse("hello"))  # Output: "olleh"



def palindrome(s):
    reversed_s = ""
    for char in s:
        reversed_s = char + reversed_s
    return s == reversed_s
print(palindrome("racecar"))  # Output: True
print(palindrome("hello"))     # Output: False

def longest_word(words):
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest
print(longest_word(["apple", "banana", "cherry", "date"]))  # Output: "banana"

def merge_two_sorted_lists(list1, list2):
    merged = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
    while i < len(list1):
        merged.append(list1[i])
        i += 1
    while j < len(list2):
        merged.append(list2[j])
        j += 1
    return merged
print(merge_two_sorted_lists([1, 2, 5], [2, 4, 6]))  



def merge_sorted_2_list(list1,list2):
    merged = list1 + list2
    
    return sorted(merged)

print(merge_sorted_2_list([1, 25, 8], [3, 4, 5,2,5,6,7,8,9,78,1])) 


def merged_sorted_lists(list1, list2):
    merged = []
    i, j = 0, 0
    
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
            
    while i < len(list1):
        merged.append(list1[i])
        i += 1
        
    while j < len(list2):
        merged.append(list2[j])
        j += 1
        
    return merged

print(merged_sorted_lists([1, 3, 5], [2, 4, 66]))      


