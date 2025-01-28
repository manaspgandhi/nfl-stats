import requests
import html5lib
from bs4 import BeautifulSoup

URL = "https://www.pro-football-reference.com/players/W/WillCa03.htm"

r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')
# prettified_html = soup.prettify()

# name_tag = soup.find("h1").find("span")
# player_name = name_tag.text.strip() if name_tag else "Name not found"

# print(player_name)

col = soup.find("th")
print(col)



def data_to_file(prettified_html):
    output_file = "html_data.html"  # Replace with your desired file name
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(prettified_html)

    print(f"HTML data has been written to {output_file}")
