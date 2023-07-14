from genai.credentials import Credentials
from genai.model import Model
from genai.schemas import GenerateParams

api_url = 'YOUR_WATSONX_API_URL'

def get_summary(api_key:str, text: str)->str:
    
    creds = Credentials(api_key, api_endpoint=api_url)

    params = GenerateParams(
        decoding_method="sample",
        max_new_tokens=200,
        min_new_tokens=10,
        stream=False,
        temperature=0.7,
        top_k=50,
        top_p=1,
    )


    summarizer = Model("google/flan-ul2", params=params, credentials=creds)

    prompt = 'The following text is a transcript from a financial earning call. Read the text and then write a short one paragraph summary.' + text

    responses = summarizer.generate([prompt])

    if responses:
        return responses[0].generated_text
    
    return ''

if __name__ == '__main__':
    api_key = input('Enter your API Key: ')
    text = input('Provide the text to summarize')

    summary = get_summary(api_key=api_key, text=text)

    print(summary)