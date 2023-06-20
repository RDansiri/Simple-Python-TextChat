import requests

# Set the login endpoint URL and credentials
login_url = "https://api.27.254.61.33/login"
username = "admin"
password = "o20IQipLrTQdyI-dMfdXhA"

# Set the target subdomain and new IP address
target_subdomain = "home107"
new_ip = "66.66.66.66"

# Create a session
session = requests.Session()

# Perform login
payload = {
    "username": username,
    "password": password
}
response = session.post(login_url, data=payload, verify=False)

# Check if login was successful
if response.status_code == 200:
    print("Login successful")

    # Update the IP address of the target subdomain
    update_url = f"https://api.example.com/update_subdomain/{target_subdomain}"
    update_payload = {
        "ip": new_ip
    }
    response = session.post(update_url, data=update_payload, verify=False)

    # Check if the IP update was successful
    if response.status_code == 200:
        print(f"Subdomain '{target_subdomain}' IP updated successfully to '{new_ip}'")
    else:
        print("Failed to update subdomain IP")

else:
    print("Login failed")
