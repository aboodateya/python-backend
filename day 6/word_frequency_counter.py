def process_file(input_file, output_file):
    try:
        with open(input_file, 'r') as infile:
            content = infile.read()

        processed_content = content.upper()

        with open(output_file, 'w') as outfile:
            outfile.write(processed_content)

        print(f"Content from '{input_file}' processed and written to '{output_file}' successfully.")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Finished processing file.\n")



def word_frequency_counter(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()

        words = text.lower().split()
        word_freq = {}

        for word in words:
            word = word.strip('.,!?;:"()[]{}\'')
            if word:
                word_freq[word] = word_freq.get(word, 0) + 1

        print(f"Word frequencies in '{filename}':\n")
        for word, freq in sorted(word_freq.items()):
            print(f"{word}: {freq}")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("\nWord frequency analysis complete.")

if __name__ == "__main__":
 
    input_filename = "input.txt"
    output_filename = "output.txt"

    process_file(input_filename, output_filename)
    word_frequency_counter(input_filename)
