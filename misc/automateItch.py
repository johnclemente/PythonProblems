import os
import zipfile
import re

def get_next_folder_name(base_path):
    # Regex pattern to match folder names like "Build1-1", "Build1-2", etc.
    pattern = re.compile(r"^(\D+)(\d+)-(\d+)$")
    folders = {}

    # Search directories for folder names matching the pattern
    for folder in os.listdir(base_path):
        if os.path.isdir(os.path.join(base_path, folder)):
            match = pattern.match(folder)
            if match:
                base_name, major, minor = match.groups()
                major, minor = int(major), int(minor)
                if base_name not in folders:
                    folders[base_name] = []
                folders[base_name].append((major, minor))

    # Find the folder with the highest major and minor version numbers
    if folders:
        latest_base_name, versions = max(folders.items(), key=lambda x: (max(x[1])))
        major, minor = max(versions)
        next_folder = f"{latest_base_name}{major}-{minor + 1}"
        return next_folder
    else:
        raise ValueError("No suitable folder found matching the expected pattern.")

def compress_folder(folder_path, output_name):
    # Create the zip file
    with zipfile.ZipFile(output_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(folder_path):
            for file in files:
                zipf.write(os.path.join(root, file), arcname=os.path.relpath(os.path.join(root, file), os.path.join(folder_path, '..')))

if __name__ == "__main__":
    base_path = input("Enter the base path where the folders are located: ")
    output_zip_name = input("Enter the name for the output zip file: ")

    try:
        next_folder = get_next_folder_name(base_path)
        folder_to_compress = os.path.join(base_path, next_folder)
        
        # Check if the folder exists, if not, create it
        if not os.path.exists(folder_to_compress):
            os.makedirs(folder_to_compress)
            print(f"Created new folder: {folder_to_compress}")
        else:
            print(f"Folder already exists: {folder_to_compress}")

        output_zip_path = os.path.join(base_path, output_zip_name + '.zip')
        compress_folder(folder_to_compress, output_zip_path)
        print(f"Folder '{folder_to_compress}' has been compressed into '{output_zip_path}'")
    except ValueError as e:
        print(e)
