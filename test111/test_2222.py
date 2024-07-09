# from selenium import webdriver
#
#
# driver=webdriver.chrome()
#
#
# driver.get('https://chat18.aichatos8.com/#/chat/1720426202581')

import requests



url='https://www.baidu.com/s?ie=utf-8&mod=1&isbd=1&isid=AE1BEAE693443945&ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=cp&fenlei=256&oq=melo&rsv_pq=cd5ba4d101397e5f&rsv_t=0fc5tyF%2B9uC6adqMdvN4%2B%2FKyV2RcTyX4gMiAjjd9WSS09AGVw08MC3JLMTQ&rqlang=cn&rsv_enter=0&rsv_dl=tb&rsv_sug3=6&rsv_sug1=5&rsv_sug7=100&rsv_btype=t&inputT=13636&rsv_sug4=15048&bs=melo&rsv_sid=undefined&_ss=1&clist=&hsug=&f4s=1&csor=2&_cr1=31473'
proxies = {
    'http':'http://112.85.164.220:99',
    'https':'https://112.85.164.220:99'
}

re1=requests.get(url=url,proxies=proxies)
print(re1.text)