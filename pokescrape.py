import aiohttp, json

class scraper():
    async def __init__(self, url):
        self.url = url
    async def load(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.url}") as r:
                if r.status == 200:
                    returned = await r.content
                    self.returned = returned
                    return True
                else:
                    return False

scrape = scraper("http://woovie.net/")
scrapeLoad = scrape.load()
print(scrapeLoad)
if scrapeLoad:
    print(scrape.returned)