import requests
import random
from fake_useragent import UserAgent
from multiprocessing import Pool

# Define a list of potential URLs to target
urls = [
    "https://thefilmyboyy.blogspot.com",
    "https://thefilmyboyy.blogspot.com/2023/05/the-beauty-of-imperfection-embracing.html",
    "https://thefilmyboyy.blogspot.com/2023/05/breaking-free-journey-of-self-discovery.html",
    "https://thefilmyboyy.blogspot.com/2023/05/how-to-get-traffic-for-your-blogs-in.html",
    "https://thefilmyboyy.blogspot.com/2023/05/9-ways-to-make-money-online.html",
    "https://thefilmyboyy.blogspot.com/2023/05/5-sustainable-living-tips-for-greener.html",
    "https://thefilmyboyy.blogspot.com/2023/05/why-did-kisi-ka-bhai-kisi-ki-jaan-flop.html",
    "https://thefilmyboyy.blogspot.com/2023/05/10-creative-diy-home-decor-ideas-to.html",
    "https://thefilmyboyy.blogspot.com/2023/05/the-psychology-of-color-understanding.html",
    "https://thefilmyboyy.blogspot.com/2023/05/10-tips-for-starting-successful-side.html",
    "https://thefilmyboyy.blogspot.com/2023/05/7-effective-ways-to-reduce-stress-and.html",
    "https://thefilmyboyy.blogspot.com/2023/05/10-tips-for-staying-productive-while.html",
    "https://thefilmyboyy.blogspot.com/2023/05/10-tips-for-starting-successful-online.html",
    "https://thefilmyboyy.blogspot.com/2023/05/10-underrated-bollywood-movies-you-must.html",
    "https://thefilmyboyy.blogspot.com/2023/04/top-10-all-time-favorite-movies-that.html",
    "https://thefilmyboyy.blogspot.com/2023/04/how-to-break-free-from-social-media.html",
    "https://thefilmyboyy.blogspot.com/2023/04/5-tips-to-lose-weight-quickly.html",
    "https://thefilmyboyy.blogspot.com/2023/04/10-tips-to-attain-better-fasion-sense.html",
    "https://thefilmyboyy.blogspot.com/2023/04/10-life-changing-lessons-from-bhagwat.html",
    "https://thefilmyboyy.blogspot.com/2023/04/10-movies-to-learn-biggest-life-lessons.html",
    "https://thefilmyboyy.blogspot.com/2023/04/5-ways-to-look-good.html",
    "https://thefilmyboyy.blogspot.com/2023/04/5-ways-to-start-conversation-with-anyone.html",
    "https://thefilmyboyy.blogspot.com/2023/04/5-ways-to-get-instant-happiness.html",
    "https://thefilmyboyy.blogspot.com/2023/04/9-ways-to-impress-people.html",
    "https://thefilmyboyy.blogspot.com/2023/04/9-ways-to-improve-your-looks.html",
    "https://thefilmyboyy.blogspot.com/2023/04/7-ways-to-cure-depression.html",
    "https://thefilmyboyy.blogspot.com/2023/04/why-you-should-hire-anchors-in-events.html",
    "https://thefilmyboyy.blogspot.com/2023/04/top-7-ways-to-earn-money-online.html",
    "https://thefilmyboyy.blogspot.com/2023/04/suraj-pancholi-latest-news.html",
    # add more URLs here...
]

# Retrieve a list of free proxies from a public API
proxy_api_url = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all"
proxies_response = requests.get(proxy_api_url)
proxies = proxies_response.text.splitlines()[:10]  # use only the first 10 proxies

# Generate a list of user agents
user_agents = [UserAgent().random for _ in range(3)]  # use only 3 user agents

def send_request(i):
    # Add some randomness to the selection of URLs, proxies, and user agents
    url = random.choice(urls)
    proxy = random.choice(proxies)
    user_agent = random.choice(user_agents)

    # Send a request with the randomly-selected parameters
    headers = {
        "User-Agent": user_agent,
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://www.google.com/",
        "Connection": "keep-alive",
        # add more headers here...
    }
    try:
        response = requests.get(url, headers=headers, proxies={"http": proxy}, timeout=30)
        print(f"Request {i} successful with proxy {proxy} and user agent {user_agent}")
    except Exception as e:
        print(f"Request {i} failed with proxy {proxy} and user agent {user_agent}. Error: {e}")

if __name__ == '__main__':
    with Pool(processes=10) as pool:
        pool.map(send_request, range(1000000))
