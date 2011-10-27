#!/usr/bin/env python
#
# This is for libanki 1.2.9+
# See libanki/tests/test_deck.py for inspiration

import sys
import re
import unicode_support_checker
from anki import DeckStorage
from anki.stdmodels import BasicModel

if __name__ != '__main__' or len(sys.argv) < 3:
    sys.exit("Usage: "+sys.argv[0]+" '<deck path>' '<card front>' '<card back>'");

# Mung arguments
deck_file   = sys.argv[1];
card_front  = sys.argv[2];
card_back   = sys.argv[3];
# todo Not even this works. It refuses to embed the newlines in the Card
card_back = re.sub(r"\\n", "\n", card_back);

# Fetch Deck, careful not to make a new one
print("Get Deck '"+deck_file+"'");
deck = DeckStorage.Deck( deck_file );
deck.addModel( BasicModel() );

# todo I don't see any other ways to prevent creating a new Deck file
if deck.cardCount == 0:
    sys.exit("ERROR: Deck '"+deck_file+"' does not exist.");

print("Deck has "+str(deck.cardCount)+"/"+str(deck.factCount)+" cards/facts");

# Build the card
print("Make a new Card for: "+card_front);
fact            = deck.newFact();
fact['Front']   = card_front.decode('utf-8');
fact['Back']    = card_back.decode('utf-8');

# Add Card to the Deck
# todo Using .decode('utf-8'), I no longer get 'duplicate card' errors :p
try:
    deck.addFact( fact );
except Exception, e:
    if hasattr(e, "data"):
        sys.exit("ERROR: Could not add '"+e.data['field']+"': "+e.data['type']);
    else:
        sys.exit(e);

# Done.
print("Save the Deck");
deck.save();
deck.close();
