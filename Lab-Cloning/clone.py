import cv2
import os

def main():
    source ="source1.png"
    dest ="destination1.png"
    mask_image ="mask.png"
     
    source = cv2.imread(source, cv2.IMREAD_COLOR)
    destination = cv2.imread(dest, cv2.IMREAD_COLOR)
    mask = cv2.imread(mask_image, cv2.IMREAD_COLOR)

    if source is None:
        print("Could not load source image", source)
        exit(0)
    if destination is None:
        print("Could not load destination image", dest)
        exit(0)
    if mask is None:
        print("Could not load mask image", mask_image)
        exit(0)

    result = cv2.seamlessClone(source, destination, mask, (400, 100), cv2.MONOCHROME_TRANSFER)
    # result2 = cv2.seamlessClone(source, destination, mask, (400, 100), cv2.MIXED_CLONE)
    # result3 = cv2.seamlessClone(source, destination, mask, (400, 100), cv2.NORMAL_CLONE)

    cv2.imshow("Output", result)
    path = "ClonedImages/"
    os.makedirs(path, exist_ok=True)  # Create the directory if it doesn't exist

    cv2.imwrite(path + "cloned_monochrome.png", result)
    # cv2.imwrite("cloned_mixed.png", result2)
    # cv2.imwrite("cloned.png", result3)
    cv2.waitKey(0)

if __name__ == "__main__":
    main()
