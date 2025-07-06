# AES Key Generator

## Overview

This script generates cryptographically secure random AES (Advanced Encryption Standard) keys of sizes 128-bit, 192-bit, and 256-bit. It is designed for ethical penetration testing, security analysis, and cryptographic purposes.

## Features

* Interactive command-line interface (CLI) and Graphical User Interface (GUI).
* Generates cryptographically secure random AES keys.
* Supports AES key lengths of 128-bit, 192-bit, and 256-bit.
* Displays the number of rounds used in AES encryption for the selected key size:

  * 128-bit: 10 rounds
  * 192-bit: 12 rounds
  * 256-bit: 14 rounds

## Technical Details

* Utilizes Python's built-in `secrets` module to generate secure random keys.
* ANSI escape sequences provide colored terminal output for enhanced readability.

## Requirements

* Python 3.x

## Usage

### Execution

Run the script directly from the terminal or download the repository.

### Interactive Menu

Upon execution, the script provides an interactive menu:

```
Select the key size (Enter to exit):
1. 128-bit
2. 192-bit
3. 256-bit
Choice:
```

* Select the desired AES key size by entering `1`, `2`, or `3`.
* After selecting the key size, specify the number of keys to generate (between 1 and 1000).
* Generated keys are displayed with an index for easy identification.

### Exiting

* Press `Enter` without typing any choice to exit the program from the main menu.
* After generating keys, press `Enter` to return to the main menu, or press `Enter` again from the main menu to close the script.

## Example Output

```
AES-128 will use 10 rounds.

Select how many keys to generate (1-1000): 3
1: 5A1F2B8D3C4E6F708192A0BCD123EF45
2: 1BCD2E3F456789AB01CDEF23456789AB
3: ABCD1234567890EFEDCBA09876543210

Press Enter to return to main menu…
```

### Author Information

**Joshua M Clatney (Clats97)**

Ethical Pentesting Enthusiast

Copyright © 2024-2025 Joshua M Clatney (Clats97) All Rights Reserved

### Disclaimer

**DISCLAIMER: This project comes with no warranty, express or implied. The author is not responsible for abuse, misuse, or vulnerabilities. Please use responsibly and ethically in accordance with relevant laws, regulations, legislation and best practices.**
