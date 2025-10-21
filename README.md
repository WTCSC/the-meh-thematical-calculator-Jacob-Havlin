# The Meh-thematical Calculator

## Overview
The Meh-thematical Calculator is a Python-based command-line application that performs basic and intermediate mathematical operations. Users can input two numbers and then choose which function to apply. Each arithmetic function — including addition, subtraction, multiplication, division, and exponents — is manually implemented for educational purposes, showcasing Python logic and control flow without relying on built-in arithmetic shortcuts.

## Features
- Perform basic arithmetic operations:
  - **Addition (`+`)**
  - **Subtraction (`-`)**
  - **Multiplication (`*`)**
  - **Division (`/`)**
  - **Exponents (`**`)**
- Input validation ensures only numeric entries are accepted.
- Clear, text-based user interface.
- All operations are handwritten using Python logic.
- Designed as a learning tool to explore function structure and input handling.

## How It Works
1. The program prompts the user to enter two numbers.
2. The user selects one of the available operations (`+`, `-`, `*`, `/`, `**`).
3. The program computes the result using its internal logic.
4. The result is displayed, and the user can perform another calculation or exit.

### Example Interaction


Enter your first number: 6
Enter your second number: 3
Choose an operation (+, -, *, /, **): **
The result is: 216



## Project Structure

the-meh-thematical-calculator/
├── calculator.py        # Main program file with handwritten arithmetic functions
├── tests/               # Unit tests for verifying correct calculations
└── README.md            # Project documentation (this file)



## Installation
1. Clone the repository:
   git clone https://github.com/WTCSC/the-meh-thematical-calculator-Jacob-Havlin.git

2. Navigate into the project directory:
   cd the-meh-thematical-calculator-Jacob-Havlin
   
3. Run the calculator:
   python3 calculator.py
  
> No external dependencies are required — this project runs on standard Python 3.

## Testing

Unit tests are included to ensure each operation produces the correct result.

To run tests:
    pytest

## License

This project is licensed under the MIT License.

## Author

Jacob Havlin
