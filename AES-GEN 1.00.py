import secrets, sys

RED = "\033[31m"
BLUE = "\033[34m"
BLACK = "\033[30m"
RESET = "\033[0m"

ASCII_ART = (
    "█████╗ ███████╗███████╗       ██████╗ ███████╗███╗   ██╗\n"
    "██╔══██╗██╔════╝██╔════╝      ██╔════╝ ██╔════╝████╗  ██║\n"
    "███████║█████╗  ███████╗█████╗██║  ███╗█████╗  ██╔██╗ ██║\n"
    "██╔══██║██╔══╝  ╚════██║╚════╝██║   ██║██╔══╝  ██║╚██╗██║\n"
    "██║  ██║███████╗███████║      ╚██████╔╝███████╗██║ ╚████║\n"
    "╚═╝  ╚═╝╚══════╝╚══════╝       ╚═════╝ ╚══════╝╚═╝  ╚═══╝"
)
BANNER_WIDTH = len(ASCII_ART.split("\n", 1)[0])

ROUNDS_MAP = {128: 10, 192: 12, 256: 14}
MENU_MAP = {"1": 128, "2": 192, "3": 256}

def banner():
    title = "A E S   K E Y   G E N E R A T O R"
    version = "Version 1.00"
    spacing = BANNER_WIDTH - len(title) - len(version)
    sys.stdout.write(
        f"{RED}{ASCII_ART}{RESET}\n"
        f"{BLUE}{title}{' ' * spacing}{RED}{version}{RESET}\n"
        f"{BLACK}By Joshua M Clatney – Ethical Pentesting Enthusiast{RESET}\n\n"
    )

def generate_hex_keys(count, bits):
    tokhex = secrets.token_hex
    return [tokhex(bits // 8).upper() for _ in range(count)]

def main():
    while True:
        banner()
        sys.stdout.write(
            "Select the key size (Enter to exit):\n"
            "1. 128-bit\n2. 192-bit\n3. 256-bit\nChoice: "
        )
        choice = input().strip()
        if choice == "":
            break
        size = MENU_MAP.get(choice)
        if size is None:
            sys.stdout.write("Invalid choice. Try again.\n\n")
            continue
        rounds = ROUNDS_MAP[size]
        sys.stdout.write(f"\nAES-{size} will use {rounds} rounds.\n\n")
        while True:
            try:
                num = int(input("Select how many keys to generate (1-1000): ").strip())
                if 1 <= num <= 1000:
                    break
                raise ValueError
            except ValueError:
                sys.stdout.write("Invalid number. Try again.\n")
        for idx, hexkey in enumerate(generate_hex_keys(num, size), 1):
            sys.stdout.write(f"{idx}: {hexkey}\n")
        input("\nPress Enter to return to main menu…")
    input("\nPress Enter to close…")

if __name__ == "__main__":
    main()