
# Define the API endpoint and credentials
BASE_URL = "https://api.prismasdwan.example.com"  # Replace with the actual API base URL
LOGIN_ENDPOINT = "/v2.0/login"
DATA_ENDPOINT = "/v2.0/some-data-endpoint"  # Replace with the specific API endpoint you need

USERNAME = "your_username"  # Replace with your username
PASSWORD = "your_password"  # Replace with your password

def authenticate():
    """Authenticate with Prisma SD-WAN and return the session token."""
    try:
        url = BASE_URL + LOGIN_ENDPOINT
        payload = {
            "username": USERNAME,
            "password": PASSWORD
        }
        headers = {
            "Content-Type": "application/json"
        }
        
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json().get("token")  # Extract the token from the response
    except requests.exceptions.RequestException as e:
        print(f"Authentication failed: {e}")
        return None

def get_data(token):
    """Fetch data from a specific Prisma SD-WAN API endpoint."""
    try:
        url = BASE_URL + DATA_ENDPOINT
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()  # Return the JSON response
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch data: {e}")
        return None

def main():
    try:
        # Authenticate and get the session token
        token = authenticate()
        if not token:
            print("Exiting due to authentication failure.")
            return
        
        print("Authentication successful. Token:", token)
        
        # Fetch data using the token
        data = get_data(token)
        if data:
            print("Data fetched successfully:", data)
        else:
            print("No data retrieved.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
