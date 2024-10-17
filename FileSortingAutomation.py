import os
import sys
import logging
import shutil
import time
from watchdog.observers import Observer   
from watchdog.events import LoggingEventHandler

source_dir = "P:/Downloads"
dest_dir_pdf = "P:/Downloads/Download PDF"
dest_dir_img = "P:/Downloads/Download Images"
dest_dir_office = "P:/Downloads/Download Word_PP_Excel"


def make_unique(dest, name):
    filename, extension = os.path.splitext(name)
    counter = 1

    while os.path.exists(f"{dest}/{name}"):
        name = f"{filename}({str(counter)}){extension}"
        counter += 1

    return name


def move(dest, entry, name):
    file_exists = os.path.exists(os.path.join(dest, name))
    if file_exists:
        unique_name = make_unique(dest, name)
        oldName = os.path.join(dest, name)
        newName = os.path.join(dest, unique_name)
        os.rename(oldName, newName)
    shutil.move(entry, dest)

class MoverHandler(LoggingEventHandler):
    def on_modified(self, event):
        with os.scandir(source_dir) as entries:
            for entry in entries:
                name = entry.name
                dest = source_dir
                if name.endswith('.pdf'):
                    dest = dest_dir_pdf
                    move(dest, entry, name)
                elif name.endswith('.jpg') or name.endswith('.jpeg') or name.endswith('.png'):
                    dest = dest_dir_img
                    move(dest, entry, name)
                elif name.endswith('.pptx') or name.endswith('.ppt') or name.endswith('.docx') or name.endswith('.doc') or name.endswith('.xlsx'):
                    dest = dest_dir_office
                    move(dest, entry, name)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = source_dir
    event_handler = MoverHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
