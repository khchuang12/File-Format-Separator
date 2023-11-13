import os
import shutil

def organize_files(input_folder):
    # Create a dictionary of format categories and their corresponding formats
    format_categories = {
        "Photos": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".raw"],
        "Videos": [".mp4", ".avi", ".mkv", ".mov", ".flv", ".wmv", ".png"],
        "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx", ".csv"],
        "RawPhotos": [".arw", ".cr2", ".nef", ".dng"]
    }

    # Create folders for each format category inside the input folder
    for category, formats in format_categories.items():
        folder_name = f"{os.path.basename(input_folder)}_{category}"
        folder_path = os.path.join(input_folder, folder_name)
        os.makedirs(folder_path, exist_ok=True)

    # Create a folder for files with formats not covered by the categories
    other_format_folder = os.path.join(input_folder, "OtherFormats")

    # Traverse the input folder and move files to their respective folders or "OtherFormats"
    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)

        # Check if the item is a file
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1].lower()
            moved = False

            # Iterate through each category and check if the file has a matching format
            for category, formats in format_categories.items():
                if file_extension in formats:
                    folder_name = f"{os.path.basename(input_folder)}_{category}"
                    # Move the file to the corresponding folder
                    shutil.move(file_path, os.path.join(input_folder, folder_name, filename))
                    moved = True
                    break

            # If the file doesn't match any format category, move it to "OtherFormats"
            if not moved:
                shutil.move(file_path, os.path.join(other_format_folder, filename))

if __name__ == '__main__':
    # Replace with the path to your input folder
    input_folder = r'your/local/folder/path'
    organize_files(input_folder)
