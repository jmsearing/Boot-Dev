
def sort_on(dict):
    return dict["num"]

def letter_count(word_list):
    letter_counts = {}
    total_count = 0
    
    #count the letters ya dingus
    for word in word_list:
        for lttr in word:
            if lttr not in letter_counts:
                letter_counts[lttr] = 0
            letter_counts[lttr] += 1
        total_count += 1

    char_list = []
    #adjust the dict in format "char":a "num":0
    for char, count in letter_counts.items():
            # iterates through each item in the letter_counts dict
            char_dict = {"char": char, "num":count}
            # creates a new dictionary for each character
            char_list.append(char_dict)
            # add the dictionary to the list
            char_list.sort(reverse=True, key=sort_on)

    return char_list, total_count

def print_results(lttr_list):
    for lttr in lttr_list:
        if lttr['char'].isalpha():
            print(f"The {lttr['char']} character was found {lttr['num']} times.")
    pass

def main():
    letter_dict = {}
    total_count = 0    
    
    with open ("books/frankenstein.txt") as f:
        raw = f.read()
    raw = raw.lower()
    words = raw.split()
    
    #Count all of the letters and put them into a list of dicts 
    letter_dict, total_count = letter_count(words)

    #print total count
    print(f"{total_count} words found in document.")

    #print_results of all the alpha characters 
    print_results(letter_dict) 


if __name__ == "__main__":
    main()

