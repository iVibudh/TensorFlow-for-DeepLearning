```
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
```

# Blackjack Game

Welcome to the Blackjack game implementation in Python. This project simulates a simplified version of the popular card game Blackjack, also known as 21.

## Blackjack House Rules

1. The deck is unlimited in size.
2. There are no jokers.
3. The Jack/Queen/King all count as 10.
4. The Ace can count as 11 or 1.
5. The cards in the deck have equal probability of being drawn.
6. Cards are not removed from the deck as they are drawn.

## Gameplay
- At the start, the user and the computer are each dealt two cards.
- The user is then prompted to either draw another card ('y') or pass ('n').
- The goal is to get a score as close to 21 as possible without exceeding it.
- The computer will automatically draw cards until its score is at least 17.
- The game ends, and the winner is determined based on the final scores.

## Functions
- deal_card(): Returns a random card from the deck.
- calculate_score(cards): Takes a list of cards and returns the total score, considering the rules.
- compare(user_score, computer_score): Compares the user and computer scores and determines the winner.