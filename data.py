from bs4 import BeautifulSoup
from requests import get
from utils import idfy




cookies = {
    'lolg_euconsent': 'nitro',
    'overwolf_tft_items_2_closed': '1',
}
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'fr-FR,fr;q=0.8',
    'Connection': 'keep-alive',
    # 'Cookie': 'lolg_euconsent=nitro; overwolf_tft_items_2_closed=1',
    'Referer': 'https://www.leagueofgraphs.com/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Sec-GPC': '1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Brave";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

response = get('https://www.leagueofgraphs.com/tft/items', cookies=cookies, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')
items = soup.find_all(class_="itemDescription")
for i in items:
    a, b = i.find(class_="coupleItemsBox").find_all(class_="itemBox")
    a_name = idfy(a.img.get("alt"))
    b_name = idfy(b.img.get("alt"))

    c = idfy(i.find(class_="relative").img.get("alt"))
    print(f"{a_name} + {b_name} = {c}")
    print("========================================")
