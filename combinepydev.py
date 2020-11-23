import wikipedia
import wolframalpha 

while True:
    raw_input = input('Q: ') #using while will never end the questions

    try:
        # adding the wolframalpha info
        app_id = '8PEWKT-9Y4XEQG5UA'

        #create a client
        client = wolframalpha.Client(app_id)

        result = client.query(raw_input)
        answer = next(result.results).text

        print(answer)


    except:
        # adding the wikipedia info
        #wikipedia.set_lang('es') #using the different languages
        print (wikipedia.summary(raw_input, sentences =2)) # fetch the data from wikipedia