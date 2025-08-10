def analyze_log_file(log_file="server.log", report_file="report.txt"):
 
    status_counts = {
        '200': 0,
        '404': 0,
        '500': 0
    }

    try:
        with open(log_file, 'r') as file:
            for line in file:
                try:
                    parts = line.strip().split()
                    if len(parts) < 3:
                        raise ValueError("Malformed log line")
                    
                    status_code = parts[1]
                    if status_code in status_counts:
                        status_counts[status_code] += 1
                except Exception as e:
                    print(f"Warning: Skipping malformed line -> {line.strip()}")

        with open(report_file, 'w') as report:
            report.write("HTTP Status Code Summary:\n")
            report.write(f"Successful (200): {status_counts['200']}\n")
            report.write(f"Not Found (404): {status_counts['404']}\n")
            report.write(f"Server Error (500): {status_counts['500']}\n")

        print(f"Analysis complete. Report written to '{report_file}'.")

    except FileNotFoundError:
        print(f"Error: Log file '{log_file}' not found.")
    except Exception as e:
        print(f"Unexpected error: {e}")



if __name__ == "__main__":
    analyze_log_file()
