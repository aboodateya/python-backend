def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32


def convert_temperatures(input_file, output_file):
    try:
        with open(input_file, 'r') as infile:
            lines = infile.readlines()

        converted_lines = []

        for line in lines:
            line = line.strip()
            if not line:
                continue  
            try:
                celsius = float(line)
                fahrenheit = celsius_to_fahrenheit(celsius)
                formatted_line = f"{celsius:.2f}C = {fahrenheit:.2f}F"
                converted_lines.append(formatted_line)
            except ValueError:
                print(f"Warning: Skipping non-numeric data -> '{line}'")

        with open(output_file, 'w') as outfile:
            for entry in converted_lines:
                outfile.write(entry + '\n')

        print(f"Successfully converted {len(converted_lines)} temperature(s).")
        print(f"Results written to '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Temperature conversion completed.")



if __name__ == "__main__":
    input_filename = "celsius.txt"
    output_filename = "fahrenheit.txt"
    convert_temperatures(input_filename, output_filename)
