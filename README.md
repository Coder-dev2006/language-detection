🧠 Language Detector (Python)

A simple yet enhanced Python tool that automatically detects the language of any text using the langdetect
 library.
You can input a single text or scan an entire file — the program will identify each language detected!

✨ Features

✅ Detects over 55+ languages
✅ Supports single text or file input
✅ Can export results to JSON or CSV
✅ Command-line interface with flexible arguments
✅ Lightweight, fast, and beginner-friendly
✅ Built entirely with pure Python

⚙️ Installation

Install the required dependency:

pip install langdetect


Clone this repository (if you haven’t yet):

git clone https://github.com/<your-username>/language-detection.git
cd language-detection

🚀 Usage
🧾 Option 1: Single text detection

Run from terminal:

python main.py -t "Bonjour tout le monde"


Output:

Detected: fr / French — top: fr(0.9999)

📂 Option 2: Detect languages in a text file

Create a file named texts.txt:

Hello world
Привет мир
Salom dunyo
Hola mundo


Then run:

python main.py -f texts.txt --csv results.csv


Output example:

Detected 4 lines, exported to results.csv ✅

🛠️ Command-line arguments
Argument	Description	Example
-t, --text	Analyze a single text string	-t "Hello world"
-f, --file	Analyze a file with multiple lines	-f texts.txt
--json	Save detection results in JSON format	--json result.json
--csv	Save detection results in CSV format	--csv result.csv
--top	Show top N detected languages	--top 3
-v	Verbose mode (debug info)	-v
📂 Project Structure
language-detection/
│
├── main.py
├── README.md
├── requirements.txt   # optional
└── texts.txt          # sample input

⚡ How It Works

Imports the detect() function from the langdetect library.

Takes either user input or file input.

Detects the dominant language(s).

Displays results or saves them in JSON/CSV.

🌍 Common Language Codes
Code	Language	Code	Language
en	English	fr	French
uz	Uzbek	ru	Russian
de	German	es	Spanish
ar	Arabic	ja	Japanese
zh	Chinese	it	Italian
🧩 Future Improvements

✅ Add translation feature (via googletrans)

✅ Add GUI (Tkinter) interface for easy use

✅ Support batch file processing

✅ Improve accuracy metrics and confidence score output

🤝 Contributing

Want to add new features?

Fork this repository

Create a new branch

git checkout -b feature/my-feature


Commit your changes

git commit -m "Add: new detection improvement"


Push and create a Pull Request 🚀

👨‍💻 Author

Developed with ❤️ by Coder-dev2006

Simple yet powerful example of natural language detection in Python.

📄 License

This project is licensed under the MIT License — free for personal and educational use!!!
