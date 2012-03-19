# -*- coding: utf-8 -*-

# Load required modules
import random

def getQuote():
    """Returns an awesome randomized quotation."""
    
    # Enough messin' around. Get to work.
    File = open('quotes.txt','r')                   # Open the file with the quotations/
    library = File.readlines()                      # Read all of em' into a list. (I'm so damn lazy!)
    
    return (random.choice(library)).split(';')      # For randomly choosing a quotation
    # And now for some details:
    #   * The quotations in quotes.txt (take a look yourself) have the following syntax: 
    #     {quote};{author};{URL}
    #   * random.choice(a) returns a random member of list 'a'
    #   * "string;delimited".split(';') returns a list like so ['string', 'delimited']
    #   * Tada!

quote = getQuote()          # Abracadabra!

# Everything below is quite 'self-explanatory'
print "Content-Type: text/html"         # The HTTP header
print ""                                # Header ends

# Body (place this in fancy markup)
print quote[0]                          # The quote (ahem)
print "<br/>"
print "~ " + quote[1]                   # ~ author
print "<br/>"
print "<a href='%s'>And now for something completely different!" % quote[2] # The surprising part!

# What you lookin' at boy?
