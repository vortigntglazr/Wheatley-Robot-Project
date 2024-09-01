# eyes.py
import cv2 as cv
import sys
import os


def eyeBase():
    sDir = os.path.dirname(__file__)
    imgName = input("enter image name located in the WheatleyEyes/images directory.\n")
    imagePath = os.path.join(sDir, 'images', imgName)
    img = cv.imread(imagePath)
    if not os.path.isfile(imagePath):
        print(f"{imagePath} does not exist.")
        sys.exit(1)
    if img is None:
        print("image not found in specified directory")
        sys.exit(1)
    cv.imshow("Display Window", img)
    k = cv.waitKey(0)
    if k == ord("s"):
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
