#Count the most frequent ASCII character in a string

from collections import Counter


def most_frequent_ascii_char(s):
    ascii_chars = [char for char in s if ord(char) < 128]
    
    count = Counter(ascii_chars)
    
    if count:
        most_common_char, freq = count.most_common(1)[0]
        return most_common_char, freq
    else:
        return None, 0
    
    
if __name__ == "__main__":
    input_string = "aaaabbaacccccc"
    char, freq = most_frequent_ascii_char(input_string)
    print(f"The most frequent ASCII character is '{char}' with {freq} occurrences.")