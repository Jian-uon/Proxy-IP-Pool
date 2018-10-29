# -*- coding: UTF-8 -*-
import json
import os


class ProxyIp:

    def __init__(self, ip='', port=0):
        if ip != '' and port != 0:
            self.ip = ip
            self.port = port
        #服务器地址
        #速度
        #存活时间
        #验证时间

    def load_IP(self, filename):
        jIp = {}
        with open(filename, 'r', encoding="utf-8") as f:
             jIp = json.load(f)
        return jIp

    def __str__(self):
         return '{"ip":"%s", "port":%d}'%(self.ip, self.port)

class ProxyWebsite:

    def __init__(self):
        self.url = ''
        self.ipXpathPattern = ''
        self.portXpathPattern = ''
        self.IpList = [] #ProxyIp

    #Return a dictionary of all proxy websites.
    @staticmethod
    def load_websites(self, filename):
        jWebsite = {}
        try:
            if os.path.exists(filename) == False:
                print('File not exists!')
                return
            else:
                with open(filename, 'r') as f:
                    jWebsite = json.load(f)
                if jWebsite == False:
                    print('File is empty!')
        except():
            print('Loading websites error!.')
            return
        return jWebsite

    #Save current IpList
    def save_Ip(self, filename):
        try:
            if self.IpList == False:
                print("IP list is empty.")
                return
            with open(filename, 'w+') as f:
                json.dump(self.IpList, f)
                print('IP list saved successfully.')
        except():
            print('Saving IP list error.')
            return
    
    def add_Ip(self, item):
        self.IpList.extend(item)  


def main():
    p = ProxyIp('127.0.0.1', 8088)
    #res = p.load_IP("ip_address.json")
    #print(res)
    print(p.__str__())
    #ans:{'proxys': [{'ip': '61.183.176.122', 'port': 53281}, {'ip': '202.108.251.230', 'port': 57491}]}
    sample = { 
        'config':'test',
        'details':[
            {'IP':'123.123.123.123', 'port':8080},
            {'IP':'123.123.123.124', 'port':8081},
            ]
        }
    #with open('temp.json', 'w+') as f:
    #    json.dump(sample, f)
    #print(json.dumps(sample))
    #p2 = ProxyWebsite()
    #print(p2.loadWebsites('temp.json'))
    pass


if __name__ == '__main__':
    main()
    pass
