from PIL import Image, ImageChops
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


class Img:
    """represents an image and basic manipulations"""

    def __init__(self, path):
        self.path = path
        self.img = Image.open(path)

    def rotate_img(self, degrees):
        return self.img.rotate(degrees, expand=1)

    def show(self):
        img = mpimg.imread(self.path)
        imgplot = plt.imshow(img)

    def save(self, path, height: int = 300, quality=95):
        ratio = height / self.img.size[0]
        sizes = tuple([int(ratio * sz) for sz in self.img.size])

        self.img = self.img.resize(sizes, Image.ANTIALIAS)
        self.img.save(path, optimize=True, quality=quality)

    def trim_boarder(self) -> Image:
        """crop any single color boarder from an image"""
        bg = Image.new(self.img.mode, self.img.size, self.img.getpixel((0, 0)))
        diff = ImageChops.difference(self.img, bg)
        diff = ImageChops.add(diff, diff, 2.0, -100)
        bbox = diff.getbbox()
        if bbox:
            return self.img.crop(bbox)
        return self.img
