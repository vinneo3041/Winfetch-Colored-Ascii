# Winfetch-Colored-Ascii
Python script to color ASCII arts for Winfetch config.ps1

1. Run AsciiGradient.py
2. Insert 1st color RGB values, e.g. *"255, 0, 0"* (Red)
3. Insert 2st color RGB values, e.g. *"0, 255, 0"* (Green)
  * if you want the Ascii Art to have just 1 color, reinsert the same values.
4. Insert the PATH for where the Ascii .txt file is. The file cannot have empty lines before or after it, unless you intended to put that empty space.
5. Insert **'1'** for generating a preview, or **'2'** for generating the Powershell string sequence.
6. When generating the string sequence, put it on the *config.ps1* file, inside the **$CustomAscii = @( ... )**

![image](https://github.com/vinneo3041/Winfetch-Colored-Ascii/assets/56792107/0ef2ab72-2718-40b1-a168-beb1a8518cdb)

![image](https://github.com/vinneo3041/Winfetch-Colored-Ascii/assets/56792107/18fe745b-d54a-4afa-b1ae-02a1f7bc0e8d)


