import cv2
import pytesseract

# Open the camera
cap = cv2.VideoCapture(0)

# Set up the text detection
pytesseract.pytesseract.tesseract_cmd = r'F:\Tesseract install\tesseract.exe'

# '--oem' is used for defining type of OCR engine that tesseract uses. '3' is for using default engine
# '--psm' is for page segmentation model where '6' specifies vertically oriented text. 
# r'--oem 3 --psm 6' here, r if for taking input string in raw format i.e., we don't consider any special characters in the string eg. 'sushil\new' will be interpreted as 'sushil' then new line then 'ew' whereas r'sushil\new' will be interpreted as 'sushil\new' only.
config = r'--oem 3 --psm 6'

try:
    while True:
        # Read the frame from the camera
        ret, frame = cap.read()
        
        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect the text in the grayscale frame
        text = pytesseract.image_to_string(gray, config=config)

        # Display the frame and the detected text
        cv2.imshow('frame', frame)
        print(text)

        # Press 'q' to quit
        if cv2.waitKey(1) == ord('q'):
            break

finally:
    # Release the camera and close the window
    cap.release()
    cv2.destroyAllWindows()
