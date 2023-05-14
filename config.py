import os

# FOR DATA
DATA_FOLDER_PATH = os.path.join(os.path.dirname(__file__), 'data')
get_file_path = lambda filename: os.path.join(DATA_FOLDER_PATH, filename)

# FOR FILES
FILES_FOLDER_PATH = os.path.join(os.path.dirname(__file__), 'files')

# FOR OUTPUT
OUTPUT_FOLDER_PATH = os.path.join(os.path.dirname(__file__), 'output')

# FOR IMAGES
IMAGES_FOLDER_PATH = os.path.join(os.path.dirname(__file__), 'images')

# FOR MODELS
MODELS_FOLDER_PATH = os.path.join(os.path.dirname(__file__), 'models')