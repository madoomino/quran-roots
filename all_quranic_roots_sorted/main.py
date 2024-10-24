import re
import json

# Function to extract roots from the file content
def extract_roots(file_content):
    # Regular expression to match the root pattern
    root_pattern = re.compile(r'ROOT:([^\|]+)\|')
    roots = []

    # Loop through each line in the file content
    for line in file_content.splitlines():
        try:
            # Check for matching root
            match = root_pattern.search(line)
            if match:
                root = match.group(1)
                roots.append(root)
        except Exception as e:
            print(f"Error processing line: {line}, Error: {e}")

    return roots

# Function to count and sort roots
def sort_roots(roots):
    # Count the occurrences of each root
    root_count = {}
    for root in roots:
        if root in root_count:
            root_count[root] += 1
        else:
            root_count[root] = 1

    # Sort roots by frequency (descending)
    sorted_roots = sorted(root_count.items(), key=lambda x: x[1], reverse=True)

    return sorted_roots

# Function to format and save sorted roots to a JSON file
def save_to_json(sorted_roots, filename='sorted_roots.json'):
    formatted_roots = [{"root_order": count, "root_word": root} for root, count in sorted_roots]

    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(formatted_roots, json_file, ensure_ascii=False, indent=4)

# Main script
if __name__ == "__main__":
    # Read the file content
    try:
        with open('quranic-corpus.txt', 'r', encoding='utf-8') as file:
            file_content = file.read()
    except FileNotFoundError:
        print("File not found. Please ensure the file exists.")
        exit(1)

    # Extract and sort roots
    roots = extract_roots(file_content)

    if roots:
        sorted_roots = sort_roots(roots)

        # Save the sorted roots to a JSON file
        save_to_json(sorted_roots)
        print("Sorted roots have been saved to 'sorted_roots.json'.")
    else:
        print("No roots were found in the file.")
