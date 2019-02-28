#author:xzh#


def cons_source_url_list():
    """"""


    import database

    source_url = "https://pan.baidu.com/pcloud/feed/getdynamiclist?auth_type=ww&filter_types=11000&query_uk=1404980556&category=0&limit=50&start={}&bdstoken=2cef3aa5bc4fa2a5f3c29a0244e13838&channel=chunlei&clienttype=0&web=ww&logid=MTU0OTUzNjg5NTc0MzAuMzc0MTY0OTE5Njk2ODM4Ng=="
    start_list = []
    url_list = []
    for page in range(0, 6):
        start_list.append(page * 50)

        url_list.append(source_url.format(page * 50))
    print(url_list)

    return url_list


