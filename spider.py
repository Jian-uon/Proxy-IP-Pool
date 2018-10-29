# -*- coding: UTF-8 -*-

# **********************************************************
# * Author        : HuJian
# * Email         : swjtu_hj@163.com
# * Create time   : 2018-10-27 00:04
# * Last modified : 2018-10-27 00:04
# * Filename      : spider.py
# * Description   : 
# **********************************************************
import requests
from lxml import etree
from class_proxy_ip import ProxyIp
from class_proxy_website import ProxyWebsite
import proxy_config
import time

class ProxyIpPoolSipder:

    def __init__(self):
        self.websites = proxy_config.PROXY_WEBSITE_POOL
        self.headers =  proxy_config.HEADERS
        self.startPageNum = 1
        self.stopPageNum = proxy_config.STOP_PAGE_NUM
        self.iniIpList = []

    def get_page(self, url, pageNum):
        try:
            url = url + str(pageNum)
            print('Crawling url{%s}...' % (url))
            req = requests.get(url, headers=self.headers)
            if req.status_code != 200:
                print('Accessing url{%s} failed! Status code {%d}' % (url, req.status_code))
            else:
                print('Finished.')
                time.sleep(1)
        except Exception as e:
            print(e)
            return ""
        return req.status_code, req.text

    def get_ipList_from_page(self, page, xpath, ipXP, portXP):
        pageContent = etree.HTML(page)
        ipList = []
        try:
            for item in pageContent.xpath(xpath):
                ip = item.findall(ipXP[0])[ipXP[1]].text
                port = item.findall(portXP[0])[portXP[1]].text
                tmpIp = ProxyIp(ip, port)
                ipList.append(tmpIp)
        except Exception as e:
            print(e)
        return ipList

    def start_spider(self):
        print('Start crawling...')
        for website in self.websites:
            try:
                curWebsite = ProxyWebsite(website)
                for pageNum in range(self.startPageNum, self.stopPageNum+1):
                    code, page = self.get_page(curWebsite.url, pageNum)
                    if code != 200: continue
                    ipList = self.get_ipList_from_page(page, curWebsite.xpath, curWebsite.ipXpathPattern, curWebsite.portXpathPattern)
                    self.iniIpList.extend(ipList)
                print('-------------------------------------Current website finished.----------------------------------------')
            except Exception as e:
                print(e)


    def verify_ip(self):
        total = len(self.iniIpList)
        times = 0
        while len(self.iniIpList) > 0:
            times += 1
            sampleIp = self.iniIpList.pop()
            currentProxy = {
                "http":"http://{ip}:{port}".format(ip=sampleIp.ip, port=sampleIp.port),
                "https":"https://{ip}:{port}".format(ip=sampleIp.ip, port=sampleIp.port),
            }
            try:
                response = requests.get(proxy_config.TARGET_TEST_WEBSITE, headers=self.headers, proxies=currentProxy, timeout=proxy_config.TIMEOUT)
                if response.status_code == 200:
                    ProxyWebsite.IpList.append(sampleIp)
                    print('IP:{ip} PORT:{port}, connection succeed! [{first}/{second}] valid:{val}'.format(ip=sampleIp.ip, port=sampleIp.port, first=times, second=total, val=len(ProxyWebsite.IpList)))
            except Exception as e:
                print("IP:{ip} PORT:{port} is not valid![{first}/{second}] valied:{val}".format(ip=sampleIp.ip, port=sampleIp.port, first=times, second=total, val=len(ProxyWebsite.IpList)))

    def save_info(self, filename='ip_address.json'):
        try:
            ProxyWebsite.save_Ip(filename)
        except Exception as e:
            print(e)



def main():
    p = ProxyIpPoolSipder()
    p.start_spider()
    p.verify_ip()
    p.save_info()
    '''
    page = p.get_page(p.websites[0]['url'], 1)
    con = etree.HTML(page)
    ip =  con.xpath('//div/table/tbody/tr')
    for i in ip:
        ip = i.findall('td')[0].text
        print(ip)

    print(ip)
    '''

    pass

if __name__ == '__main__':
    main()
    
