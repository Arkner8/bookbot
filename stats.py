def get_num_words(text):
    words = text.split()
    return len(words)

def count_character(text):
    count = {"a": 0}
    
    for character in text:
        character = character.lower()
        if character not in count:
            count[character] = 1
        else:
            count[character] += 1
    
    # count = sorted(count.items())
    
    return count

def sorted_list(dic):
    sorted = []

    for d in dic:
        if d.isalpha():
            l = dic[d]
            sorted.append({"letter" : d, "count":l})

    sorted.sort(reverse=True, key=sort_on)

    return sorted

def sort_on(items):
    return items["count"]