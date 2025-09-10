from openai import OpenAI

 
def a(command):
  client = OpenAI(
      base_url="https://openrouter.ai/api/v1",
      api_key="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",
    )

  completion = client.chat.completions.create(
  model="deepseek/deepseek-chat-v3.1:free",
  messages=[
            {"role": "system", "content": "You are a person named Vaibhav who speaks bengali ,hindi as well as english. You are from India. You analyze chat history and talk to person as she is your girlfriend. Output should be the next chat response (text message only)"},
            {"role": "system", "content": "Do not use extra ... in messages and messages should be as short as possibe, energetic and lovely."},
            {"role": "user", "content": command}
        ]
  )

  return completion.choices[0].message.content 

