import os
from dotenv import load_dotenv

load_dotenv()

def rsync_push():
    source_dir = input("current directory: ")
    destination_dir = input("destination directory: ")
    return os.system(f"rsync -a ~{source_dir} {os.getenv('username')}@{os.getenv('host')}:{destination_dir}")

def rsync_pull():
    source_dir = input("remote dir: ")
    destination_dir = input("local dir: ")
    return os.system(f"rsync -a {os.getenv('username')}@{os.getenv('host')}:{source_dir} ~{destination_dir}")

if __name__ == "__main__":
    rsync_pull()