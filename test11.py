#author:xzh#

import requests

import  re
from fake_useragent import UserAgent
import source_url_list
import database

import pymysql

def main():
    """"""

    root_url = "https://pan.baidu.com/s/"

    # source_url = "https://pan.baidu.com/pcloud/feed/getdynamiclist?auth_type=1&filter_types=11000&query_uk=1404980556&category=0&limit=50&start=2&bdstoken=2cef3aa5bc4fa2a5f3c29a0244e13838&channel=chunlei&clienttype=0&web=1&logid=MTU0OTUzNjg5NTc0MzAuMzc0MTY0OTE5Njk2ODM4Ng=="

    user_agent = UserAgent().chrome
    print(user_agent)

    headers = {
        "User-Agent": user_agent,
        "Cookie": "BAIDUID=B665C57519BB1CE733014F986955D850:FG=ww; PSTM=1524450639; BIDUPSID=4E742698B7CE1AA938C285FED0123F7A; PANWEB=ww; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; MCITY=-54028%3A; BDCLND=FdI5VGiLGiuP50G3DmS9Sv%2BT5puEraBA80TAnYJd7LM%3D; cflag=13%3A3; delPer=0; PSINO=2; BDUSS=0hxQWtLZVlEYW1HTjB2RXpJZmRIa3ZFdUZ1UXp1UmQ4R3NrQ0lmTXROOWVXb05jQUFBQUFBJCQAAAAAAAAAAAEAAAADU5O6eDkyMDIzMjc5NgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAF7NW1xezVtcV; STOKEN=8ee50ac349feeb50e7e416fc38f3d2662813e837d7f044ae0a58ae812988a2d9; SCRC=24a1fa6c4edc40cba18ff8924ac79c09; Hm_lvt_7a3960b6f067eb0085b7f96ff5e660b0=1549182728,1549509635,1549510597,1549520225; Hm_lvt_f5f83a6d8b15775a02760dc5f490bc47=1549509786,1549510604,1549520259; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; BDRCVFR[M7pOaqtZgJR]=I67x6TjHwwYf0; H_PS_PSSID=1445_21090_28328_28413; Hm_lpvt_f5f83a6d8b15775a02760dc5f490bc47=1549537336; recommendTime=android2019-ww-31%2017%3A00%3A00; Hm_lpvt_7a3960b6f067eb0085b7f96ff5e660b0=1549537453; PANPSC=13191783871572786376%3AnSvEWpGhaFom0wdWVT9TBXiC6e0Ll37p5Qm%2FyHlw2fqYXvTamKXvPHgXofrWESI4fJ06i7Fpl5f%2FHSZRhh6%2BPa1Sr93PEHDiDv6sF2krPB6pWetz1AjD6SeKHrlyURG2vIcMCeE%2BEzPl0236xFtTr1QxIuFgE8LFzlMymqcoIUw%3D",
        "Connection": "keep-alive"
    }


    result_url_list = database.select_all_complete_url()

    ## 得到url list  然后for循环每个url  进行数据搜索
    result_source_url_list = source_url_list.cons_source_url_list()

    for source_url in result_source_url_list:
        res = requests.get(source_url, headers = headers)
        # print(res.status_code)
        # print(res.content)

        result_dict = eval(str(res.content.decode()))
        if (result_dict.get("errno") == 2):
            print("~~~~~~~~~~end~~~~~~~~~~~~~~")
            break
        result_list = result_dict.get("records")
        # print(result_list)

        for each_file in result_list:
            title = each_file.get("title").replace("//", "/").replace("'", "").replace("‘", "")
            short_url = each_file.get("shorturl")
            print(title)
            file_list = each_file.get("filelist")
            file_name_list = []
            if file_list:
                for each_file1 in file_list:
                    file_name = each_file1.get("server_filename").replace("//", "/").replace("'", "").replace("‘", "")
                    file_name_list.append(file_name)
            title = title + (str(file_name_list)).replace("'", "").replace("‘", "")
            if len(title) > 220:
                title = title[:210]

            # print(short_url)
            # complete_url = "https://pan.baidu.com/s/" + short_url
            if short_url not in result_url_list:
                database.insert_data(title, short_url)
                print(title)
        import time
        time.sleep(5)
    database.close_db()







if __name__ == "__main__":
    main()