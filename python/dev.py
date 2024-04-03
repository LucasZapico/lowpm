from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import time
import subprocess

def on_modified(event):
    print(f'event type: {event.event_type}  path : {event.src_path}')
    if event.src_path.endswith('.py'):
        print('Python file changed, restarting app.')
        subprocess.run(['pipenv', 'run', 'python3', 'watchers.py'])

if __name__ == "__main__":
    event_handler = FileSystemEventHandler()
    event_handler.on_modified = on_modified

    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()