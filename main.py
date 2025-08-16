from utils import run_llama

def polish_email(draft):
    prompt = f"Rewrite this into a professional business email:\n{draft}"
    return run_llama(prompt)

if __name__ == "__main__":
    draft = input("Paste your email draft: ")
    print(polish_email(draft))
