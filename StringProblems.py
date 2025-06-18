from collections import Counter

def reverse_string(string_to_reverse):
    return string_to_reverse[::-1]

def palindrome_check(input_string):
    input_string = str(input_string)
    if input_string == input_string[::-1]:
        return True
    return False

def count_vowels_and_consonants(input_string):
    vowels = 0
    consonants = 0
    for i in range(len(input_string)):
        if input_string[i].lower() in ["a","e","i","o","u"]:
            vowels+=1
        else:
            consonants+=1
    print("Vowels: {}, Consonants: {}" .format(vowels,consonants))

def find_the_longest_word(input_string):
    list_of_words = input_string.split(" ")
    return max(list_of_words, key=len)

def character_frequency(input_string):
    return Counter(str(input_string))

def remove_duplicates(input_string):
    seen = set()
    resultant_string = ""
    for i in input_string:
        if not i in seen:
            seen.add(i)
            resultant_string+=i
    return resultant_string

def anagram_check(input_string_1,input_string_2):
    return Counter(input_string_1.lower()) == Counter(input_string_2.lower())

def substring_count(input_string, substring):
    count = 0
    start = 0

    while True:
        start = input_string.find(substring, start)
        if start == -1:
            break

        count += 1
        start += len(substring)
    return count

def capitalize_first_letters(input_string):
    list_of_words = input_string.split()
    return " ".join(word.capitalize() for word in list_of_words)

def find_the_first_non_repeating_character(input_string):
    count_of_chars = Counter(input_string.lower())
    for char in input_string:
        if count_of_chars[char.lower()] == 1:
            return char
    return ""

def find_first_unique_character(input_string):
    count_of_ch = {}
    for i in range(len(input_string)):
        if input_string[i] in count_of_ch:
            count_of_ch[input_string[i]] += 1
        else:
            count_of_ch[input_string[i]] = 1
    for key, value in count_of_ch.items():
        if value == 1:
            return key
    return None

def find_first_unique_character_Counter(input_string):
    count_of_ch = Counter(input_string)
    for key, value in count_of_ch.items():
        if value == 1:
            return key
    return None


def main():
    print("Reverse string of ANKITA: ", reverse_string("ANKITA"))
    
    print("Palindrome check of ANKITA: ", palindrome_check("ANKITA"))
    print("Palindrome check of MALAYALAM: ", palindrome_check("MALAYALAM"))
    print("Palindrome check of 1234321: ", palindrome_check(1234321))

    count_vowels_and_consonants("ANKITA")
    count_vowels_and_consonants("Saketh")

    print("Longest word in \'Bright and sunny days make everything better.\' is: ", find_the_longest_word("Bright and sunny days make everything better."))

    print("Character frequency in BANANA is: ", character_frequency("BANANA"))
    print("Character frequency in 123123412345 is: ", character_frequency(123123412345))

    print("The word \'programming\' after removing duplicates becomes: ", remove_duplicates("programming"))

    print(anagram_check("LISTEN@","SIL@ENT"))

    print(substring_count("hello world, hello", "hello"))

    print(substring_count("I am an automation tester who performs functional testing for APIs. I also do integration testing, performance testing and regression testing.", "test"))

    print(capitalize_first_letters("I am an automation tester who performs functional testing for APIs. I also do integration testing, performance testing and regression testing."))

    print(find_the_first_non_repeating_character("I am an automation tester"))

    print(find_first_unique_character("abcabbabdd"))

    print(find_first_unique_character_Counter("abcabbabdd"))

if __name__ == "__main__":
    main()