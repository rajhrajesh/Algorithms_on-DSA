vote = {}
def check_vote(name):
    if vote.get(name):
        print(f"kict out the {name}")
    else:
        vote[name] = True
        print("let them to vote")
print(check_vote("naren"))
print(check_vote("naren"))
print(check_vote("paranuh"))

# cache = {}

# def get_data_server(data):
#     return data

# def get_url(url):
#     if cache.get(url):
#         return cache[url]
#     else:
#         data = get_data_server(u)
#         cache[url] = data 
#         return data
# u = "rajesh@gamil.com"
# print(get_data_server(u))