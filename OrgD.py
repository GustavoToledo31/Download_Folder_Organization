import os
import re
import shutil
import sys

# To select the path you should run de file in that form: python OrgD.py "Your Path"
# Path Example: E:\gusta\Downloads
path = sys.argv[1]

file_folder_mapping = {
    '.png': 'images',
    '.jpg': 'images',
    '.jpeg': 'images',
    '.gif': 'images',
    '.pdf': 'pdf_word_ppt',
    '.mp4': 'videos',
    '.mp3': 'audio',
    '.doc': 'pdf_word_ppt',
    '.ipynb': 'code',
    '.py': 'code',
    '.zip': 'others',
    '.xlsx': 'excel',
    '.ppt': 'pdf_word_ppt',
    '.exe': 'others',
    '.xls': 'excel',
    'xlsm': 'excel',
    'docx': 'pdf_word_ppt'
}

files = os.listdir(path)

for file in files:
    try:
        files = os.listdir(path)

        # Searching for the file type
        if re.search('.', file, re.IGNORECASE):
            file_type = f'.{file.split(".")[-1]}'

            # If the file type is in the file_folder_mapping:
            if file_type in file_folder_mapping:
                # Choosing the folder to insert the file
                folder_to_enter = file_folder_mapping[file_type]
                # Creating the paths
                old_path = os.path.join(path, file)
                new_path = os.path.join(path, folder_to_enter, file)

                # Looking if the folder already exists
                print(folder_to_enter in files)
                if folder_to_enter not in files:
                    # Creating the folder
                    print(folder_to_enter)
                    os.mkdir(os.path.join(path, folder_to_enter))

                # Insert the file in the folder
                shutil.move(old_path, new_path)
                print(
                    f'The {file} was moved to {folder_to_enter} folder with sucess!')
            else:
                # Criar a pasta arquivos não classificável/reconhecido ou Insere o arquivo na pasta
                folder_name = "not_classified"
                old_path = os.path.join(path, file)
                new_path = new_path = os.path.join(path, folder_name, file)

                if folder_name not in files:
                    os.mkdir(os.path.join(path, folder_name))

                # Inserir o arquivo na pasta
                shutil.move(old_path, new_path)
                print(
                    f'The {file} was moved to {folder_name} folder with sucess!')
    except:
        print("Error during the organization")
