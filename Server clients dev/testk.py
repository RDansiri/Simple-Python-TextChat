import requests

# Specify the DirectAdmin URL, username, and password
username = "admin"  # Modify with your DirectAdmin username
password = "o20IQipLrTQdyI-dMfdXhA"  # Modify with your DirectAdmin password
func = "api.cmd_api_show_resellers"

payload = {
    'username': username,
    'password': password,
    'api.version': 1,
    'func': func
}
x = requests.get('https://27.254.61.33:2222/CMD_API_SHOW_RESELLERS', verify = False)
print(x.text)
