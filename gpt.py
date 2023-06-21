import openai

openai.api_key = "YOUR API KEY"

model_engine = "text-davinci-003"

def _get_ans_from_response(response:openai.openai_object.OpenAIObject) -> str:
    first = dict(response)['choices']
    sec = dict(first[0])
    return sec['text']

def _getter(model_engine:str = model_engine,prompt:str = "") -> str:
    # Send the request to the Chat GPT API
    response = openai.Completion.create(
                          engine=model_engine,
                          prompt=prompt,
                          max_tokens=1024
                          )
    return _get_ans_from_response(response)

print(_getter(prompt="Why do we need to have an System Development Life Cycle?. In 3 paragraphs"))