from morse_code_pairs import morse_table, morse_reverse_table
import pyinputplus

# Color for printing the error message
CRED = '\033[91m'
CEND = '\033[0m'


def word2morse_encoder(word):
    """Converts word to morse code. The word is not case sensitive"""
    try:
        encoded_list = [morse_table[char] for char in word.lower()]
    except KeyError as err:
        print(CRED + f"'{word}' contains and invalid character." + CEND)
        print(CRED + repr(err) + CEND)
        raise err
    return " ".join(encoded_list)


def morse_word_decoder(word):
    """Decodes a word of morse code. The result is uppercase."""
    try:
        decoded_list = [morse_reverse_table[char] for char in word.split(" ")]
    except KeyError as err:
        print(CRED + f"'{word}' contains and invalid key." + CEND)
        print(CRED + repr(err) + CEND)
        raise err

    return "".join(decoded_list).upper()


def morse_encoder(text):
    """Converts word to morse code. The word is not case sensitive"""
    encoded_list = [word2morse_encoder(word) for word in text.split()]
    return "|".join(encoded_list)


def morse_decoder(encoded_text):
    """Converts text back from Morse Code. It is not case sensitive."""
    encoded_word_list = encoded_text.split('|')
    decoded_word_list = [morse_word_decoder(word) for word in encoded_word_list]
    return " ".join(decoded_word_list)


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
