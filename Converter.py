"""
Hebrew Text Converter

This program allows the user to convert Hebrew text to either Phoenician or Samaritan script based on their choice.

Usage:
1. Run the program.
2. Enter the Hebrew text you want to convert.
3. Choose 'P' for Phoenician or 'S' for Samaritan script.
4. View the converted text.
5. Decide whether to end the program or perform another conversion.

Author: [Your Name]
"""


def hebrew_to_phoenician(text):
    """
    Convert Hebrew text to Phoenician script.

    Args:
        text (str): The input Hebrew text.

    Returns:
        str: The converted text in Phoenician script.
    """
    hebrew_to_phoenician_mapping = {
        'א': '𐤀', 'ב': '𐤁', 'ג': '𐤂', 'ד': '𐤃', 'ה': '𐤄',
        'ו': '𐤅', 'ז': '𐤆', 'ח': '𐤇', 'ט': '𐤈', 'י': '𐤉',
        'ך': '𐤊', 'כ': '𐤊', 'ל': '𐤋', 'ם': '𐤌', 'מ': '𐤌',
        'ן': '𐤍', 'נ': '𐤍', 'ס': '𐤎', 'ע': '𐤏', 'ף': '𐤐',
        'פ': '𐤐', 'ץ': '𐤑', 'צ': '𐤑', 'ק': '𐤒', 'ר': '𐤓',
        'ש': '𐤔', 'ת': '𐤕'
    }

    phoenician_text = ''.join(hebrew_to_phoenician_mapping.get(char, char) for char in text)
    return phoenician_text


def hebrew_to_samaritan(text):
    """
    Convert Hebrew text to Samaritan script.

    Args:
        text (str): The input Hebrew text.

    Returns:
        str: The converted text in Samaritan script.
    """
    hebrew_to_samaritan_mapping = {
        'א': '𐡀', 'ב': '𐡁', 'ג': '𐡂', 'ד': '𐡃', 'ה': '𐡄',
        'ו': '𐡅', 'ז': '𐡆', 'ח': '𐡇', 'ט': '𐡈', 'י': '𐡉',
        'ך': '𐡊', 'כ': '𐡊', 'ל': '𐡋', 'ם': '𐡌', 'מ': '𐡌',
        'ן': '𐡍', 'נ': '𐡍', 'ס': '𐡎', 'ע': '𐡏', 'ף': '𐡐',
        'פ': '𐡐', 'ץ': '𐡑', 'צ': '𐡑', 'ק': '𐡒', 'ר': '𐡓',
        'ש': '𐡔', 'ת': '𐡕'
    }

    samaritan_text = ''.join(hebrew_to_samaritan_mapping.get(char, char) for char in text)
    return samaritan_text


def converter():
    """
    The main function of the Converter program.

    Runs the conversion process until the user decides to end the program.
    """
    while True:
        hebrew_text = input("Enter Hebrew text: ")
        conversion_choice = input("Enter 'P' for Phoenician or 'S' for Samaritan: ")

        if conversion_choice.upper() == 'P':
            result = hebrew_to_phoenician(hebrew_text)
        elif conversion_choice.upper() == 'S':
            result = hebrew_to_samaritan(hebrew_text)
        else:
            print("Invalid choice. Please enter 'P' or 'S'.")
            return

        print(f"Converted text: {result}")

        end_program = input("Do you want to end the program? (y/n): ")
        if end_program.lower() == 'y':
            print("Thank you for using the Hebrew Text Converter. 𐤋𐤄𐤕𐤓𐤀𐤅𐤕!")
            break


if __name__ == "__main__":
    converter()
