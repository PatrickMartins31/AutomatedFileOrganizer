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

