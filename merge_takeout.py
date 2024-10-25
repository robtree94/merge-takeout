import os
import shutil
import logging
import time

def merge_and_organize(source_folder, destination_folder, total_files):
    total_copied = 0
    start_time = time.time()

    logging.info(f"Starting to process {source_folder}")

    try:
        for root, dirs, files in os.walk(source_folder):
            for file in files:
                source_path = os.path.join(root, file)
                relative_path = os.path.relpath(source_path, source_folder)
                destination_path = os.path.join(destination_folder, relative_path)

                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                logging.info(f"Copying {source_path} to {destination_path}")

                shutil.copy2(source_path, destination_path)
                total_copied += 1
                percentage_complete = (total_copied / total_files) * 100
                elapsed_time = time.time() - start_time
                estimated_remaining_time = (elapsed_time / total_copied) * (total_files - total_copied)
                logging.info(f"Progress: {percentage_complete:.2f}% | Elapsed Time: {elapsed_time:.2f}s | Estimated Remaining Time: {estimated_remaining_time:.2f}s")

    except Exception as e:
        logging.error(f"Error processing {source_path}: {e}")

    end_time = time.time()
    total_time = end_time - start_time
    logging.info(f"Finished processing {source_folder} in {total_time:.2f} seconds.")

def main():
    logging.basicConfig(filename='merge_log.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

    source_folders = [
        "F:\\Takeout 1",
        "F:\\Takeout 2",
        "F:\\Takeout 3",
        "F:\\Takeout 4",
        "F:\\Takeout 5"
    ]
    destination_folder = "F:\\Merged Takeout"

    os.makedirs(destination_folder, exist_ok=True)

    total_files = 0
    for source_folder in source_folders:
        if os.path.exists(source_folder):
            for root, dirs, files in os.walk(source_folder):
                total_files += len(files)
        else:
            logging.warning(f"Source folder not found: {source_folder}")

    logging.info("Starting the merging and organizing process...")
    logging.info(f"Total files to process: {total_files}")

    for source_folder in source_folders:
        merge_and_organize(source_folder, destination_folder, total_files)

if __name__ == "__main__":
    main()
