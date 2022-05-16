import os
import glob

BASE_PATH = os.getcwd()
FOLDER = 'sum'
SUM_FILE_NAME = 'sum.txt'

full_path = os.path.join(BASE_PATH, FOLDER, SUM_FILE_NAME)

dict_ = {}

for filename in glob.glob('*.txt'):
   with open(os.path.join(BASE_PATH, filename), 'r') as file_obj:
      number_lines = file_obj.readlines()
      dict_[len(number_lines)] = filename

with open(full_path, 'w') as file_data:
   for item in sorted(dict_):
      filename = dict_[item]
      with open(os.path.join(BASE_PATH, filename), 'r') as file_obj:
         number_lines = file_obj.readlines()
         file_data.write(f'\n{filename}\n{len(number_lines)}\n')
      with open(os.path.join(BASE_PATH, filename), 'r') as file_obj:
         for content in file_obj:
            file_data.write(content)