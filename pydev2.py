# import the API from wikipedia

import wikipedia

while True:
    raw_input = input('Q:')
    wikipedia.set_lang('es') #using the different languages
    print (wikipedia.summary(raw_input, sentences =2)) # fetch the data from wikipedia