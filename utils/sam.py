# Importing libraries
import numpy as np
import torch
import matplotlib.pyplot as plt
from segment_anything import SamAutomaticMaskGenerator, sam_model_registry
import supervision as sv
from PIL import Image
import numpy as np
from config import (
  MODELS_FOLDER_PATH,
  OUTPUT_FOLDER_PATH,
  IMAGES_FOLDER_PATH
)
import os

def show_anns(anns):
  if len(anns) == 0:
    return
  sorted_anns = sorted(anns, key=(lambda x: x['area']), reverse=True)
  ax = plt.gca()
  ax.set_autoscale_on(False)

  img = np.ones((sorted_anns[0]['segmentation'].shape[0], sorted_anns[0]['segmentation'].shape[1], 4))
  img[:,:,3] = 0
  for ann in sorted_anns:
    m = ann['segmentation']
    color_mask = np.concatenate([np.random.random(3), [0.35]])
    img[m] = color_mask
  ax.imshow(img)

def execute_sam(images_list):
  sam_checkpoint = f"{MODELS_FOLDER_PATH}/sam_vit_h_4b8939.pth"
  model_type = "vit_h"
  DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
  sam = sam_model_registry[model_type](checkpoint=sam_checkpoint).to(device=DEVICE)

  for image_name in images_list:
    # check if image is already segmented
    if os.path.isfile(f'{OUTPUT_FOLDER_PATH}/{image_name}'):
      continue
    else:
      with Image.open(f'{IMAGES_FOLDER_PATH}/{image_name}') as image:
        image_np = np.array(image)
        mask_generator = SamAutomaticMaskGenerator(sam)
        masks = mask_generator.generate(image_np)

        mask_annotator = sv.MaskAnnotator()
        detections = sv.Detections.from_sam(sam_result=masks)
        new_image = mask_annotator.annotate(scene=image_np.copy(), detections=detections)

        new_image_pil = Image.fromarray((new_image * 255).astype(np.uint8)) 
        new_image_pil.save(f'{OUTPUT_FOLDER_PATH}/{image_name}')
  print("All images segmented")