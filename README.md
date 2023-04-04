# Real-Time Text Detection with Tesseract OCR using OpenCV

This is a Python program that uses the OpenCV and Tesseract libraries to perform real-time text detection and recognition from a live video stream. The program captures frames from the default camera and applies image processing techniques to detect text in the frames. Tesseract OCR is then used to recognize the text, which is displayed on the screen.

## Installation

1. Clone the repository to your local machine:

```
git clone https://github.com/s-maurya00/OCR_on_PC-Tesseract_and_OpenCV
```

2. Install the required libraries using pip:

```
pip install -r requirements.txt
```

3. Install Tesseract OCR on your system. You can download the latest version from the official website: https://github.com/tesseract-ocr/tesseract<br/>
Your may also refer:<br/>
`https://github.com/UB-Mannheim/tesseract/wiki`<br/>
`https://tesseract-ocr.github.io/tessdoc/Installation.html`<br/>
`https://github.com/tesseract-ocr/tesseract`


## Usage

1. Open a terminal or command prompt and navigate to the project directory.
```
cd OCR_on_PC-Tesseract_and_OpenCV
```

2. Run the program using Python:
```
python camera_with_tesseract.py
```

3. The program will open a new window showing the live video stream. Any text detected in the frames will be displayed in the terminal.

4. To quit the program, press 'q' on your keyboard.

## Checking Tesseract Installation

To check if Tesseract OCR is properly installed on your system, you can run the following command in the terminal or command prompt:

```
tesseract --version
```

This should display the version number of Tesseract installed on your system. If the command is not recognized, it means Tesseract is not properly installed or added to the system's PATH environment variable.

## Credits

This program was created by [Sushil Maurya](https://github.com/s-maurya00)