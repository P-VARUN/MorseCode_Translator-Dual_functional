import keyboard
import time
from core_files.morse_data import REV_MORSE

def morse_to_text():
    current_code = ""
    final_code = []
    last_time = time.time()
    print("Start pressing spacebar | 'q' to exit")
    print("Live.Morse: ", end="", )

    while True:
        now = time.time()
        
        if keyboard.is_pressed('space'):
            start = time.time()
            while keyboard.is_pressed('space'):
                time.sleep(0.01)
            duration = time.time() - start
            if duration < 0.3:
                current_code += "."
                print(".", end="", flush=True)
                final_code.append(".")
            elif duration > 0.3:
                current_code += "-"
                print("-", end="", flush=True)
                final_code.append("-")
            last_time = time.time()
        else:
            if now-last_time > 3.0:
                final_code.append("  ")
                print("  ", end="", flush=True)
                last_time=now

        if keyboard.is_pressed('q'):
            print("\n Final result: ")
            print("".join(final_code))
            print("→ " + "".join(REV_MORSE.get(code.strip(), "?") for code in "".join(final_code).split("  ")))
            print("\nBack to menu!")
            break

        time.sleep(0.01)