PROXY_WEBSITE_POOL = [
	{
		"url" : "https://www.kuaidaili.com/free/inha/",
		#"xpath" : "//td[@data-title='IP']/text()",
        "xpath":"//div/table/tbody/tr",
        "ip_xpath":['td',0],
        "port_xpath":['td',1],
	},
	{
		"url" : "http://www.xicidaili.com/nn/",
		"xpath":"//table/tr[@class]",
        "ip_xpath":['td',1],
        "port_xpath":['td',2],
	}
]

HEADERS = {'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4',
                'Accept-Encoding': 'gzip, deflate, sdch',
                'X-Requested-With': 'XMLHttpRequest',
                'Accept': 'text/html, */*; q=0.01',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
                'Connection': 'keep-alive',
                'Referer': 'http://www.baidu.com'}

TARGET_TEST_WEBSITE = 'http://www.jianshu.com'
STOP_PAGE_NUM = 10
TIMEOUT = 1
