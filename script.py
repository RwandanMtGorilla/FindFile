import os
import shutil

def copy_files_with_specific_name(src_folder, dst_folder, filename_contains):
    if not os.path.exists(dst_folder):
        os.makedirs(dst_folder)

    for root, dirs, files in os.walk(src_folder):
        for file in files:
            if filename_contains in file and file.endswith(".docx"):
                src_file = os.path.join(root, file)
                dst_file = os.path.join(dst_folder, file)
                shutil.copy(src_file, dst_file)
                print(f"Copied: {src_file} -> {dst_file}")

input_folder = 'input'
output_folder = 'output'
specific_string = '2212190320'

copy_files_with_specific_name(input_folder, output_folder, specific_string)
