import sys
import sort
import shutil
import normalize
from pathlib import Path

def handle_file(path, root_folder, dist):
    target_folder = root_folder/dist
    target_folder.mkdir(exist_ok=True)
    path.replace(target_folder/normalize.normalize(path.name))

def handle_archive(path, root_folder, dist):
    target_folder = root_folder/dist
    target_folder.mkdir(exist_ok=True)

    new_name = normalize.normalize(path.name.replace(".zip", '').replace(".gz", '').replace(".tar", ''))

    archive_folder = target_folder/new_name
    archive_folder.mkdir(exist_ok=True)

    try:
        shutil.unpack_archive(str(path.resolve()), str(archive_folder.resolve()))
    except shutil.ReadError:
        archive_folder.rmdir()
        return
    except FileNotFoundError:
        archive_folder.rmdir()
        return
    path.unlink()


def remove_empty_folders(path):
    for item in path.iterdir():
        if item.is_dir():
            remove_empty_folders(item)
            try:
                item.rmdir()
            except OSError:
                pass

def get_files_list(path):
    files_list = list()
    if path.exists():        
        for item in path.iterdir():
            files_list.append(item.name)

    return files_list

def main(folder_path):
    print(folder_path)
    sort.sort(folder_path)

    for file in sort.images:
        handle_file(file, folder_path, "images")

    for file in sort.documents:
        handle_file(file, folder_path, "documents")

    for file in sort.audio:
        handle_file(file, folder_path, "audio")

    for file in sort.video:
        handle_file(file, folder_path, "video")

    for file in sort.others:
        handle_file(file, folder_path, "others")

    for file in sort.archives:
        handle_archive(file, folder_path, "archives")

    remove_empty_folders(folder_path)

    result_file_path = folder_path/'FilesList.txt'
    with open(result_file_path, 'w') as fw:
        fw.write(f"All extensions: {sort.registered_extensions}\n")
        fw.write(f"Unknown extensions: {sort.unknown_extensions}\n")
        fw.write(f"images: {get_files_list(folder_path/'images')}\n")
        fw.write(f"documents: {get_files_list(folder_path/'documents')}\n")
        fw.write(f"audio: {get_files_list(folder_path/'audio')}\n")
        fw.write(f"video: {get_files_list(folder_path/'video')}\n")
        fw.write(f"archive: {get_files_list(folder_path/'archives')}\n")
        fw.write(f"others: {get_files_list(folder_path/'others')}\n")
        

if __name__ == '__main__':
    path = sys.argv[1]
    #path = 'Temporary'

    folder = Path(path)
    main(folder.resolve())