import wikipediaapi

wikipedia.set_lang("en")

def scrape(name="Microsoft", length=3):
    results = wikipedia.summary(name, sentences=length)
    return results

print(scrape())