import urllib.request
import ssl
from json import loads
from splinter.browser import Browser
from time import sleep
import traceback
# ssl._create_default_https_context=ssl._create_unverified_context
# from json import loads

# headers={
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
# }

# def get_ticket_url():
#     req=urllib.request.Request("https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date=2018-02-25&leftTicketDTO.from_station=ZZF&leftTicketDTO.to_station=ZDN&purpose_codes=ADULT");
#     req.headers=headers;
#     html=urllib.request.urlopen(req).read();
#     print(html)
#     print(html[1])
# get_ticket_url()
username=u"3333333"；
passwd=u"33335";
starts = u"%u4E0A%u6D77%2CSHH"#定义开始地址
ends = u"%u8425%u53E3%u4E1C%2CYGT"#定义目的地

dtime=u"2018-02-23"
order=0
pa=u"33333"
ticket_url = "https://kyfw.12306.cn/otn/leftTicket/init"
login_url = "https://kyfw.12306.cn/otn/login/init"
initmy_url = "https://kyfw.12306.cn/otn/index/initMy12306";
def login():
    b.find_by_text(u"登录").click();
    sleep(3);
    b.fill("loginUserDTO.user_name", username)
　　sleep(1);
　　b.fill("userDTO.password", passwd);
    sleep(1);
    print("等待验证码，自行输入...")
    while True:
        if b.url!=imit_myurl:
            sleep(1);
