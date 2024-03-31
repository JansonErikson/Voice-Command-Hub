import threading
from stt_module import listen
from dialog_manager import process_command

def main():
    while True:
        text = listen()
        if text:
            thread = threading.Thread(target=process_command, args=(text,))
            thread.start()

if __name__ == "__main__":
    main()