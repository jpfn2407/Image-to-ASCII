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
    if 0 == gray_value:
        return grayscale['0']
    elif 1 <= gray_value <= 29:
        return grayscale['1']
    elif 30 <= gray_value <= 58:
        return grayscale['2']
    elif 59 <= gray_value <= 87:
        return grayscale['3']
    elif 88 <= gray_value <= 114:
        return grayscale['4']
    elif 115 <= gray_value <= 141:
        return grayscale['5']
    elif 142 <= gray_value <= 168:
        return grayscale['6']
    elif 169 <= gray_value <= 195:
        return grayscale['7']
    elif 196 <= gray_value <= 222:
        return grayscale['8']
    else:
        return grayscale['9']


def main(argv):
    wsize = 50
    try:
        opts, args = getopt.getopt(argv, "hi:s:", ["ifile=", "size="])
    except getopt.GetoptError:
        print('main.py -i <inputfile> ')
        sys.exit(2)
    if not opts:
        print('Invalid parameters. Check "py main.py -h" for more information.')
    else:
        for opt, arg in opts:
            print(arg)
            if opt == '-h':
                print('main.py -s <output_width_size> -i <inputfile>')
                sys.exit()
            elif opt in ("-s", "--size"):
                wsize = int(arg.strip())
            elif opt in ("-i", "--ifile"):
                image_path = arg
                get_image(image_path, wsize)
            else:
                print('Invalid parameters. Check "py main.py -h" for more information.')
                sys.exit()


def get_image(image_path, wsize):
    img = Image.open(image_path)
    hsize = int((float(img.size[1]) * wsize) / (float(img.size[0]) * 1.5))
    img = img.resize((wsize, hsize), Image.ANTIALIAS)
    rgb_img = img.convert('RGB')
    for y in range(hsize):
        print("")
        for x in range(wsize):
            r, g, b = rgb_img.getpixel((x, y))
            print(to_gray_scale(r, g, b), end="")


if __name__ == '__main__':
    main(sys.argv[1:])
