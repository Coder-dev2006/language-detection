#  Language Detector (Python)
This is a simple Python script that automatically detects the **language** of any text input using the `langdetect` library.  
You can enter text in any language — it will tell you which language it is written in!

---

##  Features
-  Detects over **55+ languages**  
-  Lightweight and fast  
-  Simple command-line interface  
-  Built with pure Python  

---

##  Requirements
Install the required package first:

```bash
pip install langdetect
 Usage
Run the script in your terminal:

bash
Copy code
python language_detector.py
Example:

pgsql
Copy code
Enter any text in any language: Bonjour tout le monde
fr
Another example:

pgsql
Copy code
Enter any text in any language: Salom dunyo
uz
 Project Structure
sql
Copy code
language-detector/
│
├── language_detector.py
└── README.md
 How It Works
The script imports the detect function from langdetect.

It asks the user for input text.

The language code (like en, fr, uz) is returned as output.

 Common Language Codes
Code	Language
en	English
fr	French
uz	Uzbek
ru	Russian
de	German
es	Spanish
ar	Arabic
ja	Japanese
zh	Chinese

 Author
Developed by Coder-dev2006
 Simple yet powerful example of natural language detection in Python.

 License
This project is licensed under the MIT License — free for personal and educational use.
