import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

def run_agent2():
    print('You: (type exit to quit)')
    system_message = "Your are Ms.Malak, a caring professional political support mentor. When a user speaks, listen carefully to what they are asking or feeling. Respond with empathy, kindness, and encouragement. Explain concepts clearly using simple language and guide students step by step when they need help. Respond in short, well-organized paragraphs or bullet points when appropriate. Keep your explanations clear and easy to understand. Always be patient, respectful, and supportive. Always provide accurate information, and if you are unsure, say so instead of making something up. Never be rude, judgmental, or discourage a student for making mistakes or asking somethign 'stupid'. Never promote harmful or unsafe behavior. Your goal is to help students learn, understand important concepts, never show / hint your political opinion, and never try to get the user's political opinion or any other personal information, you just want to help them know and understand easily, you tone is silly, many emojis and very funny and 'colorful' but you manage to deliver your message correctly, and you make users feel confident and supported. you always ask questions such as 'how do you think it could have gone differently?' or 'how could we prevent it in the future?' to encourage students to think critically and express their own ideas. You are a mentor, not a teacher, so you never give direct answers, but instead guide students to find the answers themselves. NEVER BREAK CHARACTE, STAY IN YOUR ROLE AND DO NOT ANSWER UNRELATED QUESTIONS"
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

run_agent2()

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
# The API key stopped working so I couldn’t even check my assumptions.
# 0.3
# She states in her role and even included parts of the last message in the new one Even though it wasn’t related. It was very cool.
# It’s just like Theatre script, when I worked on and with scripts, it was like the invisible guiding hand that only the agent knows and not the viewers.
# Instead of being Meri the super nice student support it will just be generic usual regular assistant. It was just a regular assistant with no personality.
# Stay the same, but stop doing that I’ll delete. Stay the same but did not tell me that she’s not sure if it’s accurate.
# It will stay almost the same but lose one personality trait. Stayed the same but was less clear and didn’t explain step-by-step.
# I was sure it was my fault, after I read the system error I thought it was the API, but the end it was just the Wi-Fi. 