import requests
import json

def filter_data(data, directions):
        """Puts together the data for the same line the direction."""
        sorted_data = dict()
        for p in data['stationboard']:
            line_name = p['name']
            direction = p['to']
            if (direction in directions):
                if (line_name in sorted_data):
                    if (direction in sorted_data[line_name]):
                        if (len(p['passList'])>0):
                            sorted_data[line_name][direction].append(p['passList'][0]['arrival'])
                    else:
                        sorted_data[line_name][direction] = list()
                else:
                    sorted_data[line_name] = dict()
        return sorted_data

# In the event of a network problem (e.g. DNS failure, refused connection, etc),
# Requests will raise a ConnectionError exception.
# Response.raise_for_status() will raise an HTTPError if the HTTP request
# returned an unsuccessful status code.
# If a request times out, a Timeout exception is raised.
# If a request exceeds the configured number of maximum redirections, a
# TooManyRedirects exception is raised.
# All exceptions that Requests explicitly raises inherit from
# requests.exceptions.RequestException.
if __name__ == '__main__':
    with open('data/data.json') as json_file:  
        data = json.load(json_file)
        for p in data['stationboard']:
            print('category: ' + p['category'])
            print('name: ' + p['name'])
            print('to: ' + p['to'])
            if (len(p['passList'])>0):
                print('arrival: ' + p['passList'][0]['arrival'])
            print('')

    
    #url = "http://transport.opendata.ch/v1/stationboard?station=Lausanne,Malley&limit=10"
    #response = requests.get(url)
    #print(response.json()) # might raise an exception, needs to be managed
    #with open('data.txt', 'w') as outfile:
    #    json.dump(response.json(), outfile)
