from pathlib import Path
import shutil


# File categories and their extensions
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv"],
    "Music": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Applications": [".exe", ".msi"],
}


def get_category(file_extension):
    """Return the category for a given file extension."""

    for category, extensions in FILE_CATEGORIES.items():
        if file_extension.lower() in extensions:
            return category

    return "Others"


def organize_folder(folder_path):
    """Organize files in the given folder into categories."""

    folder = Path(folder_path)

    if not folder.exists():
        print("The folder does not exist.")
        return

    if not folder.is_dir():
        print("The given path is not a folder.")
        return

    files_moved = 0

    for file in folder.iterdir():

        # Ignore folders
        if file.is_dir():
            continue

        extension = file.suffix

        category = get_category(extension)

        category_folder = folder / category

        # Create category folder if it doesn't exist
        category_folder.mkdir(exist_ok=True)

        destination = category_folder / file.name

        # Avoid overwriting an existing file
        if destination.exists():
            print(f"Skipped: {file.name} (already exists)")
            continue

        shutil.move(str(file), str(destination))

        print(f"Moved: {file.name} -> {category}/")
        files_moved += 1

    print()
    print("Organization complete!")
    print(f"Files moved: {files_moved}")


if __name__ == "__main__":

    folder_path = input("Enter the folder path to organize: ")

    organize_folder(folder_path)
