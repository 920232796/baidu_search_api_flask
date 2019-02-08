#author:xzh#

import database

def main():
    """"""
    # result_list = database.select_all_complete_url()
    #
    # print(result_list)
    # title = "haha"
    # complete_url = "https://hahah.com"
    # database.insert_data(title, "2222")
    # database.close_db()

    database.all_data()

    list1 = database.search_content("电子书",0, 10)

    print(list1)
    print(len(list1))

if __name__ == "__main__":
    main()