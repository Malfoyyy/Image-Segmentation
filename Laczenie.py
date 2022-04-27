from PIL import Image
import formic
def Lacz(root):
    fileset = formic.FileSet(root)
    images = [Image.open(x) for x in fileset]
    box = (120, 0, 260, 384)
    widths, heights = zip(*(i.crop(box).size for i in images))
    total_width = sum(widths)
    max_height = max(heights)
    new_im = Image.new('RGB', (total_width, max_height))
    x_offset = 0
    for im in images:
        new_image = im.crop(box)
        new_im.paste(new_image, (x_offset, 0))
        x_offset += new_image.size[0]
    new_im.save('test.jpg')