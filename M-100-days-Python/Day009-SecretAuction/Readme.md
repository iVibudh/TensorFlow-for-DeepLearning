# Silent Auction Bidding System

This Python program simulates a silent auction bidding system, where users can place bids for an item without knowing the bids of other participants. The program will determine the winner and the highest bid once the auction is complete.

## Features

- **Bidding:** Users can enter their name and bid amount for the auctioned item.
- **Anonymous Bidding:** Bids are kept secret, and participants do not know the bids of others.
- **Winner Determination:** The program finds and announces the winner with the highest bid after the auction ends.
- **Interactive Interface:** The program uses the `replit` library to create an interactive and clear console interface.
- **Logo Display:** The program starts by displaying a logo using the `art` library.

## Usage

1. Run the program using the `main.py` file.
2. The program will display a logo and prompt the user to enter their name and bid.
3. Users can continue to place bids by typing 'yes' when asked if there are any other bidders.
4. To end the auction, type 'no' when prompted.
5. The program will then announce the winner and the highest bid.

## Example

```bash
$ python main.py
# [Program Logo]
What is your name?: Alice
What is your bid?: $150
Are there any other bidders? Type 'yes' or 'no'.
yes
[Screen Clears]
# [Program Logo]
What is your name?: Bob
What is your bid?: $200
Are there any other bidders? Type 'yes' or 'no'.
no
The winner is Bob with a bid of $200
