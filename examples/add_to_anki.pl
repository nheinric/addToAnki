#!/usr/bin/env perl
use strict;
use warnings;

=head1 DESCRIPTION

A quick script to dump a copied WWWJDIC definition from the clipboard
and shove it into an Anki deck using add_to_anki.py.

See L<http://www.csse.monash.edu.au/~jwb/cgi-bin/wwwjdic.cgi?1C>

=head1 NOTES

Only works on OSX for now. But if you have an alternative to `pbpaste` on
your platform for dumping clipboard contents you could use that.

It expects UTF-8 encoding.

I added this to my Quicksilver catalog to make it easier to run.

=head1 SYNOPSIS

=over
=item Close Anki if it's open
=item Copy a full definition and sample sentences from WWWJDIC to the clipboard
=item Run this script
=back
=cut

# Setup the environment. Must be UTF8! See add_to_anki.py
my $home = $ENV{HOME};
$ENV{LANG} = "en_US.UTF-8";
$ENV{PYTHONIOENCODING} = "utf-8";
$ENV{PYTHONPATH} .=
    ":/Applications/Anki.app/Contents/Resources/lib/python2.7"
    . ":$home/workspace/lib/anki-1.2.9/libanki";
open DEBUG, ">/tmp/blah" or die "Cant open debug file: $!";

my $deck = "$home/Documents/Anki/japanese.anki";

# On OSX, this will dump the contents of the clipboard.
my $str = `pbpaste`;
print DEBUG "Process input: $str\n";

# WWWJDIC-specific cleanup.
my $key = (split /(\s|【)+/, $str)[0];
$str =~ s/\[(Edit|Ex|L|GI?|S|A|JW|W|V)\]//g;
$str =~ s/'//g;
$str =~ s/\n/\\n/g;

#print DEBUG "add_to_anki.py '$deck' '$key' '$str'\n";
my $log = `$home/workspace/bin/add_to_anki.py '$deck' '$key' '$str'`;

print DEBUG "Result:\n$log\n";
close DEBUG;
