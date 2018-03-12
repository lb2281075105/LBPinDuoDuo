# 服饰
'''
抓取的链接：http://apiv3.yangkeduo.com/operation/14/groups?opt_type=1&size=100&offset=0&flip=&pdduid=0
抓取到链接后，接下来的工作就是对JSON格式的数据进行解析
'''

from  urllib import request
import json
import jsonpath
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

class PythonDress(object):
    def __init__(self):
        # 爬取服饰链接
        self.url = 'http://apiv3.yangkeduo.com/operation/14/groups?opt_type=1&size=100&offset=0&flip=&pdduid=0'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:56.0)'}

    def get_html(self):
        req = request.Request(self.url,headers = self.headers)
        response = request.urlopen(req)
        html = response.read()
        return html

    def get_mkdir(self):
        jsonobj = json.loads(self.get_html().decode('utf-8'))
        # 服饰下 - 全部小分类
        opt_name_list = jsonpath.jsonpath(jsonobj, '$..opt_name')
        print(opt_name_list)
       
if __name__ == "__main__":
    pythonDress = PythonDress()
    pythonDress.get_mkdir()
    print(" -- 爬取完毕 -- ")
