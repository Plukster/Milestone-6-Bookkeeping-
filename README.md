## Milestone Details

### Milestone 1
- Initial setup and equation handling
- Basic project structure implementation

### Milestone 2
- Complete Caesar cipher implementation
- Encryption and decryption functions
- Proper handling of case sensitivity and special characters

### Milestone 3
- Pascal's Triangle generation and display
- Mathematical algorithm implementation
- Visualization of triangle patterns

### Milestone 4
- Trade-offs analysis documentation
- Comparison of different approaches
- Performance and complexity analysis

### Milestone 5
- Ancient, Inc. project implementation
- Business logic and requirements fulfillment
- Complete solution integration


# Quadratic Equations - Milestone 1

## Back to School

This project demonstrates solving quadratic equations with coefficients that may have formatting issues (extra spaces, missing spaces).


### What This Does

The `equations.py` file contains a simple quadratic equation solver that:
- Parses quadratic equations in the format: `ax² + bx + c = 0`
- Extracts coefficients (a, b, c) from the equation string
- Solves using the quadratic formula: `x = (-b ± √(b² - 4ac)) / (2a)`
- Handles both real and complex solutions

### Example Usage

```python
# Simple quadratic equation solver
eq = '4x^2 +4x + (-8) = 0'
# Output:
# a = 4, b = 4, c = -8
# x1 = 1.0
# x2 = -2.0
```

### Requirements

- Python 3.x
- No external dependencies (uses built-in `cmath` module)

### How to Run

```bash
cd milestone_1
python equations.py
```

# Milestone 2 “Secret messages”

## How Caesar Cipher Works
- Each letter in the plaintext is shifted a certain number of places down or up the alphabet
- For example, with a shift of 3: A → D, B → E, C → F, etc.
- When reaching the end of the alphabet, it wraps around (Z → C)

## Requirements
1. Implement encryption function
2. Implement decryption function  
3. Handle both uppercase and lowercase letters
4. Preserve spaces and punctuation
5. Support shift values from 0 to 25

## Usage Examples

### Encryption Examples:
```
encrypt("Hello World!", 3) → "Khoor Zruog!"
encrypt("ABC xyz", 1) → "BCD yza"
encrypt("Secret Message", 13) → "Frperg Zrffntr"
```

### Decryption Examples:
```
decrypt("Khoor Zruog!", 3) → "Hello World!"
decrypt("BCD yza", 1) → "ABC xyz"
decrypt("Frperg Zrffntr", 13) → "Secret Message"
```

## Milestone 3 Pascal's Triangle Generator

A Python implementation of Pascal's Triangle generation with command-line interface. This program creates and displays Pascal's Triangle with customizable number of rows, formatted for clean visual output.

## Features
- Generates Pascal's Triangle up to specified number of rows
- Command-line interface for easy usage
- Proper error handling for invalid inputs
- Centered formatting for aesthetically pleasing display
- Type hints for better code documentation
- Self-contained implementation without external dependencies

## Usage
```bash
python triangle.py 5
```

## Example Output
```
    1    
   1 1   
  1 2 1  
 1 3 3 1 
1 4 6 4 1
```

## Implementation Details
- Uses dynamic programming approach for efficient calculation
- Each row is calculated based on the previous row values
- Handles edge cases and input validation
- Supports any positive integer number of rows
- Includes both basic generation and formatted printing functions

## Milestone 4 “Trade-offs”
# Two Sum Problem Solver

A Python implementation of the classic Two Sum problem with two different approaches. This program finds two numbers in an array that add up to a target value and returns their indices.

## Features
- Two different algorithms for solving the Two Sum problem
- Efficient O(n) time complexity solution using hash set
- Brute force O(n²) time complexity solution for comparison
- Type hints for better code documentation
- Clear output formatting for results
- Self-contained implementation without external dependencies

## Algorithms
1. **Brute Force Approach** (`find_sum`): Uses nested loops to check all pairs
   - Time Complexity: O(n²)
   - Space Complexity: O(1)

2. **Hash Set Approach** (`find_sum_fast`): Uses a hash set for efficient lookup
   - Time Complexity: O(n)
   - Space Complexity: O(n)

## Usage
```python
# Example usage
result = find_sum_fast(5, [1, 2, 3, 4, 5])
print(result)  # Output: (0, 3) or (1, 2)
```

## Example Output
```
find_sum(5, [1, 2, 3, 4, 5]) -> (0, 3) or (1, 2)
find_sum_fast(5, [1, 2, 3, 4, 5]) -> (0, 3) or (1, 2)
```

## Milestone 5 “Ancient, Inc.”

This repository contains a dataset of personal information records with the following fields:
- Name (first and last)
- Date of birth 
- Occupation/Job title
- Date of death (if applicable)

The data includes 100+ records of individuals with various professions including therapists, doctors, engineers, educators, and more. Each record follows a consistent format with comma-separated values.

## Data Format
```
Name,Date of Birth,Occupation,Date of Death
```

## Usage
- Can be used for data analysis projects
- Suitable for CSV parsing exercises
- Good for practicing data cleaning and manipulation
- Useful for database population and testing

## Files Included
- `data.csv` - Main dataset file with all records
- `README.md` - This documentation file

## Technologies Used
- CSV format for data storage
- Command line tools for data processing
- Basic text editing capabilities

---

**Note**: This is a sample dataset for educational purposes only. All names and dates are fictional.
