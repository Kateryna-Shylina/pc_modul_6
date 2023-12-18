import sys
from pathlib import Path

images = list()
documents = list()
audio = list()
video = list()
folders = list()
archives = list()
others = list()
unknown_extensions = set()
registered_extensions = set()

main_folders = {
    'images': [images, ['JPEG', 'PNG', 'JPG', 'SVG']],
    'documents': [documents, ['DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX']],
    'audio': [audio, ['MP3', 'OGG', 'WAV', 'AMR']],
    'video': [video, ['AVI', 'MP4', 'MOV', 'MKV']],
    'archives': [archives, ['ZIP', 'GZ', 'TAR']],
    'folders': [folders],    
    'others': [others] 
}

def get_extensions(file_name):
    return Path(file_name).suffix[1:].upper()

def sort(folder):
    for item in folder.iterdir():
        if item.is_dir():
            if item.name not in ('images', 'documents',  'audio', 'video', 'folders', 'archives', 'others'):
                folders.append(item)
                sort(item)
            continue

        extension = get_extensions(file_name=item.name)
        new_name = folder/item.name
        if not extension:
            others.append(new_name)
        else:
            container = None
            for key, value in main_folders.items():
                if key not in ('folders', 'others'):
                    for ext in value[1]:                        
                        if extension == ext:
                            container = value[0]
                            break
                    if container != None:
                        registered_extensions.add(extension)
                        container.append(new_name)
                        break                
            else:
                unknown_extensions.add(extension)
                others.append(new_name)               





"""
if __name__ == '__main__':
    path = 'Temporary'
    print(f"Start in {path}")

    folder = Path(path)
    sort(folder)

    print(f"images: {images}")
    print(f"documents: {documents}")
    print(f"audio: {audio}")
    print(f"video: {video}")
    print(f"archive: {archives}")
    print(f"others: {others}")
    print(f"unkown: {others}")
    print(f"All extensions: {registered_extensions}")
    print(f"Unknown extensions: {unknown_extensions}")
    print(f"Folder: {folders}")
"""
