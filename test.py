# from transformers import LayoutXLMTokenizer

# tokenizer = LayoutXLMTokenizer.from_pretrained('microsoft/layoutxlm-base')

import logging
# logging.root.setLevel(logging.DEBUG)
# logging.basicConfig(level=logging.DEBUG)
from pdf2image import convert_from_path
from PIL import Image
from pathlib import Path
sample_path = Path("./syuwa-nihongo-daijiten/OCM-Promotion/shuwa-nihongo-daijiten-p96.pdf")
assert sample_path.exists()
# images = convert_from_path(sample_path)

full_path = Path("syuwa-nihongo-daijiten/SYUWA-NIHONGO DAIJITEN.pdf")
assert full_path.exists()

images = convert_from_path(full_path)
for image in images:
    print(f"{image.width} x {image.height}")
