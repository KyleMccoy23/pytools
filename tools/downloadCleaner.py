

import shutil
import os

source_path = "C:\\Users\\kylem\\Downloads"
application_path = "C:\\Users\\kylem\\OneDrive\\Documents\\Sorted Downloads\\Applications"
pdf_path = "C:\\Users\\kylem\\OneDrive\\Documents\\Sorted Downloads\\pdf"
document_path = "C:\\Users\\kylem\\OneDrive\\Documents\\Sorted Downloads\\documents"
archive_path = "C:\\Users\\kylem\\OneDrive\\Documents\\Sorted Downloads\\archives"
misc_path = "C:\\Users\\kylem\\OneDrive\\Documents\\Sorted Downloads\\Misc"
image_path = "C:\\Users\\kylem\\OneDrive\\Documents\\Sorted Downloads\\images"

def main():
    for i in os.scandir(source_path):
        if ".exe" in i.name or ".msi" in i.name:
            shutil.move(i.path, application_path)
        if ".pdf" in i.name:
            shutil.move(i.path, pdf_path)
        if ".docx" in i.name:
            shutil.move(i.path, document_path)
        if '.zip' in i.name:
            shutil.move(i.path, archive_path)
        if '.png' in i.name or '.webp' in i.name or '.jpg' in i.name or '.jpeg' in i.name :
            shutil.move(i.path, image_path)
        else:
            shutil.move(i.path, misc_path)