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
    