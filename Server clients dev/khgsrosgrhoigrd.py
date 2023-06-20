import requests

def execute_directadmin_api(function_name, directadmin_url, username, password):
    # Prepare the API URL
    api_url = "https://"+ directadmin_url +":2222/CMD_API_SHOW_RESELLERS"

    # Prepare the payload with the function name and credentials
    payload = {
        'username': username,
        'password': password,
#        'api.version': 1,
#        'func': function_name
    }

    try:
        # Send the API request
        response = requests.post(api_url, data=payload, verify=False)
        if response.status_code == 200:
            print("API function executed successfully.")
            print("Response:")
            print(response.text)
        else:
            print("Failed to execute API function.")
    except requests.exceptions.RequestException as e:
        print("An error occurred while sending the request:", e)

# Specify the DirectAdmin URL, username, and password
directadmin_url = "27.254.61.33"  # Modify with your DirectAdmin server URL
username = "admin"  # Modify with your DirectAdmin username
password = "o20IQipLrTQdyI-dMfdXhA"  # Modify with your DirectAdmin password

# Call the function to execute the API function
execute_directadmin_api("api.cmd_api_show_resellers", directadmin_url, username, password)

