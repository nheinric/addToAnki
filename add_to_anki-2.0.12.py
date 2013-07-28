#!/usr/bin/env python
# This is for libanki 2.0.12
# See libanki/tests/*

import sys, re, unicode_support_checker
from anki import Collection as aopen

if __name__ != '__main__' or len(sys.argv) < 5:
    sys.exit("Usage: "+sys.argv[0]+" '<collection path>' '<deck name>' '<card front>' '<card back>'")

# Mung arguments
coll_file   = sys.argv[1]
deck_name   = sys.argv[2]
card_front  = sys.argv[3]
card_back   = sys.argv[4]
# todo Not even this works. It refuses to embed the newlines in the Card
card_back = re.sub(r"\\n", "\n", card_back)

# All Decks are in a single Collection
print("Get Collection/Deck '"+coll_file+"/"+deck_name+"'")
deck = aopen( coll_file );
deckId = deck.decks.id( deck_name )

# todo Not sure why a simple 'select' doesnt do the model stuff for me...
deck.decks.select( deckId )
basic_model = deck.models.byName('Basic')
basic_model['did'] = deckId
deck.models.save( basic_model )
deck.models.setCurrent( basic_model )

# todo I don't see any other ways to prevent creating a new Deck
if deck.cardCount == 0:
    sys.exit("ERROR: Collection/Deck '"+coll_file+"/"+deck_name+"' does not exist.")

print("Deck has "+str(deck.cardCount())+" cards")

# Build the card
# todo Using .decode('utf-8'), I no longer get 'duplicate card' errors :p
print("Make a new Card for: "+card_front)
fact            = deck.newNote()
fact['Front']   = card_front.decode('utf-8')
fact['Back']    = card_back.decode('utf-8')

# Add Card to the Deck
try:
    deck.addNote( fact )
except Exception, e:
    if hasattr(e, "data"):
        sys.exit("ERROR: Could not add '"+e.data['field']+"': "+e.data['type'])
    else:
        sys.exit(e)

# Done.
print("Save the Deck")
deck.save()
deck.close()
