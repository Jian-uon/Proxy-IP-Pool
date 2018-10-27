# -*- coding: UTF-8 -*-
import json
import os


class ProxyIp:

    def __init__(self):
        self.ip = ''
        self.port = 0
        #服务器地址
        #速度
        #存活时间
        #验证时间

    def load_IP(self, filename):
        jIp = {}
        with open(filename, 'r', encoding="utf-8") as f:
             jIp = json.load(f)
        return jIp


class ProxyWebsite:

    def __init__(self):
        self.url = ''
        self.xpath_pattern = ''
        self.IP_list = [] #ProxyIp

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

    #Save current IP_list
    def save_ip(self, filename):
        try:
            if self.IP_list == False:
                print("IP list is empty.")
                return
            with open(filename, 'w+') as f:
                json.dump(self.IP_list, f)
                print('IP list saved successfully.')
        except():
            print('Saving IP list error.')
            return



def main():
    #p = ProxyIp()
    #res = p.loadIp("ip_address.json")
    #print(res)
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
