import requests

def get_public_ip():
    try:
        payload = {
            'Username': "admin",
            'Password': "o20IQipLrTQdyI-dMfdXhA"
        }
        response = requests.get('https://27.254.61.33:2222', verify = False, data = payload)
        print(response)
        print(response.text)
    except requests.exceptions.RequestException:
        return None

# Call the function to get the public IP
public_ip = get_public_ip()

