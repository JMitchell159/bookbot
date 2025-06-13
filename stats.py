def num_words(text):
    return len(text.split())

def num_char(text):
    counts = {}
    lowercase = text.lower()

    for symbol in lowercase:
        if symbol in counts:
            counts[symbol] += 1
        else:
            counts[symbol] = 1
    
    return counts

def num_char_sorted(text):
    dict_list = []
    chars = num_char(text)

    for key in chars:
        dict_list.append({"char": key, "num": chars[key]})
    
    return sorted(dict_list, reverse=True, key=lambda x: x['num'])