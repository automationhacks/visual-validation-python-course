import os


def is_file_downloaded(path):
    if os.path.exists(path):
        return True


def remove_file_if_exists(path):
    if os.path.exists(path):
        os.remove(path)


def move_file_to_path(src, dst):
    os.rename(src, dst)
