#lab 10 breze howard

import string

#helper function to clean the string (ignore spaces, punctuation, and letter case)
def clean_string(s):
    return ''.join(char.lower() for char in s if char.isalpha())

#recursive function to check if the string is a palindrome
def is_palindrome(s):
    #clean the string by removing non-alphabetic characters and converting to lowercase
    s = clean_string(s)
    
    #base case: if the string is empty or has only one character, it is a palindrome
    if len(s) <= 1:
        return True
    #recursive case: compare the first and last characters
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])  #recur with the substring without the first and last characters

#recursive function to count vowels and consonants in the string
def count_vowels_consonants(s):
    #clean the string by removing non-alphabetic characters and converting to lowercase
    s = clean_string(s)
    
    vowels = "aeiou"
    #base case: If the string is empty, return 0 vowels and 0 consonants
    if len(s) == 0:
        return 0, 0
    
    #check if the first character is a vowel or consonant
    first_char = s[0]
    if first_char in vowels:
        vowel_count, consonant_count = count_vowels_consonants(s[1:])
        return vowel_count + 1, consonant_count
    elif first_char.isalpha():
        vowel_count, consonant_count = count_vowels_consonants(s[1:])
        return vowel_count, consonant_count + 1
    else:
        #skip non-alphabetic characters
        return count_vowels_consonants(s[1:])
    
#main logic to check if the string is a palindrome and if it has more vowels than consonants
def analyze_string(s):
    palindrome_result = is_palindrome(s)
    vowels, consonants = count_vowels_consonants(s)
    
    #determine if the string has more vowels than consonants
    more_vowels = vowels > consonants
    
    #print the results
    print(f"String: {s}")
    print(f"Is palindrome: {palindrome_result}")
    print(f"More vowels than consonants: {more_vowels}")

#example
string = "Eevee"
analyze_string(string)