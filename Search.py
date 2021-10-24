
import requests
import json

def get_movie_rating(obj):
    ratings = obj.get('Ratings')
    for x in ratings:
        if x.get("Source") == "Rotten Tomatoes":
            return int(x.get("Value").strip('%'))
    return 0

def get_movie_data(str):
    url = "http://www.omdbapi.com/"
    parameters = {"t":str, "r":"json", "apikey": "b55608c3"}
    res = requests.get(url, parameters)

    print(res.text)
    print(res.url)
    result = res.json()
    print(result)
    return result


def get_sorted_recommendations(arr):
    ret = []
    for x in arr:
        item = (x,get_movie_rating(get_movie_data(x)))
        ret.append(item)

    ret.sort(key = lambda e: (e[1], e[0]), reverse = True)
    return [item[0] for item in ret]


print(get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes", "Dead Pool"]))