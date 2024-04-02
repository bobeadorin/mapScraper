from main import getPopularTimesData
from GoogleDataFetch import getURL_List
import threading

result_list_lock = threading.Lock()



def getData (place, result_list ) -> None:
        data = getPopularTimesData(place["placeUrl"])
        infoData=  {
         "name": place["name"],
         "type": place["type"],
         "location": place["location"],
         "vicinity": place["vicinity"],
         "traffic" : data
      }
        print(infoData)
        with result_list_lock:
              result_list.append(infoData)

def requestDataHandle (placesData) -> list:
    result_list = []
    threads = [threading.Thread(target=getData, args=(place,result_list)) for place in placesData]
    
    for thread in threads:
          thread.start()
    for thread in threads:
          thread.join()
    return result_list    
    