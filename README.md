# PyMorse
Module that can convert text to Morse Code or decode it back to uppercase text.

## How to use:
Simply download and add morse_code_pairs.py and morse_converter.py to your working directory and then import morse_encoder or morse_decoder to your python script and use them. 

## Example code:
```python
from morse_converter import morse_encoder, morse_decoder
import pyinputplus

def main():
    text_to_encode = pyinputplus.inputStr(
        prompt="Please enter the text which you want to be converted into Morse Code:"
    )
    encoded_text = morse_encoder(text_to_encode)
    print(f"Your text after Morse encoding is:\n{encoded_text}")
    print(f"Your original text is:\n{text_to_encode}")
    print(f"And the decoding is:\n{morse_decoder(encoded_text)}")


if __name__ == '__main__':
    main()


```

## Sources:
The Morse Code table has been compiled by combining the resources from the following websites:

[Wikipedia Article About Morse Code](https://en.wikipedia.org/wiki/Morse_code)

[GitHub Repository](https://gist.github.com/mohayonao/094c71af14fe4791c5dd)

[Morse Code Table for Electronics](https://www.electronics-notes.com/articles/ham_radio/morse_code/characters-table-chart.php)
