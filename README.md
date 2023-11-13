# File Organizer

## Overview

This Python script provides a convenient way to organize files in a specified input folder. It categorizes files into subfolders based on their formats, facilitating a more structured storage system. Additionally, it efficiently handles files with unsupported formats, grouping them into a designated "OtherFormats" folder.

## Features

- **Format Categories:** The script classifies files into various format categories, including Photos, Videos, Documents, and RawPhotos, based on their extensions.
- **Customization:** Easily customize the script by modifying the `format_categories` dictionary to include additional formats or create new categories.
- **Efficient Organization:** Subfolders corresponding to each format category are created within the input folder, promoting a neat and organized directory structure.
- **Fallback Folder:** Files with unsupported formats are moved to an "OtherFormats" folder, preventing clutter and ensuring no file is left unorganized.

## Usage

1. Replace `your/local/folder/path` with the actual path to your target folder in the `input_folder` variable at the end of the script.
2. Run the script, and it will automatically organize the files within the specified folder.

## Example

Suppose you have a folder with mixed-format files:

your/local/folder/path
|-- image1.jpg
|-- document.pdf
|-- video.mp4
|-- rawfile.arw
|-- script.py

After running the script, the folder structure will be transformed into:

your/local/folder/path
|-- Photos_image1.jpg
|-- Documents_document.pdf
|-- Videos_video.mp4
|-- RawPhotos_rawfile.arw
|-- OtherFormats_script.py

Now, your files are grouped according to their respective categories for a cleaner and more manageable file system.

## Contributing

- Contributions are welcome! Feel free to open issues, submit feature requests, or create pull requests to enhance the functionality of the script.
