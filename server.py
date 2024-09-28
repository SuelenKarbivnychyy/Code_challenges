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
