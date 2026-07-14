import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

def run_chat():
    print('You: (type exit to quit)')
    system_message = "Your name is Meri. You are a mother role for students. You explain things clearly. You are a good listener and always respond with empathy.You are always there for them and respond with kindness."
    history = []

    while True:
        user_input = input('>> ')

        if user_input.lower() == 'exit':
            break

        history.append({'role': 'user', 'content': user_input})

        response = client.messages.create(
            model='claude-haiku-4-5-20251001',
            max_tokens=300,
            temperature=0.7,
            system=system_message,
            messages=history
        )

        reply = response.content[0].text
        print(f'Claude: {reply}')
        history.append({'role': 'assistant', 'content': reply})

run_chat()

# 0.1
#  It has a personality and that’s nice compared to a chatbot, and it knows more.
# The program will still run, but Claude will forget what it previously said, it only remembers the last message.
# The program will probably fail and won't start, when and try to talk to it, it fails.
# The program will still run, it became a big creative, but mostly the same.
# where in your world does something only work if you carry the whole backstory with you, every single time?
# every time I want to talk to my mother about my friends, she wants the whole backstory and keeps forgetting it so I need to do it every single time.
# I had a bug and I was sure it was because I called it wrong, but it was the API key.
# 0.2
# usage.input_tokens is the number of tokens that were sent to the model and usage.output_tokens is the number of tokens the model generated in its reply.
# When I reduced the tokens and wrote long questions, the answers simply cut off in the middle.
# It was mostly the same but when the temperature was set to 1 the answers were more creative and sometimes a bit off topic, and when it was set to 0 the answers were more factual and to the point, but sometimes a bit boring. 
# Temperature actually controls how creative the model is in its responses. 1 is the most creative and 0 is the least creative.
# Six because for every prompt, I write it also gives a response and it saves all of it in the history.
# It needs to go back to the chat to try and remember because the API doesn’t have its own memory.
# My school takes money for every page with print in the library so no longer your document is the more you pay.
# The AI would stop seeing the user's newest message.
# The AI would forget what it said previously.
# I would lose a useful debugging tool, but the AI would behave the same.
#  The API key stopped working so I couldn’t even check my assumptions.