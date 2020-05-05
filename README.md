# terminal train-tickets query tool on 12306.cn Readme

## demo

![image](https://github.com/cao-weiwei/12306query-tickets/blob/master/imgs/Python3%E5%AE%9E%E7%8E%B0%E7%81%AB%E8%BD%A6%E7%A5%A8%E6%9F%A5%E8%AF%A2%E5%B7%A5%E5%85%B7-%E7%AC%94%E8%AE%B0-%E5%9B%BE1-%E6%9C%80%E7%BB%88%E7%BB%93%E6%9E%9C%E7%A4%BA%E4%BE%8B.png)

## Key Features

- Fetch queries from www.12306.cn vai official APIs / 通过12306车票查询接口制作命令行火车票查询工具


- This a small cralwer script for search train schedule infromation using `requests` library in `Python`, the hardest part is how to analyse train code and train route information from javascript files. / 本项目最核心知识点在于`requests`库的使用，难点在于如何分析js文件寻找车站和英文关系对应以及列车车次信息获取后如何解析。


- Meanwhile, this is also a chance to improve my `Python` skills, like using `yield` to generating iterator and how to use `@property` decorators and others. / 其他的知识点还有`yield`使用，`@property`装饰器，`dicopt`命令行界面以及`prettytable`表格输出`colorama`表格上色。


## Instructions

For more detials please check [here](https://github.com/cao-weiwei/12306query-tickets/blob/master/Python3%E5%AE%9E%E7%8E%B0%E7%81%AB%E8%BD%A6%E7%A5%A8%E6%9F%A5%E8%AF%A2%E5%B7%A5%E5%85%B7-%E7%AC%94%E8%AE%B0.md) / 更多详情请查看[这里](https://github.com/cao-weiwei/12306query-tickets/blob/master/Python3%E5%AE%9E%E7%8E%B0%E7%81%AB%E8%BD%A6%E7%A5%A8%E6%9F%A5%E8%AF%A2%E5%B7%A5%E5%85%B7-%E7%AC%94%E8%AE%B0.md)
