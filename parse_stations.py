# --coding: UTF-8--
import re, requests
from pprint import pprint

url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9098'

# \u8d77\u8bf7\u6c42\uff0c\u83b7\u5f97\u8f66\u7ad9\u539f\u59cb\u5b57\u7b26
resp = requests.get(url)

# \u4f7f\u7528\u6b63\u5219\u8868\u8fbe\u5f0f\uff0c\u63d0\u53d6\u4e2d\u6587\u548c\u7b80\u5199\u4ee3\u7801\u5bf9\u5e94\u5173\u7cfb
# \u6b63\u5219\u8868\u8fbe\u5f0f\uff1a\u4e2d\u6587\u5b57\u7b26\uff0c\u7ad6\u7ebf\u4ee5\u53ca\u5143\u7ec4
stations = re.findall(r'([\u4e00-\u9fa5]+)\|([A-Z]+)', resp.text)
print(stations)
# \u8bbe\u7f6e\u8f93\u51fa\u683c\u5f0f
##pprint(dict(stations), indent=4)
