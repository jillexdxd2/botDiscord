import requests

def getServerInf(server = 20022603): #27536009 lex
    url = f"https://api.battlemetrics.com/servers/{server}"

    token = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbiI6IjM5NzE4MDE2ZjZlYjY1NmMiLCJpYXQiOjE0NzgwMzc1MjQsIm5iZiI6MTQ3ODAzNzUyNCwiaXNzIjoiaHR0cHM6Ly93d3cuYmF0dGxlbWV0cmljcy5jb20iLCJzdWIiOiJ1cm46dXNlcjoxIn0.iwwHt2lvBxlBqcEm7HrX1b1Rb9MXcMghUY5xspluWgw"

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        server_data = response.json()
        serverInfo = {"Team1": server_data["data"]["attributes"]["details"]["squad_teamOne"],
                    "Team2": server_data["data"]["attributes"]["details"]["squad_teamTwo"],
                    "Map": server_data["data"]["attributes"]["details"]["map"]}

        print(serverInfo)
        return serverInfo
    else:
        print(f"Error en la petición: {response.status_code}")
        print(response.json())  

getServerInf()