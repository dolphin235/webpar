#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
import re


def web_explore(url):
    try:
        soup = get_soup(url)
        js_script_lists = get_js_scripts(soup)
        link_lists = get_links(soup)

    except Exception as e:
        print(e)


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


def get_soup(url):
    response = requests.get(url)
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        return soup

    else:
        raise Exception(f"[ERROR] response fail : {str(response.status_code)}")


def get_js_scripts(bsoup):
    res_list = []
    profiles = bsoup.find_all('script', type='text/javascript')
    for profile in profiles:
        res_list.append(profile['src'])

    return res_list


def get_links(bsoup):
    res_list = []
    for link in bsoup.find_all('a', attrs={'href': re.compile("^http://")}):
        res_list.append(link.get('href'))

    return res_list