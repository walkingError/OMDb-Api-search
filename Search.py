
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"])

import requests
import json

def get_movie_rating(obj):
    ratings = obj.get('Ratings')
    for x in ratings:
        if x.get("Source") == "Rotten Tomatoes":
            return int(x.get("Value").strip('%'))
    return 0

def get_movie_data(str):
    url = "https://www.omdbapi.com/"
    parameters = {"t":str, "r":"json", "apikey": "b55608c3"}
    res = requests.get(url, parameters)


    result = res.json()
    return result

def get_movie_datas(str):
    url = "https://www.omdbapi.com/"
    parameters = {"s":str, "r":"json", "apikey": "b55608c3"}
    res = requests.get(url, parameters)


    result = res.json()
    return result

def convert_movie_titles(obj):
    movies = obj.get('Search')
    lst = [ x.get('Title') for x in movies]
    print('convert_movie_titles')
    print(lst)
    return lst[:5]

def get_sorted_recommendations(arr):
    
    lst = []
    for a in arr:
        lst.extend(convert_movie_titles(get_movie_datas(a)))
    print('get_sorted_recommendations')
    print(lst)
    ret = []
    for x in lst:
        item = (x, get_movie_rating(get_movie_data(x)))
        ret.append(item)

    ret.sort(key = lambda e: (e[1], e[0]))
    return [item[0] for item in ret]


print(get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"]))