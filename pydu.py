import os
import sys

def get_dir_size(start_path):
    total_dir_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if not os.path.islink(fp): #пропускаем симлинки
                total_dir_size += os.path.getsize(fp)
    return total_dir_size

def format_size(size_in):
    for val in ['B', 'KB', 'MB', 'GB', 'TB', 'PB']:
        if size_in < 1024: break
        else: size_in /= 1024
    if val == 'B': return "{}{}".format(size_in, val)  #для байтов не нужно оставлять 2 знака после запятой
    else: return "{:.2f}{}".format(size_in, val)

if len(sys.argv) <= 1:
    cwd = os.getcwd()
else:
    cwd = sys.argv[1]
    if not os.path.isdir(cwd):
        print("{} is not directory".format(cwd))
        exit(1)

items = os.listdir(cwd)
item_list = []
total_size=0

for item in items:
    item_full_name = os.path.join(cwd, item)
    if os.path.isdir(item_full_name):
        dir_size = get_dir_size(item_full_name)
        total_size += dir_size
        item_list.append((dir_size, item+"/"))

    else:
        file_size = os.path.getsize(item_full_name)
        total_size += file_size
        item_list.append((file_size, item))

item_list.sort(key=lambda size: size[0], reverse=True)

for size, name in item_list:
    print("{:<10}{:<12}".format(format_size(size),name))

print("Total {}".format(format_size(total_size)))