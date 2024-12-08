import requests

def get_user_input():
    while True:
        text = input("Please enter text to translate: ").strip()
        if text:
            return text
        print("Input cannot be empty. Please try again.")

def make_post_request(url, headers, data):
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Raises an error for bad responses
        return response
    except requests.exceptions.RequestException as e:
        print(f"HTTP Request failed: {e}")
        return None

def get_translation(text):
    url = "https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&to=zh-Hans"
    headers = {
        "Ocp-Apim-Subscription-Key": "YOUR_SUBSCRIPTION_KEY",
        "Ocp-Apim-Subscription-Region": "YOUR_SUBSCRIPTION_REGION",
        "Content-type": "application/json"
    }
    data = [{"Text": text}]
    response = make_post_request(url, headers, json=data)
    if response:
        translation = parse_response(response)
        if translation:
            try:
                # Assuming the translation API returns a list of translations for each input text
                return translation[0]["translations"][0]["text"]
            except (KeyError, IndexError):
                print("Error parsing the translation response.")
    return None

def parse_response(response):
    try:
        return response.json()
    except ValueError:
        print("Failed to parse JSON response.")
        return None

# The following lines are for demonstration and should be adjusted or removed for actual use
text_to_translate = get_user_input()
translation = get_translation(text_to_translate)
print(f"Translation: {translation}")