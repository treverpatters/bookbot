from string import ascii_lowercase as alc
def main():
    global book_path 
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    char_count(text)
    report(text)
    

# retrieves text and puts into string
def get_book_text(path):
    with open(path) as f:
        return f.read()
    
# takes string and breaks words apart based on space
def word_count(contents):
    words = contents.split()
    return len(words)

# counts each of the characters included
def char_count(contents):
    lowered_string = contents.lower()
    global char_totals
    char_totals = {}
    for char in lowered_string:            
        if char in char_totals.keys():         
            char_totals[char] += 1
        else:
            char_totals[char] = 1
    return

def report(contents):
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count(contents)} words found in the document")
    print("")
    #now to loop through char_totals key, sorted by highest to lowest, alphabet only
    sorted_dict = dict(sorted(char_totals.items(), key=lambda item: item[1], reverse=True))
    for i in sorted_dict:
        if i in alc:
            print(f"The '{i}' character was found {sorted_dict[i]} times")
    print("--- End report ---")
    return    

main()