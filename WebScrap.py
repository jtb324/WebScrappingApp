from bs4 import BeautifulSoup
import requests


class AmazonQuery:

    def __init(self):
        self.type = "string"

    def getSoup(self, url):  # thresholdAmt):
        '''This function takes a url and searches for'''
        print("checking amazon....")

        headers = {
            'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
        }

        page = requests.get(url, headers=headers)

        soup = BeautifulSoup(page.content, 'lxml')

        return soup

    def getTitle(self, soup):
        '''This function will fetch the title of the object you are looking for using the productTitle id.'''

        print("Fetching the name of the listing you are interested in...")
        title = soup.find(id="productTitle").get_text().strip()
        return title

    def getPrice(self, soup):
        '''This function will fetch the price of the object. This is based of the price in the buybox and uses the id price_inside_buybox.'''

        print('Fetching the price of the item that you are interested in...')
        price = soup.find(id="price_inside_buybox").get_text().strip()
        return price

    def getDescription(self, soup, tag, identifier):
        '''Goal of this function is to get the description of the object. This returns a list of all items that fit within the provided class. tag is the html5 tag and identifier refers to the html5 class'''

        # print("This is the description of the item...")
        description = soup.find_all(
            tag, class_=identifier)

        return description


desk = AmazonQuery()

page = desk.getSoup(
    'https://www.amazon.com/Standing-Desk-Height-Adjustable-Workstation/dp/B07PQ18JNF/ref=sr_1_7?dchild=1&keywords=standing+desk&qid=1590273343&sr=8-7')


print(desk.getTitle(page))
print('\n')

print(desk.getPrice(page))
print('\n')
tag = input("What is the description of the tag you want? ")
identifier = input("What is the class or id of that tag? ")

# span and a-list-item would be replaced by tag and identifier
print(len(desk.getDescription(page, 'span', 'a-list-item')))
