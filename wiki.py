import wikipediaapi
import time

user_agent = "p4_wiki (cadegarlett@gmail.com)"
wiki = wikipediaapi.Wikipedia(user_agent, "en")

def fetch_links(page):
    links_list = []
    links = page.links

    for title in links.keys():
        links_list.append(title)

    return links_list    

#create start & target pages
start_page = wiki.page("Pasadena High School (California)")
target_page = wiki.page("Rose Parade")

print(fetch_links(start_page))