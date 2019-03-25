import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get(
    'https://www.nettiauto.com/listAdvSearchFindAgent.php?id=175213966&tb=tmp_find_agent&PN[0]=adv_search&PL[0]=advSearch.php?id=175213966@posted_by=@tb=tmp_find_agent&id_model=358')

soup = BeautifulSoup(response.text, 'html.parser')

listings = soup.find_all(class_='listing_nl')

with open('listings.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['Model', 'Price', 'Motor', 'Year', 'Link', 'Image']
    csv_writer.writerow(headers)

    for listing in listings:
        model = listing.find(class_='tricky_link').get_text()
        price = listing.find(class_='main_price').get_text()
        motor = listing.find(class_='eng_size').get_text().replace(
            '(', '').replace(')', '')
        year = listing.find(class_='vehicle_other_info').find(
            'ul').find('li').get_text()
        link = listing.find('a')['href']
        image = listing.find('img')['src']
        csv_writer.writerow([model, price, motor, year, link, image])
