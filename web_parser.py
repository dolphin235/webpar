#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup


def get_js_script(url):

    response = requests.get(url)
    if response.status_code == 200:
        res_list = []
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        
        profiles = soup.find_all('script', type='text/javascript')
        for profile in profiles:
            res_list.append(profile['src'])

        return res_list

    else:
        print(f"[ERROR] response {str(response.status_code)}")

'''
    sites = []
    try:
        site_detail = {
            'Name' : profile.find('h2').find('a').text,
            'Description' : profile.find('div').text.strip(),
        }
        sites.append(site_detail)

    except:
        site_detail = {
            'Name' : profile.find('h2').find('a').text,
            'Description' : "Description Not Found",
        }
        sites.append(site_detail)
'''

def test_run():
    url = "https://www.naver.com/"
    return get_js_script(url)


def main():

    print(test_run())


if __name__=="__main__": 
    main()
