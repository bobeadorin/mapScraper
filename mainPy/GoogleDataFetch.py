import requests


def getLocationRadius(location, radius = 3000) -> list:
    apiKey : str = "AIzaSyCSplKljwEnyAPRjYty6Bj0DKG9EO_1igE"
    apiUrl : str = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={location}&radius={radius}&type=bus_station&key={apiKey}'
    response : dict = requests.get(apiUrl).json()
    placeIds = []
    for place in response['results']:
        placeIds.append({
                "placeUrl" :f"https://www.google.com/maps/place/?q=place_id:{place['place_id']}",
                "name" : place['name'],
                "type" : place['types'][0],
                "vicinity" : place['vicinity'],
                "location": place['geometry']['location'],      
            })
        
    return placeIds

# dataArr = getLocationRadius("44.44552048018695, 26.0628307107671")

def getURL_List(dataArr) -> list:
    urlList = []
    for data in dataArr:
        urlList.append(data["placeUrl"])
    return urlList





