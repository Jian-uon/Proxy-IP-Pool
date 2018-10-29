import json
import os
from class_proxy_ip import ProxyIp


class ProxyWebsite:
    IpList = [] #static ProxyIp

    def __init__(self, dic={}):
        self.url = ''
        self.xpath = ''
        self.ipXpathPattern = ''
        self.portXpathPattern = ''
        try:
            self.url = dic['url']
            self.xpath = dic['xpath']
            self.ipXpathPattern = dic['ip_xpath']
            self.portXpathPattern = dic['port_xpath']
        except Exception as e:
            pass


    #Return a dictionary of all proxy websites.
    @staticmethod
    def load_websites(self, filename):
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
    @staticmethod
    def save_Ip(filename):
        try:
            if ProxyWebsite.IpList == False:
                print("IP list is empty.")
                return
            with open(filename, 'w+') as f:
                json.dump(ProxyWebsite.IpList, fp=f, default=ProxyIp.ip_2_json)
                print('IP list saved successfully.')
        except Exception as e:
            print('Saving IP list error.%s'%e)
            return

def main():
    p = ProxyIp('123.123.123.123', 7777)
    pw = ProxyWebsite()
    pw.IpList.append(p)
    ProxyWebsite.save_Ip('xxx.json')
    pass

if __name__ == '__main__':
    main()
    pass
