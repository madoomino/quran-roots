# import json
# import os
# from collections import defaultdict

# # Directory containing the JSON files
# directory = '.'

# # Dictionary to store the combined data
# combined_data = defaultdict(int)

# # Loop through surah numbers from 1 to 114
# for surah_number in range(1, 115):
#     # Generate the JSON file name
#     json_file_name = f'surah_{str(surah_number).zfill(3)}.json'
#     json_file_path = os.path.join(directory, json_file_name)
    
#     # Check if the file exists
#     if os.path.exists(json_file_path):
#         # Read the JSON file
#         with open(json_file_path, 'r', encoding='utf-8') as json_file:
#             data = json.load(json_file)
#             # Combine the data
#             for item in data:
#                 root_word = item['root_word']
#                 occurrences = item['occurrences']
#                 combined_data[root_word] += occurrences

# # Convert the combined data to a list of dictionaries
# combined_data_list = [{'root_word': k, 'occurrences': v} for k, v in combined_data.items()]

# # Sort the combined data by the Arabic alphabet
# combined_data_list = sorted(combined_data_list, key=lambda x: x['root_word'])

# # Add the "root_order" field
# for index, item in enumerate(combined_data_list):
#     item['root_order'] = index + 1

# # Write the combined data to a new JSON file
# with open('combined_data.json', 'w', encoding='utf-8') as json_file:
#     json.dump(combined_data_list, json_file, ensure_ascii=False, indent=4)

# print("Data successfully written to 'combined_data.json'")


import json
import os
from collections import defaultdict

# Directory containing the JSON files
directory = '.'

# Dictionary to store the combined data
combined_data = defaultdict(int)

# Loop through surah numbers from 1 to 114
for surah_number in range(1, 115):
    # Generate the JSON file name
    json_file_name = f'surah_{str(surah_number).zfill(3)}.json'
    json_file_path = os.path.join(directory, json_file_name)
    
    # Check if the file exists
    if os.path.exists(json_file_path):
        # Read the JSON file
        with open(json_file_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            # Combine the data
            for item in data:
                root_word = item['root_word'].strip()
                occurrences = item['occurrences']
                if root_word:  # Ignore empty root words
                    combined_data[root_word] += occurrences

# Convert the combined data to a list of dictionaries
combined_data_list = [{'root_word': k, 'occurrences': v} for k, v in combined_data.items()]

# Sort the combined data by the Arabic alphabet
combined_data_list = sorted(combined_data_list, key=lambda x: x['root_word'])

# Add the "root_order" field
for index, item in enumerate(combined_data_list):
    item['root_order'] = index + 1

# Write the combined data to a new JSON file
with open('combined_data.json', 'w', encoding='utf-8') as json_file:
    json.dump(combined_data_list, json_file, ensure_ascii=False, indent=4)

print("Data successfully written to 'combined_data.json'")