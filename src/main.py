import requests
import json
def main():
    username=input("Enter ur git username:")
    api_url=f"https://api.github.com/users/{username}"
    user_data=get_data(api_url)
    if user_data is not None:
        display_data(user_data)
        save_response(user_data)
    else:
        print("User not found")

def get_data(api_url):
    response=requests.get(api_url)
    if(response.status_code==200):
        print("Data fetched successfully")
        user=response.json()
        return user
    else:
        return None
def display_data(user):
    print(
    f"\nUsername:{user['login']}\n"
    f"Followers:{user['followers']}\n"
    f"Following:{user['following']}\n"
    f"Public Repositories:{user['public_repos']}\n"
    f"Account Created:{user['created_at']}\n"
    )

def save_response(user):
    with open(f"output\\{user['login']}.json","w") as file:
        json.dump(user,file,indent=4)
main()