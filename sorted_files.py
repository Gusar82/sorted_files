import os


def find_files_txt(dir_files: str) -> dict:
    """создает словарь, где ключ имя файла (только txt)"""
    files = dict()
    for file in os.listdir(dir_files):
        #  if file.split('.')[-1] == 'txt':
        if file.endswith('.txt'):
            files[file] ={}
    return files


def count_line_file(file_path):
    with open(file_path, 'r', encoding='utf8') as file:
        text = file.read()
        len_text = text.strip().count('\n')+1
        return len_text, text


def sort_files_lines(dir_files: str) -> dict:
    """сортировка файлов, где ключ - имя файла, значение - кортеж количество строк в файле и техт"""
    files = find_files_txt(dir_files)
    for file_key in files.keys():
        file_path = os.path.join(dir_files, file_key)
        files[file_key] = count_line_file(file_path)
    return dict(sorted(files.items(), key=lambda i: i[1]))


def add_text_in_file(new_file_path: str, files_text: dict):
    with open(new_file_path, 'w', encoding='utf8') as file:
        for name_file, (len_text, text) in files_text.items():
            if file.tell() > 0:
                file.write('\n')
            file.write(f"{name_file}\n")
            file.write(f"{str(len_text)}\n")
            file.write(text.strip())


base_path = os.getcwd()
files_dir = 'sorted'
union_file = 'union.txt'

dir_path = os.path.join(base_path, files_dir)
union_file_path = os.path.join(base_path, union_file)

files_txt = sort_files_lines(dir_path)
add_text_in_file(union_file_path, files_txt)







