import os
import shutil


def rename_files(source_dir, destination_dir):
    file_list = os.listdir(source_dir)
    file_list.sort()

    name = input("Enter the desired file name: ")


    starting_number = int(input("Enter the starting number for renaming: "))

    for index, file_name in enumerate(file_list):
        
        file_ext = os.path.splitext(file_name)[1]
      
        new_file_name = f"{name}_{starting_number + index:02d}{file_ext}"

        source_path = os.path.join(source_dir, file_name)
        destination_path = os.path.join(destination_dir, new_file_name)

        shutil.move(source_path, destination_path)

    print("Files renamed successfully!")


source_directory = "/path/to/source/directory"
destination_directory = "/path/to/destination/directory"

rename_files(source_directory, destination_directory)
