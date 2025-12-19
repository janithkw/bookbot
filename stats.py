def get_num_words(text):
    words = text.split()
    return len(words)

#Count characters of text and return as dictionary
def get_char_count(text):
    char_count = dict()
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
        
    return char_count

def sort_on_num(char_dict):
    return char_dict["num"]


def get_sorted_characters(char_count):
    # Convert dict to list of {"char": c, "num": n} then sort descending by count
    char_list = [{"char": char, "num": count} for char, count in char_count.items()]
    char_list.sort(reverse=True, key=sort_on_num)
    return char_list
