import pandas as pd
from config import (
  DATA_FOLDER_PATH
)
import json

def generate_metadata_file(images_list, data_file):
  """
    THIS FUNCTION IS USED TO GENERATE METADATA FILE
    images_list: list of images (list)
    data_file: path to data file (string) with extension
  """
  dataframe = pd.read_csv(f'{DATA_FOLDER_PATH}/{data_file}')
  df_filtered = dataframe[dataframe['link'].str.contains('|'.join(images_list))]
  data = {}

  for index, row in df_filtered.iterrows():
    # Get the image name without the extension
    image_name_without_ext = row['link'].split('/')[-1].split('.')[0]
    # Add the data to the JSON object
    data[image_name_without_ext] = {
      'image': f"images/{image_name_without_ext}.jpg",
      'conditioning_image': f"output/{image_name_without_ext}.jpg",
      'caption': row['caption'],
    }
  json_data = json.dumps(data, indent=2)

  # Print the JSON string
  print(json_data)
  with open(f'{DATA_FOLDER_PATH}/metadata.json', 'w') as file:
    json.dump(data, file, indent=2)
  print('File saved to: metadata.json')