import requests
from bs4 import BeautifulSoup
def fetch_random_article():
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "list": "random",
        "rnlimit": 1,
        "format": "json"
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data['query']['random'][0]
def fetch_article_content(pageid):
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "parse",
        "pageid": pageid,
        "format": "json"
    }
    response = requests.get(url, params=params)
    data = response.json()
    content = data['parse']['text']['*']
    # Parse for links using BeautifulSoup
    soup = BeautifulSoup(content, 'html.parser')
    links = []
    for a in soup.find_all('a', href=True):
        # Filtering only Wikipedia links
        if a['href'].startswith('/wiki/') and ':' not in a['href']:
            links.append(a['href'].split('/wiki/')[-1])
    return content, links
def fetch_articles_from_category(category):
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "list": "categorymembers",
        "cmtitle": f"Category:{category}",
        "cmlimit": 10,
        "format": "json"
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data['query']['categorymembers']
def main():
    print("Welcome to the Random Wikipedia Explorer!")
    # Ask user for category (you can modify this to use actual Wikipedia categories)
    category = input("Enter a category (e.g. Science, History) or press Enter for random: ")
    if category:
        articles = fetch_articles_from_category(category)
        if articles:
            selected_article = articles[0]  # For simplicity, select the first one
            print(f"Selected Article: {selected_article['title']}")
            content, links = fetch_article_content(selected_article['pageid'])
            print(content)  # Display the article content
            # Process to explore links could go here
        else:
            print("No articles found in this category.")
    else:
        random_article = fetch_random_article()
        content, links = fetch_article_content(random_article['pageid'])
        print(f"Random Article: {random_article['title']}")
        print(content)  # Display the article content
    while True:
        follow = input("Would you like to follow one of the articles (y/n)? ")
        if follow.lower() == 'y':
            for i, link in enumerate(links):
                print(f"{i + 1}: {link}")
            choice = int(input("Select a number to follow the link: ")) - 1
            
            if 0 <= choice < len(links):
                new_article_title = links[choice]
                print(f"Following link to {new_article_title}")
                new_article = fetch_article_content(new_article_title)
                print(new_article)  # Display new article content
                # Update `links` for the new article, etc.
            else:
                print("Invalid choice.")
        else:
            break
if __name__ == "__main__":
    main()
