from utils import (
  get_column_from_csv,
  download_images,
  get_filenames_in_folder,
  execute_sam,
  generate_metadata_file
)
from config import (
  get_file_path,
  FILES_FOLDER_PATH,
  IMAGES_FOLDER_PATH,
  OUTPUT_FOLDER_PATH
)

FILENAME = 'out.csv'
FILE_PATH = get_file_path(FILENAME)

NEW_FILE_NAME = 'LIST.txt'
NEW_FILE_PATH = f"{FILES_FOLDER_PATH}/{NEW_FILE_NAME}"

get_column_from_csv(FILE_PATH, 'link', NEW_FILE_PATH)
download_images(NEW_FILE_PATH, IMAGES_FOLDER_PATH)

ALL_IMAGES = get_filenames_in_folder(FILES_FOLDER_PATH)
execute_sam(ALL_IMAGES)

GENERATED_OUTPUTS = get_filenames_in_folder(OUTPUT_FOLDER_PATH)

generate_metadata_file(GENERATED_OUTPUTS, FILENAME)