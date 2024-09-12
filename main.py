import http.client
import json
import sys

#Function to get user github activity
def fecth_github_activity(username):
    #Github api connection
    connection_api = http.client.HTTPSConnection("api.github.com")
    
    #You need to include your GitHub token for the GitHub API connection. 
    token = ""

    #Create a dictionary with the token and specify the software making the request.
    headers = {
        "Authorization": f"token {token}",
        "User-Agent": 'Zarvi16G'
    }
    
    #Make the request, using the username provided as a function parameter.
    connection_api.request("GET", f"/users/{username}/events/public", headers=headers)

    #Save the response using getresponse()
    response = connection_api.getresponse()

    #Use a conditional statement to check if the request was successful (status code 200). If not, return the status code and the reason for the error.
    if response.status == 200:
        #Read the response and decode it from bytes to characters using UTF-8.
        data = response.read().decode('utf-8')
        #Load the response as a dictionary for further use.
        events = json.loads(data)

        #Get the event type and name of the event.
        for event in events:
            event_type = event['type']
            repo_name = event['repo']['name']
            print(f"- {event_type} at {repo_name}")

    else:
        print(f"Error: {response.status} - {response.reason}")

    connection_api.close()


if __name__ == "__main__":
    #The sys module is used to manage command line arguments.
    if len(sys.argv) != 2:
        print("Uso: python main.py <username>")
        sys.exit(1)
    username = sys.argv[1]
    fecth_github_activity(username)