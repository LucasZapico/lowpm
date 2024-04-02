from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
from utils.config import load_config, check_and_create_project_dir

config = load_config()

def on_modified(event):
    if event.src_path.endswith('.md'):
        print(f'Markdown file {event.src_path} has been modified')

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

watch_directory(config['project_dir'])