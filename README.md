# Hebrew to Phoenician/Samaritan converter
## Overview

The Converter is a simple Python program designed to convert Hebrew text to either Phoenician or Samaritan script. It provides a command-line interface for user interaction, allowing users to input Hebrew text, choose the script for conversion, and view the converted text.

## Wikipedia Reference

#### For a more detailed overview, you can visit: 
   - [Biblical Hebrew orthography](https://en.wikipedia.org/wiki/Biblical_Hebrew_orthography)
   - [Samaritan script](https://en.wikipedia.org/wiki/Samaritan_script)
   - [Samaritan Hebrew](https://en.wikipedia.org/wiki/Samaritan_Hebrew)
   - [Paleo-Hebrew alphabet](https://en.wikipedia.org/wiki/Paleo-Hebrew_alphabet)
   - [Phoenician alphabet](https://en.wikipedia.org/wiki/Phoenician_alphabet)
   - [Hebrew alphabet](https://en.wikipedia.org/wiki/Hebrew_alphabet)

## Usage

1. **Run the Program:**
   - Execute the program in a Python environment.
   **Note:**
   - This program is designed to work only with Hebrew text.

2. **Input Hebrew Text:**
   - Enter the Hebrew text you want to convert when prompted.

3. **Choose Script Conversion:**
   - Select 'P' for Phoenician or 'S' for Samaritan when prompted.

4. **View Converted Text:**
   - The program will display the converted text based on the chosen script.

5. **End Program or Perform Another Conversion:**
   - Decide whether to end the program or perform another conversion.

## Author

This program is authored by yehonatanke.

## Functions

### `hebrew_to_phoenician(text)`

Converts Hebrew text to Phoenician script.

- **Parameters:**
  - `text` (str): The input Hebrew text.

- **Returns:**
  - `str`: The converted text in Phoenician script.

### `hebrew_to_samaritan(text)`

Converts Hebrew text to Samaritan script.

- **Parameters:**
  - `text` (str): The input Hebrew text.

- **Returns:**
  - `str`: The converted text in Samaritan script.

### `converter()`

The main function orchestrating the conversion process.

- **Steps:**
  1. Accepts user input for Hebrew text and script choice.
  2. Invokes the appropriate conversion function.
  3. Displays the converted text.
  4. Prompts the user to end the program or perform another conversion.

## Execution

- The program runs in a loop until the user decides to end it.
- Users may need to modify character mappings for accuracy, as the program relies on simple mappings.

## Note

- This program is designed to work only with Hebrew text.
- This program is intended for personal purposes and may require further development for accurate script conversion.

## Author

yehonataKe
