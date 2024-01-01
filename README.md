<div align="center">
  <img src="https://img.shields.io/badge/language-Python-%233776AB.svg?logo=python">
  <img src="https://custom-icon-badges.demolab.com/github/license/denvercoder1/custom-icon-badges?logo=law">
</div>

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

## License

This program is released under the [MIT License](https://github.com/yehonatanke/AncientHeb_Converter/blob/main/LICENSE). Feel free to use, modify, and distribute the code in accordance with the terms of the license.

## Author

yehonataKe
