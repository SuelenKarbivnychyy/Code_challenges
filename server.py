# Write a function that takes in a phrase and returns a dictionary that can be used to lookup words by word lengths.

# For example, the phrase "cute cats chase funny rats" should return a dictionary like so:

# {
#     4: {"cute", "cats", "rats"},
#     5: {"chase", "funny"}
# }
# Notice that the keys of the dictionary above are integers and its values are sets that contain strings.


def words_count(prase):
    
    dict_words_count = {}
    words = prase.rsplit(" ")
    
    for word in words:
        word_lenght = len(word)
        if word_lenght in dict_words_count:
            dict_words_count[word_lenght].add(word)
        else:
            dict_words_count[word_lenght] = {word}
            
    return dict_words_count
# print(words_count("cute cats chase funny rats"))    

#######################################################################################################################

# Write a function that takes in a list and reverses it in-place (without creating a new list).

def reverse_list(list_to_reverse):  
    
    
    list_lenght = len(list_to_reverse)
    print(f" List to reverse in place: {list_to_reverse}")
    half_list = int(list_lenght /2)
    
    index = 0
    last_index = list_lenght-1
    
    while index != half_list:
        
        last_item = list_to_reverse[last_index]
    
        current_item = list_to_reverse[index]
        
        # print(f"current item: {current_item} and the index is: {index} \nlast item: {last_item} and its index: {last_index}\n")

        list_to_reverse[index], list_to_reverse[last_index] = last_item, current_item
        
        index += 1
        last_index -=1
    
    return list_to_reverse
    
    
# print(reverse_list([5, 3, 5, 2, 9, 2, 1, 11, 7,12, 2]))    




##########################################################################

# Write a function that takes in two strings and returns True if the strings are anagrams of one another. 
# A Anagram is a word, phrase, or name formed by rearranging the letters of another, such as cinema, formed from iceman.
# For example,

# "moon", "noom" => True
# "bat", "snack" => False
# "", "" => True


def is_anagram(word_1, word_2):

    #######################FIRST SOLUTION################################
    
    # word_1 = word_1.replace(" ", "")
    # word_2 = word_2.replace(" ", "")

    # if len(word_1) != (len(word_2)):
    #     return False

    # for letter in word_1.lower():
    #     if letter in word_2.lower():
    #         word_2 = word_2.replace(letter, "", 1)
    #         continue
    #     else:
    #         return False

    # return True

    #####################SECOND SOLUTION######################################

    word_1 = word_1.replace(" ", "").lower()
    word_2 = word_2.replace(" ", "").lower()

    word_1_ocurrencies = {}
    word_2_ocurrencies = {}

    for letter in word_1:        
        if letter not in word_1_ocurrencies:
            word_1_ocurrencies[letter] = 1
        else:
            word_1_ocurrencies[letter] += 1

    for char in word_2:
        if char not in word_2_ocurrencies:
            word_2_ocurrencies[char] = 1
        else:
            word_2_ocurrencies[char] += 1
                 

    for item in word_1_ocurrencies:
        if item not in word_2_ocurrencies:
            return False
        else:
            if word_1_ocurrencies[item] == word_2_ocurrencies[item]:
                continue
            else:
                return False

    return True


# print(is_anagram("cinema", "iceman"))  

# TODO: Make it work with frases that contains white space
print(is_anagram("William Shakespeare", "I am a weakish speller"))
# print(is_anagram("moon", "noom"))




########################################################################################

# Write a function that prints an encrypted message.

# Using this method, the message HOT SAUCE would look like this:

# HTAC
# OSUE
# It’s a pretty simplistic method of encryption. All you do is split the letters of the initial message and alternate them over two rows of text, skipping any spaces. For example, the first letter goes in the first row, the second letter goes in the second row, the third letter goes in the first row, and so on…

# Write a function that takes in a phrase and prints an encrypted version of that phrase using the method described above.

# The phrase is guaranteed to only contain uppercase, alphabetic characters and spaces.


def encrypted_message(message_to_encrypt):

    encryption_1 = ""
    encryption_2 = ""  

    message_to_encrypt = message_to_encrypt.replace(" ", "").upper()    
 
    current_index = 0
    message_lenght = len(message_to_encrypt)

    while current_index <= message_lenght - 1: 

        if current_index == message_lenght - 1:
            encryption_1 += message_to_encrypt[-1]

            return f"{encryption_1}\n{encryption_2}"        
         
        encryption_1 += message_to_encrypt[current_index]
        encryption_2 += message_to_encrypt[current_index+1]

        # print(f"message 1: {encryption_1}, message 2: {encryption_2}, index: {current_index}")

        current_index += 2

    return f"{encryption_1}\n{encryption_2}"   

# print(encrypted_message("HOT SAUCE abecde f"))    



