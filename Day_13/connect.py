import requests
import pprint
import pandas as pd
api_key= "546f470df01ca99446a0353907aca4fb"
api_key_v4 = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1NDZmNDcwZGYwMWNhOTk0NDZhMDM1MzkwN2FjYTRmYiIsInN1YiI6IjYzMDYxNzM2YjdkMzUyMDA3YmM4N2VlZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.Q_JhwJC8ho6IB3DeQj9CThIINg5ROHrs7R2uLBONUhU"
# HTTP REQUESTS

# Endpoint o url

# Método
"""
GET
/movie/{movie_id}
https://api.themoviedb.org/3/movie/550?api_key=546f470df01ca99446a0353907aca4fb
"""
movie_id = 500
api_version = 3
api_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/movie/{movie_id}"
endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}&page=1"
print(endpoint)
# r = requests.get(endpoint) # data={"api_key": api_key})
# print(r.status_code)
# print(r.text)


movie_id = 501
api_version = 4
api_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/movie/{movie_id}"
endpoint = f"{api_base_url}{endpoint_path}"
headers={
    'Authorization': f'Bearer {api_key_v4}',
    'Content-Type': 'application/json;charset=utf-8'
}
# r = requests.get(endpoint, headers=headers) # data={"api_key": api_key})
# print(r.status_code)
# print(r.text)

api_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/search/movie"
search_query='The Matrix'
endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}&query={search_query}"
# print(endpoint)
r = requests.get(endpoint)
# pprint.pprint(r.jexutson())
if r.status_code in range (200, 299):
    data = r.json()
    results = data['results']
    if len(results) > 0:
        # print(results[0].keys())
        movie_ids = set()
        for result in results:
            _id = result['id']
            # print(result['title'], _id)
            movie_ids.add(_id)
        # print(list(movie_ids))
output = 'movies.csv'
movie_data = []

for movie_id in movie_ids:
    api_version = 3
    api_base_url = f"https://api.themoviedb.org/{api_version}"
    endpoint_path = f"/movie/{movie_id}"
    endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}"
    r = requests.get(endpoint)
    if r.status_code in range (200, 299):
        data = r.json()
        movie_data.append(data)

df = pd.DataFrame(movie_data)
print(df.head)
df.to_csv(output, index=False)
# data = r.json()
# data.keys()
# data['page']
# data['results']
# type(data['results'])
# results = data['results']
# results[0].keys()