# making of questioning-app

import wolframalpha

raw_input = input('Question:')
app_id = '8PEWKT-9Y4XEQG5UA'

#create a client
client = wolframalpha.Client(app_id)

result = client.query(raw_input)
answer = next(result.results).text

print(answer)
