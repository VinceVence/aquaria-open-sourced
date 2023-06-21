import openai

class OpenAI_API:

    def __init__(self):
        self.api_key = "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"
        self.model_engine = "text-davinci-003"
        openai.api_key = "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"

    def _get_ans_from_response(self, response):
        first = dict(response)['choices']
        sec = dict(first[0])
        return sec['text']

    def _getter(self, prompt):
        response = openai.Completion.create(
                          engine=self.model_engine,
                          prompt=prompt,
                          max_tokens=2048
                          )
        return self._get_ans_from_response(response)

    def get_answer(self, prompt, concat="Only topics about fisheries in the Philippines. If it's not related say 'I can't answer topics outside fisheries.'"):
        prompt = prompt + "Answer in Formal style." + concat
        answer = self._getter(prompt)
        return answer
