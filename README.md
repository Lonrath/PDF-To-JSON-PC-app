# PDF to JSON Converter

This is a Python-based GUI application that converts PDF files into JSON format. The application uses the Tkinter library for the user interface and PyPDF2/PdfPlumber for handling PDF files.

## Features

- Select a PDF file from your computer.
- Convert the content of the PDF into a JSON file.
- Save the JSON file to a location of your choice.
- Each line of the PDF is saved as a separate JSON element.
- Easy-to-use graphical user interface (GUI).
## Installation

1. Clone the repository:
   
   git clone https://github.com/Lonrath/PDF-To-JSON-PC-app.git
   cd pdf-to-json-converter

2. Install the required dependencies:
   
  pip install pdfplumber

3. Run the application:

  python main.py
Usage
  Launch the application by running the main.py file.
  Click on the "Select PDF and Convert" button.
  Choose a PDF file from your computer.
  Select a location to save the resulting JSON file.
  The application will process the PDF and save its content in JSON format.

  
JSON Output Example
  {
    "pdf_content": [
        "First line of the PDF",
        "Second line of the PDF",
        "Third line of the PDF"
    ]
}


Building an Executable File
  
  You can convert the application into a standalone executable file using PyInstaller:

  pyinstaller --onefile --noconsole --icon=app_icon.ico main.py

  The executable file will be located in the dist folder.
