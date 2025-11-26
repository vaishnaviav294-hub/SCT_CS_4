# SCT_CS_4
Overview:

This project is a safe and educational key‑input logger built using Python. It records only the keys that the user types inside the program’s own terminal window. The logged keys are saved to a text file, helping beginners understand keyboard event handling without creating harmful system‑wide keyloggers.

 Features:

*Logs only user‑typed keys in the program
*Saves keystrokes to a file
*Press ESC to stop logging
*Simple and beginner‑friendly
*Safe for learning and legal to use

How to Run on Kali Linux:

Install pynput:
pip3 install pynput

Create the script:
nano safe_key_input_logger.py

Paste the code into the file and save.

Run the script:
python3 safe_key_input_logger.py


Type inside the terminal.
Press ESC to stop.

View the log:
cat key_input_log.txt

Requirements:

Python 3
pynput library
