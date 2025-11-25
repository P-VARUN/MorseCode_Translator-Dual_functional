from core_files.text_to_morse import transmit
from core_files.morse_to_text import morse_to_text

print("Morse Code Translator")
print("1 → Text to Morse (with sound)")
print("2 → Type Morse with SPACEBAR → converts to text")
print("--→ Type 'ex' to exit\n")

while True:
    choice = input("Choose 1 or 2: ").strip()
    
    if choice == "ex":
        print("Bye! 73")
        break
        
    if choice == "1":
        text = input("\nEnter your message: ")
        if text:
            print(f"Sending: {text}")
            transmit(text)
            
    elif choice == "2":
        print("\n" + "="*50)
        print("MORSE KEY MODE ACTIVATED")
        print("="*50)
        print("• Short press SPACE = dit (.)")
        print("• Long press SPACE  = dah (-)")
        print("• Wait 3 seconds = new word")
        print("• Press 'Q' to quit this mode", end="")
        morse_to_text()
        
    else:
        print("Please type 1 or 2")