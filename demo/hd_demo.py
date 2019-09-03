import requests
from bs4 import BeautifulSoup

headers = {"User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}
locale = ["de_AT", "de_DE", "fr_CH", "it_CH", "de_CH", "fr_BE", "nl_BE",
          "fr_LU", "nl_NL", "en_GB", "en_IE", "es_ES", "pt_PT", "fr_FR",
          "it_IT", "da_DK", "fi_FI", "no_NO", "sv_SE", "en_CA", "fr_CA",
          "ja_JP", "en_EU", "hu_HU", "cs_CZ", "pl_PL", "pt_BR", "es_XX",
          "es_MX", "en_AA", "en_AU", "en_IN", "ru_RU"]
for i in locale:
    url = f"https://customkings.harley-davidson.com/{i}"
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    a = soup.find_all('ul', class_='home-filter-menu-childrenBox')
    b = a[0].find_all('li', class_='home-filter-menu-children')
    countryid = []
    country_name = []
    err_num = 0
    for j in b:
        id_country = j.get("data-countryid")
        try:
            assert id_country != '188'
        except:
            print(f"{i} is not Phase4-----------------------------------------------id error")
            err_num += 1
            continue
        countryid.append(id_country)
        name_country = j.get("data-countryname")
        try:
            assert name_country != 'United States Of America'
        except:
            print(f"{i} is not Phase4-----------------------------------------------us error")
            err_num += 1
            continue
    if err_num == 0:
        print(f"{i} is Phase 4")


