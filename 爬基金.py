import requests
import re
import random
import time


info_dict = dict()

# 获取数据
def request(fund_num, last_num):
    # print(last_num)
    url = 'http://fundgz.1234567.com.cn/js/' + fund_num + '.js?rt=1590713320543'
    r = requests.get(url)
    return r.text

# 数据处理
def process(info,i):
    n = re.search('name":"(\w+)',info)
    q = re.search('gszzl":"([-]?\w+\.\w+)',info)
    # info_dict.clear()
    info_dict[i] = [n.group(1), q.group(1)]

def main():
    while True:
        num_list = ['005737', '006087', '007339']
        for i in range(3):
            last_num = random.randint(11111111,99999999)
            info = request(num_list[i], last_num)
            process(info,i)
        # print('=====================')
        # time.sleep(20)
        print(info_dict[0]+info_dict[1]+info_dict[2],end='\r')
        # print(1)
        # print(str(info_dict[0]),end='\r')
        # print(info_dict[0],end='\r')
        # print(info_dict[1],end='\r')
        # print(info_dict[2],end='\r')
        info_dict.clear()
        time.sleep(5)



if __name__ == '__main__':
    main()