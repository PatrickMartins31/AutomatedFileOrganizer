# AutomatedFileOrganizer

This project automates the organization of files in your Downloads folder, automatically moving them to specific subfolders based on their file type. It uses the **Watchdog** library to monitor your Downloads folder and sorts files like PDFs, images, and office documents into designated folders in real-time.

## Features

- **Automated File Sorting:** Files in your Downloads folder are automatically moved to the appropriate subfolders:
  - **PDFs** go to `Download PDF`
  - **Images** (JPG, JPEG, PNG) go to `Download Images`
  - **Office Documents** (Word, PowerPoint, Excel) go to `Download Word_PP_Excel`
- **Real-Time Monitoring:** The script continuously monitors the Downloads folder and moves files as soon as they are downloaded or modified.
- **Duplicate Handling:** If a file with the same name already exists in the target folder, the script will automatically rename the new file with a unique name.

## Folder Structure

- `source_dir` (Watched Folder):
  - `P:/Downloads`
- Destination Folders:
  - `P:/Downloads/Download PDF` - For PDF files
  - `P:/Downloads/Download Images` - For image files (JPG, PNG, etc.)
  - `P:/Downloads/Download Word_PP_Excel` - For Word, PowerPoint, and Excel documents

# How It Works

- The script uses Python’s **watchdog** library to monitor changes in the Downloads folder.
- Whenever a file is added or modified, the script checks its extension and moves it to the appropriate folder.
- If a file with the same name already exists in the target folder, the script ensures that the new file is renamed with a unique identifier to prevent overwriting.

## Example

1. Download a PDF file in your Downloads folder, and it will automatically be moved to **Download PDF**.
2. Download an image (e.g., `photo.jpg`), and it will be moved to **Download Images**.
3. Download a PowerPoint presentation or Word document, and it will be moved to **Download Word_PP_Excel**.

## Dependencies

- Python 3.x
- Watchdog
