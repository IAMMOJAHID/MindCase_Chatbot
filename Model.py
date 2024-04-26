import PyPDF2
import requests


def read_pdf(file_path):
    text = ''
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text


def get_answer_to_question(pdf_text, question):
    
    
    url = "https://api-inference.huggingface.co/models/deepset/roberta-base-squad2"
    
    api_key = "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"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "inputs": {
            "question": question,
            "context": pdf_text
        }
    }

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        # print(response.json())
        output = response.json()
        answer = output["answer"]
        return answer, output
    else:
        return ("Sorry, this is out of context"), ("Sorry, this is out of context")


# # Read PDF content
# # question = "Can you write name of all male and female characters in the movie?"
# # API Key

# # Summarize text
# # answer = get_answer_to_question(pdf_text, question, api_key)
# # if answer:
# #     print("Answer:", answer)
# # else:
# #     print("Failed to Answer.")





