vote = {}
def check_vote(name):
    if vote.get(name):
        print("kict out the")
    else:
        vote[name] = True
        print("let them to vote")
# print(check_vote('rajesh'))
# print(check_vote('rajesh'))
# print(check_vote('mike'))
# print(check_vote("mike"))

cache = {}

def get_url(url):
    if cache.get(url):
        return cache[url]
    else:
        cache[url] = url