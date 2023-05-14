import pandas as pd
import requests
import os

def get_column_from_csv(file_path, column_name, new_file_path):
  """
    THIS FUNCTION IS USED TO GET A COLUMN FROM A CSV FILE AND SAVE IT TO .TXT FILE
    file_path: path to .csv file (string)
    column_name: name of column (string)
    new_file_path: path to new .txt file (string)
  """
  df = pd.read_csv(file_path)
  df[column_name].to_csv(new_file_path, index=False, header=False)
  filename = new_file_path.split('/')[-1]
  print(f'File saved to: {filename}')

def download_images(file_path, output_folder):
  """
    THIS FUNCTION IS USED TO DOWNLOAD IMAGES FROM A .TXT FILE
    file_path: path to .txt file (string)
    output_folder: path to output folder (string)
  """
  with open(file_path) as f:
    urls = f.readlines()
  urls = [url.strip() for url in urls]
  for url in urls:
    filename = url.split('/')[-1]
    r = requests.get(url, allow_redirects=True)
    open(f'{output_folder}/{filename}', 'wb').write(r.content)
  print(f'All images downloaded to: {output_folder}')

def get_filenames_in_folder(folder_path):
  """
    THIS FUNCTION IS USED TO GET ALL FILENAMES IN A FOLDER
    folder_path: path to folder (string)
  """
  filenames = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
  return filenames