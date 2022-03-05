import requests

def main():
    jokes = []
    
    jokes.append(get_chuckNorris_joke())
    jokes.append(get_yoMamma_joke())
    jokes.append(get_geekJokes_joke())
    jokes.append(get_jokeApi_joke())
    jokes.append(get_jokesOne_joke())
    jokes.append(get_dadJoke_joke())

    # print jokes
    for joke in jokes:
        if joke == None:
            continue
        print(f"joke source: {joke['category']}\njoke: {joke['joke']}\n")

def get_chuckNorris_joke():
    """query chuck norris jokes

    return
    ------
    format_data : dict
        contains the joke source and joke
    """
    url = 'https://api.chucknorris.io/jokes/random'

    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            joke = data['value']

            format_data = {'category' : 'Chuck Norris', 'joke' : joke}
            
            return format_data

        else: 
            print(f"ERROR fetching joke: {url}")
    except:
        print(f"ERROR: cannot connect to {url}")
    
def get_yoMamma_joke():
    """query yo mama joke

    return
    ------
    format_data : dict
        contains the joke source and joke
    """
    url = 'https://yomomma-api.herokuapp.com/jokes'

    try:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            joke = data['joke']

            format_data = {'category' : 'Yo Mama', 'joke' : joke}
            
            return format_data
        
        else:
            print(f"ERROR fetching joke: {url}")
    except:
        print(f"ERROR: cannot connect to {url}")

def get_geekJokes_joke():
    """query a geek joke

    return
    ------
    format_data : dict
        contains the joke source and joke
    """
    
    url = 'https://geek-jokes.sameerkumar.website/api?format=json'

    try:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            joke = data['joke']

            format_data = {'category' : 'geek joke', 'joke' : joke}

            return format_data
        else:
            print(f"ERROR fetching joke: {url}")
    except:
        print(f"ERROR: cannot connect to {url}")

def get_jokeApi_joke():
    """query a random joke

    return
    ------
    format_data : dict
        contains the joke source and joke
    """
    
    url = 'https://v2.jokeapi.dev/joke/Any'

    try:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            
            # joke can be single or twopart
            joke_type = data['type']
            if joke_type == 'twopart':
                joke = f"{data['setup']} {data['delivery']}"
                format_data = {'category' : 'jokeAPI', 'joke' : joke }
            else:
                joke = data['joke']
                format_data = {'category' : 'jokeAPI', 'joke' : joke }

            return format_data
        else:
            print(f"ERROR fetching joke: {url}")
    except:
        print(f"ERROR: cannot connect to {url}")

def get_jokesOne_joke():
    """query joke of the day

    return
    ------
    format_data : dict
        contains the joke source and joke
    """
    # joke of the day
    url = 'https://api.jokes.one/jod?category=jod'

    try:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            joke_type = data['contents']['jokes']['title']
            joke = data['contents']['jokes']['text']

            format_data = {'category' : joke_type, 'joke': joke}

            return format_data

        else:
            print(f"ERROR fetching joke: {url}")
    except:
        print(f"ERROR: cannot connect to {url}")

def get_dadJoke_joke():
    """query dad joke

    return
    ------
    format_data : dict
        contains the joke source and joke
    """
    
    url = 'https://icanhazdadjoke.com/'

    try:
        header = {'Accept' : 'application/json'}
        response = requests.get(url, headers=header)
        
        if response.status_code == 200:
            data = response.json()
            joke = data['joke']

            format_data = {'category' : 'dad joke', 'joke' : joke}

            return format_data
        else:
            print(f"ERROR fetching joke: {url}")
    except:
        print(f"ERROR: cannot connect to {url}")

if __name__ == "__main__":
    main()