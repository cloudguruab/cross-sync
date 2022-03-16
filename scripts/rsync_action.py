import os
from dotenv import load_dotenv

load_dotenv()

def rsync_push():
    source_dir = input("current directory: ")
    destination_dir = input("destination directory: ")
    return os.system(f"rsync -a ~{source_dir} root@{os.getenv('host')}:{destination_dir}")

def rsync_pull():
    source_dir = input("remote dir: ")
    destination_dir = input("local dir: ")
    return os.system(f"rsync -a root@{os.getenv('host')}:{source_dir} ~{destination_dir}")

def main():
    q = input("Pulling from host [Y/n]: ")
    if q.strip().lower() == "y": rsync_pull()
    else: rsync_push()

if __name__ == "__main__":
    main()