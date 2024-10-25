import os
import shutil

# Dynamic path setting based on the script's location
base_path = os.path.dirname(os.path.abspath(__file__))
source_base = os.path.join(base_path, 'Takeout')
destination_folder = os.path.join(base_path, 'Merged_Takeout')

# Ensure the destination folder exists
os.makedirs(destination_folder, exist_ok=True)

# Merge files from all source folders to the destination folder
for i in range(1, 7):
    source_folder = os.path.join(source_base, f'Takeout{i}')
    
    # Walk through each file in the source folder
    for root, _, files in os.walk(source_folder):
        for file in files:
            # Full path to the source file
            source_path = os.path.join(root, file)
            
            # Determine the relative path for merging the file structure
            relative_path = os.path.relpath(source_path, source_folder)
            destination_path = os.path.join(destination_folder, relative_path)
            
            # Ensure any subdirectories in the relative path exist in the destination
            os.makedirs(os.path.dirname(destination_path), exist_ok=True)
            
            # Move file if it doesn't already exist in the destination folder
            if not os.path.exists(destination_path):
                shutil.move(source_path, destination_path)

# Function to get total file count and size in a directory
def get_folder_stats(path):
    total_files = 0
    total_size = 0
    for root, _, files in os.walk(path):
        total_files += len(files)
        total_size += sum(os.path.getsize(os.path.join(root, file)) for file in files)
    return total_files, total_size

# Calculate source folder totals
total_source_files = 0
total_source_size = 0
for i in range(1, 7):
    source_folder = os.path.join(source_base, f'Takeout{i}')
    files, size = get_folder_stats(source_folder)
    total_source_files += files
    total_source_size += size

# Calculate destination folder totals
merged_files, merged_size = get_folder_stats(destination_folder)

# Output results for validation
print(f"Total files in source: {total_source_files}, Total size in source: {total_source_size} bytes")
print(f"Total files in merged: {merged_files}, Total size in merged: {merged_size} bytes")

# Check if file counts and sizes match
if total_source_files == merged_files and total_source_size == merged_size:
    print("Validation successful: All files have been merged correctly!")
else:
    print("Validation failed: The merged folder does not match the source folders.")
