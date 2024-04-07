from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
from utils.config import load_config, check_and_create_project_dir
from utils.colorized_util import console
from handlers.main_handler import handle_change
from utils.logger import logger
from app import config
from utils.colorized_util import console

def on_modified(event):
    if event.src_path.endswith(".md"):
        logger.info(f"Markdown file {event.src_path} has been modified")
        console.print(f"Markdown file {event.src_path} has been modified")
        handle_change(event.src_path)


def watch_directory(path):
    event_handler = FileSystemEventHandler()
    event_handler.on_modified = on_modified
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
    console.print("Watching for changes in the project directory...")


