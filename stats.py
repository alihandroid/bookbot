def get_num_words(s):
    return len(s.split())

def get_char_counts(s):
    char_counts = {}
    for c in s:
        c = c.lower()
        if c in char_counts:
            char_counts[c] += 1
        else:
            char_counts[c] = 1
    return char_counts

def sort_char_counts(char_counts):
    def sort_on(d):
        return d["count"]
        
    char_counts_list = [{"name": c, "count": char_counts[c]} for c in char_counts]
    char_counts_list.sort(reverse=True, key=sort_on)
    
    result = {}
    for tuple in char_counts_list:
        result[tuple["name"]] = tuple["count"]
        
    return result