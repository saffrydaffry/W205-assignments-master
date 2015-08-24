from whoosh.fields import Schema

from whoosh.fields import ID, KEYWORD, TEXT
import csv
#page_dates		tweet_texts	page_texts	page_links	max_id	page_linktxts	tweet_blob
my_schema = Schema( user_id = TEXT(stored=True),
                    dates = TEXT(stored=True),
                    URLs = TEXT(stored = True),
                    hashtags = TEXT(stored = True),
                    tweet = TEXT(stored = True),
                    )

import os

from whoosh.index import create_in

if not os.path.exists("1-index"):
    os.mkdir("1-index")
    index = create_in("1-index", my_schema)

from whoosh.index import open_dir

index = open_dir("1-index")
columns = ["user_id", "dates", "URLs", "hashtags", "tweet"]
# Open a writer for the index
'''
with index.writer() as writer:
   # Open the CSV file
   with open("WC2015.csv", "rb") as csvfile:
     # Create a csv reader object for the file
        csvreader = csv.reader(csvfile)

        for row in csvreader:
            doc = {}

       # Read the values for the row enumerated like
       # (0, "name"), (1, "quantity"), etc.
            for colnum, value in enumerate(row):

         # Get the field name from the "columns" list
                fieldname = columns[colnum]

         # Strip any whitespace and convert to unicode
         # NOTE: you need to pass the right encoding here!
                value = unicode(value.strip(), "utf-8")

         # Put the value in the dictionary
                doc[fieldname] = value

       # Pass the dictionary to the add_document method
                writer.add_document(**doc)

'''
### Querying

searcher = index.searcher()


from whoosh.query import Term, And

print "Query 1:"
query = And([Term("tweet", "usa"), Term("tweet", "japan")])

results = searcher.search(query)
print('# of hits:', len(results))
print('Best Match:', results[0])

print "Query 2"
query = And([Term("tweet", "how"), Term("tweet", "won")])

results = searcher.search(query)
print('# of hits:', len(results))
print('Best Match:', results[0])

print "Query 3"
query = And([Term("tweet", "usa"), Term("tweet", "won")])

results = searcher.search(query)
print('# of hits:', len(results))
print('Best Match:', results[0])

print "Query 4"
query = And([Term("tweet", "canada"), Term("tweet", "usa")])

results = searcher.search(query)
print('# of hits:', len(results))
print('Best Match:', results[0])
'''
# Whoosh' `QuerParser` object automatically parse strings into `Query` objects


from whoosh.qparser import QueryParser

parser = QueryParser("tweet", index.schema)

results = parser.parse("champion or champions")
print results

#parser.parse("(song OR wild) AND (song OR austen)")

#parser.parse("song wild author:'William Blake'")
'''