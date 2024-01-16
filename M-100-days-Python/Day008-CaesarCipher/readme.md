# Caesar Cipher Encoder/Decoder

This Python program implements a simple Caesar Cipher to encode and decode messages. The Caesar Cipher is a substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet.

## Features

- **Encryption:** Type 'encode' to encrypt a message.
- **Decryption:** Type 'decode' to decrypt a message.
- **Shift:** Enter the shift number to determine the degree of encryption/decryption.
- **Alphabet Handling:** The program handles input messages containing numbers, symbols, and spaces without altering them during encoding/decoding.
- **Modulus Operation:** If the user enters a shift number greater than 26, the program uses the modulus operator to ensure it remains within the range of the alphabet.
- **Restart Option:** After encoding or decoding a message, the user can choose to restart the program for another operation.

## Usage

1. Run the program using the `main.py` file.
2. The program will display a logo and prompt the user to choose between encoding or decoding.
3. Enter the message to be encrypted or decrypted.
4. Input the shift number to determine the cipher shift.
5. If the user wants to perform another operation, they can type 'yes' when prompted. Otherwise, type 'no' to exit the program.

## Example

```bash
$ python main.py
# [Program Logo]
Type 'encode' to encrypt, type 'decode' to decrypt:
encode
Type your message:
hello world
Type the shift number:
3
Here's the encoded result: khoor zruog
Type 'yes' if you want to go again. Otherwise type 'no'.
yes
Type 'encode' to encrypt, type 'decode' to decrypt:
decode
Type your message:
khoor zruog
Type the shift number:
3
Here's the decoded result: hello world
Type 'yes' if you want to go again. Otherwise type 'no'.
no
Goodbye
