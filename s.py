import pygame
import random

# Define the dimensions of the window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Define the dimensions of the cards
CARD_WIDTH = 70
CARD_HEIGHT = 100

# Define the colors
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Initialize Pygame
pygame.init()

# Create the window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Solitaire")

# Load the card images
cards = []
for i in range(1, 14):
    for j in range(4):
        cards.append(pygame.image.load(f"cards/{i}_{j}.png"))

# Shuffle the deck
deck = list(range(52))
random.shuffle(deck)

# Create the piles
tableau_piles = [[deck.pop() for _ in range(i + 1)] for i in range(7)]
stock_pile = deck
discard_pile = []

# Define the functions
def draw_card(x, y, card):
    """Draw a card at the given position."""
    window.blit(cards[card], (x, y))

def draw_pile(x, y, pile, selected_card=None):
    """Draw a pile of cards at the given position."""
    for i, card in enumerate(pile):
        if selected_card is not None and i >= selected_card:
            draw_card(x, y + (i - 1) * 20, card)
        else:
            draw_card(x, y + i * 20, card)

def get_selected_card(x, y, pile):
    """Return the index of the selected card in the pile."""
    if len(pile) == 0:
        return None
    elif x >= 0 and x < CARD_WIDTH and y >= (len(pile) - 1) * 20 and y < len(pile) * 20:
        return len(pile) - 1
    else:
        return get_selected_card(x, y, pile[:-1])

# Run the game loop
running = True
selected_pile = None
selected_card = None
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if x >= 10 and x < 10 + CARD_WIDTH and y >= 10 and y < 10 + CARD_HEIGHT:
                if len(stock_pile) > 0:
                    discard_pile.append(stock_pile.pop())
            elif x >= 90 and x < 90 + CARD_WIDTH and y >= 10 and y < 10 + CARD_HEIGHT:
                if len(discard_pile) > 0:
                    stock_pile.extend(discard_pile[::-1])
                    discard_pile.clear()
            elif selected_pile is None:
                for i, pile in enumerate(tableau_piles):
                    if x >= 10 + i * 100 and x < 10 + i * 100 + CARD_WIDTH and y >= 120 and y < 120 + CARD_HEIGHT * len(pile):
                        selected_pile = i
                        selected_card = get_selected_card(x - (10 + i * 100), y - 120, pile)
                        if selected_card is not None:
                            selected_card += 1
                        break
            else:
                if x >= 10:
