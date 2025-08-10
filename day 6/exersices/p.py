def is_palindrome(word):
    """
    Checks if a word is a palindrome (case-insensitive).
    """
    word = word.lower()
    return word == word[::-1]


def find_and_save_palindromes(input_file, output_file):
    try:
       
        with open(input_file, 'r') as infile:
            words = infile.readlines()

        palindromes = []

      
        for word in words:
            word = word.strip()  
            if word and is_palindrome(word):
                palindromes.append(word.upper())

      
        with open(output_file, 'w') as outfile:
            for p in palindromes:
                outfile.write(p + '\n')

        print(f"Found {len(palindromes)} palindrome(s). Written to '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Palindrome check completed.")



if __name__ == "__main__":
    input_filename = "input_words.txt"
    output_filename = "palindromes.txt"
    find_and_save_palindromes(input_filename, output_filename)
