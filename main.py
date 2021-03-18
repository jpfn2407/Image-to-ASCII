import sys
import getopt
from PIL import Image

grayscale = {
    '0': " ",  # 0 - 26
    '1': ".",  # 27 - 53
    '2': ":",  # 54 - 80
    '3': "-",  # 81 - 107
    '4': "=",  # 108 - 134
    '5': "+",  # 135 - 161
    '6': "*",  # 162 - 188
    '7': "#",  # 189 - 215
    '8': "%",  # 216 - 242
    '9': "@"  # 243 - 255
}


def to_gray_scale(r, g, b):
    gray_value = int((r + g + b) / 3)
    if 0 <= gray_value <= 26:
        return grayscale['0']
    elif 27 <= gray_value <= 53:
        return grayscale['1']
    elif 54 <= gray_value <= 80:
        return grayscale['2']
    elif 81 <= gray_value <= 107:
        return grayscale['3']
    elif 108 <= gray_value <= 134:
        return grayscale['4']
    elif 135 <= gray_value <= 161:
        return grayscale['5']
    elif 162 <= gray_value <= 188:
        return grayscale['6']
    elif 189 <= gray_value <= 215:
        return grayscale['7']
    elif 216 <= gray_value <= 242:
        return grayscale['8']
    else:
        return grayscale['9']


def main(argv):
    wsize = 50
    try:
        opts, args = getopt.getopt(argv, "hi:s:", ["ifile=", "size="])
    except getopt.GetoptError:
        print
        'main.py -i <inputfile> '
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('main.py -s <width size> -i <inputfile>')
            sys.exit()
        elif opt in ("-s", "--size"):
            wsize = int(arg)
        elif opt in ("-i", "--ifile"):
            image_path = arg
            get_image(image_path, wsize)
        else:
            print('Invalid parameters. Check "py main.py -h" for valid parameters.')


def get_image(image_path, wsize):
    img = Image.open(image_path)
    hsize = int((float(img.size[1]) * wsize) / (float(img.size[0]) * 1.33))
    img = img.resize((wsize, hsize), Image.ANTIALIAS)
    rgb_img = img.convert('RGB')
    for y in range(hsize):
        print("")
        for x in range(wsize):
            r, g, b = rgb_img.getpixel((x, y))
            print(to_gray_scale(r, g, b), end="")


if __name__ == '__main__':
    main(sys.argv[1:])
