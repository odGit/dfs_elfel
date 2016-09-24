from PIL import Image
import os

def get_crop_box(w,h):
    qw = w//5
    qh = h//4
    x0 = 0
    y0 = 3 * qh
    x1 = qw
    y1 = 4 * qh
    return (x0,y0,x1,y1)


for root, dirs, file_in_dir in os.walk("./stereoviews_by_peter_elfelt/"):
    for img_file in file_in_dir:
        head, tail = os.path.split(img_file)
        if tail != ".DS_Store" and tail[-3:] != "png":
            img = Image.open(root+img_file)
            w, h = img.size
            crop_img = img.crop(get_crop_box(w,h))
            crop_img.save(root+"number/"+tail[:-4]+".png", "PNG")