import cv2

# global variables
original_image = cv2.imread("dog.jpg")
display_image = original_image.copy()
isSelectingRoi = False
top_left_rect_corner = (None, None)
escape_key = 27
end_process_keys = [escape_key]


def renderRect(coordinates):
    # coordinates - tuple containing ( <top_left_rect_corner>, <bottom_right_rect_corner> )

    global original_image, display_image

    # reset display image
    display_image = original_image.copy()
    # render rect on display image
    cv2.rectangle(display_image, coordinates[0], coordinates[1],
                  (0, 0, 0), thickness=2, lineType=cv2.LINE_AA)


def resetImage():
    global original_image, display_image
    display_image = original_image.copy()


def handleMouse(action, x, y, flags, userdata):
    global isSelectingRoi, top_left_rect_corner

    # reset image
    # start drawing rect
    if action == cv2.EVENT_LBUTTONDOWN:
        isSelectingRoi = True
        top_left_rect_corner = (x, y)
        resetImage()

    # rerender rect on mouse move
    if action == cv2.EVENT_MOUSEMOVE and isSelectingRoi == True:
        renderRect((top_left_rect_corner, (x, y)))

    # stop drawing rect
    # save selected region
    if action == cv2.EVENT_LBUTTONUP:
        isSelectingRoi = False
        top_left_rect_corner = (None, None)


# Setup

# Create a named Window
cv2.namedWindow("Select a new Region of Interest")
# Bind Mouse Callback
cv2.setMouseCallback("Select a new Region of Interest", handleMouse)


while(True):
    # Display the image using imshow
    cv2.imshow("Select a new Region of Interest", display_image)

    # Wait for user to press a key
    key = cv2.waitKey(20)
    if (key in end_process_keys):
        break


# Destroy the window
cv2.destroyAllWindows()
