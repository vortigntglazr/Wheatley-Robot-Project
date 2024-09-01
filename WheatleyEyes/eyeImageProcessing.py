# eyeImageProcessing.py
import cv2 as cv
import sys
import os
import requests


# individual run
def eyeBase() -> object:
    sDir = os.path.dirname(__file__)  # defining the subdir
    imgUrl = input("enter url for image\n")
    data = requests.get(imgUrl).content
    subdir = 'images'
    filePath = os.path.join(subdir, 'img.jpg')
    f = open(filePath, 'wb')  # opening the subdir and writing the url image to it
    f.write(data)
    f.close()
    imagePath = os.path.join(sDir, 'images', 'img.jpg')
    img = cv.imread(imagePath)  # reading said url image that was imported to the subdir
    if not os.path.isfile(imagePath):
        print(f"{imagePath} does not exist.")  # debugging
        sys.exit(1)
    if img is None:
        print("image not found in specified directory")
        sys.exit(1)
    cv.imshow("Display Window", img)
    k = cv.waitKey(0)
    if k == ord("s"): # dev testing
        cv.destroyAllWindows()
        secondQ = input("would you like to process another photo? ('yes' or 'no')\n")
        if secondQ == "yes":
            eyeBase()
        else:
            cv.destroyAllWindows()
            print("Goodbye!")
            sys.exit(0)
if __name__ == "__main__":
    eyeBase()

