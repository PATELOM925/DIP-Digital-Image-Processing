from PIL import Image
import os

print("Current working directory:", os.getcwd())

def image_quality(input_fp, output_fp, quality):
    image = Image.open(input_fp) 
    image.save(output_fp, quality=quality, optimize=True)

def image_converter(input_fp, output_fp, dpi):
    image = Image.open(input_fp)
    image.save(output_fp, dpi=dpi)

if __name__ == "__main__":
    image_converter(r"/Users/om-college/Library/CloudStorage/OneDrive-pdpu.ac.in/PDEU/DIP-Digital Image Processing/Lab-1/stockWaterfall.jpeg", r"/Users/om-college/Library/CloudStorage/OneDrive-pdpu.ac.in/PDEU/DIP-Digital Image Processing/Lab-1/stockWaterfall.jpegstockWaterfall_dpi.jpeg", dpi=(72, 72))
    image_quality('/Users/om-college/Library/CloudStorage/OneDrive-pdpu.ac.in/PDEU/DIP-Digital Image Processing/Lab-1/stockWaterfall.jpeg','/Users/om-college/Library/CloudStorage/OneDrive-pdpu.ac.in/PDEU/DIP-Digital Image Processing/Lab-1/stockWaterfall.jpegstockWaterfall_compressed.jpeg',quality=10)
