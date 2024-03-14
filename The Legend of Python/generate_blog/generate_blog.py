from openai import OpenAI
client = OpenAI()

def genr_blog(topic):
  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "user", "content": topic}
    ]
  )

  completion_content = completion.choices[0].message.content
  return completion_content

def init():
  write_along = True

  while write_along:
    choice = input('Would you like me to write you a paragraph? (y/n) ')

    if choice == 'y':
      topic = input('What should this paragraph be about? ')
      answer = genr_blog(topic)
      print(answer)
    else:
      write_along = False

init()