import os


def get_size(struct, result=0):
    for item in os.listdir(struct):
        item_path = os.path.join(struct, item)
        if os.path.isfile(item_path):
            result += os.path.getsize(item_path)
        elif os.path.isdir(item_path):
            result += get_size(item_path)
    return result


dir_path = input('Введите путь до католога: ')

files_count = 0
dirs_count = 0

for obj in os.listdir(dir_path):
    obj_path = os.path.join(dir_path, obj)
    if os.path.isfile(obj_path):
        files_count += 1
    elif os.path.isdir(obj_path):
        dirs_count += 1

print(f'Папок: {dirs_count}')
print(f'Файлов: {files_count}')

folder_size = get_size(dir_path) / 10**6
print(f'Размер папки: {folder_size} Мбайт')