#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import re
import requests
from bs4 import BeautifulSoup

from multiprocessing import Pool

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36'}

def download_page():
    try:
        urls = []
        url_VG = "http://dotamax.com/match/tour_team_heroes/?team_id=726228"
        url_Secret = "http://dotamax.com/match/tour_team_heroes/?team_id=1838315"
        url_C9 = "http://dotamax.com/match/tour_team_heroes/?team_id=1333179"
        url_Empire = "http://dotamax.com/match/tour_team_heroes/?team_id=46"
        url_EG = "http://dotamax.com/match/tour_team_heroes/?team_id=39"
        url_IG = "http://dotamax.com/match/tour_team_heroes/?team_id=5"
        url_LGD = "http://dotamax.com/match/tour_team_heroes/?team_id=15"
        url_NiP = "http://dotamax.com/match/tour_team_heroes/?team_id=2085365"
        url_Alliance = "http://dotamax.com/match/tour_team_heroes/?team_id=111474"
        url_EHOME = "http://dotamax.com/match/tour_team_heroes/?team_id=4"
        url_NewBee = "http://dotamax.com/match/tour_team_heroes/?team_id=1375614"
        url_HR = "http://dotamax.com/match/tour_team_heroes/?team_id=1846548"
        url_NaVi = "http://dotamax.com/match/tour_team_heroes/?team_id=36"
        url_HGT = "http://dotamax.com/match/tour_team_heroes/?team_id=484909"
        url_CDEC = "http://dotamax.com/match/tour_team_heroes/?team_id=1520578"
        url_VP = "http://dotamax.com/match/tour_team_heroes/?team_id=40"
        url_BU = "http://dotamax.com/match/tour_team_heroes/?team_id=2197847"
        urls.append(url_VG)
        urls.append(url_Secret)
        urls.append(url_C9)
        urls.append(url_Empire)
        urls.append(url_EG)
        urls.append(url_IG)
        urls.append(url_LGD)
        urls.append(url_NiP)
        urls.append(url_Alliance)
        urls.append(url_EHOME)
        urls.append(url_NewBee)
        urls.append(url_HR)
        urls.append(url_NaVi)
        urls.append(url_HGT)
        urls.append(url_CDEC)
        urls.append(url_VP)
        urls.append(url_BU)

        teams = ["VG", "Secret", "C9", "Empire", "EG", "IG", "LGD", "NiP",
                "Alliance", "EHOME", "NewBee", "HR", "NaVi", "HGT", "CDEC",
                "VP", "BU"]
        for url_team in zip(urls,teams):
            url = url_team[0]
            team = url_team[1]
            page = requests.get(url,timeout = 10,headers = headers)
            page.encoding = 'utf-8'
            page = page.content
            # soup = BeautifulSoup(page)

            hero_patt = r'<span class="table-title-font"> (.*?)</span></a></td><td>(.*?)</td>'
            hero_times = re.findall(hero_patt, str(page))
            hero_time_str = ''
            for hero_time in hero_times:
                print hero_time
                hero = hero_time[0]
                time = hero_time[1]
                hero_time_str += hero + ' ' + time + '\n'
            filename = str(team) + '.txt'
            with open(filename, 'w') as fw:
                fw.write(hero_time_str)

            print 'downloading finish'
    except requests.HTTPError, e:
        print HTTPError,':',e


if __name__ == '__main__':
    download_page()

