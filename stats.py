def count_book_words(book_text):
    words = book_text.split()
    return len(words)

def count_characters(book_text):
    dict_char = {}

    for c in book_text:
        d = c.lower()
        if d in dict_char:
            dict_char[d] += 1
        else:
            dict_char[d] =1
    
    return dict_char

def sort_on(items):
    return items["num"]

def list_of_dict(dict_to_list):
    final_list = []
    for entry in dict_to_list:
        if entry.isalpha() == True:
            my_dict ={}
            my_dict["char"] = entry
            my_dict["num"] = dict_to_list[entry]
            final_list.append(my_dict)
    final_list.sort(reverse=True, key=sort_on)
    return final_list