from sys import argv
from os import listdir

from PIL import Image
from numpy import ndarray, uint8

parentPath = argv[0].replace(argv[0].split("\\")[-1], "")
inputs = parentPath + "inputs\\"
outputs = parentPath + "outputs\\"

def reprocessImage(imagePath):
    outputPath = outputs + "Processed " + imagePath.split("\\")[-1]

    # len(image.mode): RGB = 3, RGBA = 4
    image = Image.open(imagePath)
    data = ndarray((image.height, image.width, len(image.mode)), dtype=uint8, buffer=image.tobytes())
    Image.fromarray(data, mode=image.mode).save(outputPath)

    return outputPath

print('''
  ___                                   ____                                                   
 |_ _|_ __ ___   ____  ____  ___ ____  |  _ \ ___ ____  ____ ___   ___ ___  ___ ___  ___  ____ 
  | || '_ ` _ \ / _  |/ _  |/ _ \  __| | |_) / _ \  _ \|  __/ _ \ / __/ _ \/ __/ __|/ _ \|  __|
  | || | | | | | (_| | (_| |  __/ |    |  _ <  __/ |_) | | | (_) | (_|  __/\__ \__ \ (_) | |   
 |___|_| |_| |_|\__,_|\__, |\___|_|    |_| \_\___|  __/|_|  \___/ \___\___||___/___/\___/|_|   
                      |___/                      |_|                Pro Max Plus 6G XDR OLED 8K
''')

input("Press enter to process the folder:\n" + inputs + "\n\nand output its outputs into the folder:\n" + outputs + "\n")

for fileName in listdir(inputs):
    reprocessImage(inputs + fileName)
    print("Processed: " + fileName)

input()
