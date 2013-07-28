# Setup
    1. Grab the Anki 1.2.9 source (under the Linux section) from [here](http://ankisrs.net/)
    1. Add the path to the Anki libs to your PYTHONPATH
    1. `export PYTHONIOENCODING=utf-8`

# Usage
    ./add_to_anki-2.0.12.py '<collection path>' '<deck name>' '<card front>' '<card back>'

# Synopsis
    ./add_to_anki.py "/Users/me/Documents/Anki/User 1/mydeck.anki" "japanese" '黍団子' '黍団子 【きびだんご】  (n) millet dumplings     黍団子一つください。   Give me one kibidango.'

    Also see `examples/add_to_anki.pl` (perl) for a frontend that pulls card info from the clipboard on OSX
