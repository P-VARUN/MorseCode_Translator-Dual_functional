# Morse Code Translator (Real-Time + Sound)

A **fully functional two-way Morse code translator** built in Python — no external hardware needed.

- Type text → hear and see perfect Morse code with real 650 Hz tone  
- Press and hold **SPACEBAR** like a real Morse key → watch it convert live to letters  
- Professional timing, clean output, beginner-friendly code

Perfect for learning Morse code, or just having fun!

---

### Features

- Real sine-wave sound (650 Hz) using Pygame
- Text → Morse with perfect spacing
- Morse → Text using SPACEBAR as a straight key
- Live visual feedback as you type
- Clean final decoded message
- Press **Q** to quit keyer mode
- Type **ex** to exit

---

### How to Run

1. Clone or download this repo
2. Install requirements:
   ```bash
   pip install pygame keyboard
   ```
3. Run the program
    ```
    main.py
    ```

### How to use

Mode 1 — Text to Morse
Type any message → hear and see it in Morse code!

Mode 2 — SPACEBAR Keyer
Short press SPACE = . (dit)
Long press SPACE = - (dah)
Wait ~3 seconds = new word
Press Q to finish and see decoded text

Try typing:
```Example code:
.... . .-.. .-.. ---   .-- --- .-. .-.. -.. 
output → HELLO WORLD
```
### MOSRSE TRANSLATIONS
```
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
    '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3',
    '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8',
    '----.': '9'

```
Made with ❤️. 
Feel free to work and improve!
