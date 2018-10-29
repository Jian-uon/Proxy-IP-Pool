import json


class ProxyIp:

    def __init__(self, ip='', port=0):
        self.ip = ip
        self.port = port
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

    def ip_2_json(self):
        return {
            'ip' : self.ip,
            'port': self.port
        }

    def __str__(self):
         return '{"ip":"%s", "port":%d}'%(self.ip, self.port)
