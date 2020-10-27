import shutil

import cv2
from pyzbar import pyzbar
import json
import os
import zipfile

# Opening config file and getting info from it.
with open('config.json') as cfg_file:
    config = json.loads(cfg_file.read())

originals_path = config['originals']
result_path = config['result_path']
working_dir = config['working_dir']
allowed_extensions = config['allowed_ext']
os.chdir(originals_path)
log_file = open(os.path.join(result_path, 'result.log'), 'w')

if not os.path.isdir(working_dir):
    os.makedirs(working_dir)


# Function to decode QR code
def decode_qr(path):
    current_image = cv2.imread(path)
    barcodes = pyzbar.decode(current_image)
    if len(barcodes) == 0:
        return None
    barcodeData = barcodes[0].data.decode("utf-8")
    return barcodeData


def compress_files():
    for directory in os.listdir(working_dir):
        dir_path = os.path.join(working_dir, str(directory))
        if not os.path.isdir(dir_path):
            continue
        zip_path = os.path.join(result_path, "%s.zip" % str(directory))
        zipf = zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED)
        for file in os.listdir(dir_path):
            zipf.write(os.path.join(dir_path, file), file)
        zipf.close()


def process_file(image_path, file_name, cur_qr_data):
    current_working_dir = os.path.join(working_dir, cur_qr_data)
    if not os.path.isdir(current_working_dir):
        os.makedirs(current_working_dir)
    os.replace(image_path, os.path.join(current_working_dir, file_name))


sum = 1
dir_list = os.listdir(originals_path)
for image in os.listdir(originals_path):
    full_image_path = os.path.abspath(image)
    qr_data = None
    if image.split(".")[-1].lower() in allowed_extensions:
        qr_data = decode_qr(full_image_path)
    if qr_data is not None:
        process_file(full_image_path, str(image), qr_data)
    else:
        log_file.write("ERROR : Barcode not found in file %s\n" % image)
    print("processed %d out of %d" % (sum, len(dir_list)))
    sum += 1

print("starting compressing files")
compress_files()

if os.path.isdir(working_dir):
    shutil.rmtree(working_dir, ignore_errors=True)
