import httplib2
from bs4 import BeautifulSoup, SoupStrainer


def grabLinks(webpage):
    http = httplib2.Http()
    status, response = http.request(webpage)

    webLinks=[]

    for link in BeautifulSoup(response, parse_only=SoupStrainer('a'), features="html.parser"):
        if link.has_attr('href'):
            webLinks.append(link['href'])

    return {webpage:webLinks}

if __name__ == '__main__':
    print(grabLinks('https://www.aitimejournal.com/'))