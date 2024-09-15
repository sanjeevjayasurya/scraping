import bs4
import requests

# Scrape all the book list with title, price and their ratings and availability only on the first page
res = requests.get('https://books.toscrape.com/')
soup = bs4.BeautifulSoup(res.text,"lxml")

products = []
articles = soup.find_all('article', class_='product_pod')

for article in articles:
    # Extract the title
    title = article.find('h3').a.get('title')

    # Extract the availability
    availability = article.find('p', class_='instock availability').text.strip()

    # Extract the price
    price = article.find('p', class_='price_color').text.strip()

    # Extract the star-rating
    star_rating = len(article.find('p', class_='star-rating').find_all('i', class_='icon-star'))

    # Create a dictionary to store the extracted data for each product
    product = {
        'title': title,
        'availability': availability,
        'price': price,
        'star_rating': star_rating
    }

    # Append the product dictionary to the list
    products.append(product)

print(products)

