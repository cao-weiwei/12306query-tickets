# coding: utf-8

"""命令行火车票查看器

Usage:
    tickets [-gdtkz] <from> <to> <date>

Options:
    -h,--help   显示帮助菜单
    -g          高铁
    -d          动车
    -t          特快
    -k          快速
    -z          直达

Example:
    tickets 杭州 北京 2019-03-25
    tickets -dg 杭州 北京 2019-03-25
"""
from docopt import docopt
import requests, prettytable
from stations import stations
from colorama import init, Fore

init()

class TrainsInfo:
    headers = '车次 车站 时间 历时 有票 无座 硬座 软座 硬卧 动卧 软卧 高级软卧 二等座 一等座 特等座 商务座 其他'.split()

    def __init__(self, available_trains, from_to_stations, options):
        """
        定义类用到的变量：列车信息，列车类型选项
        available_trains：列车信息
        fom_o_saions：起止车站，模糊匹配，例如杭州，杭州东等
        options：列车类型选项
        """
        self.available_trains = available_trains
        self.from_to_stations = from_to_stations
        self.options = options

    @property
    def trains(self):
        for each_train in self.available_trains:
            each_train_split = each_train.split('|')
            train_code = each_train_split[3]#车次

            if not self.options or train_code[0].lower() in self.options:
                """
                显示符合条件的列车信息，即列车类型匹配g/d/z等 或者
                不输入列车等级 也可查询
                """
                trains = [train_code,       #车次
                    '\n'.join([Fore.GREEN + self.from_to_stations[each_train_split[6]] + Fore.RESET, 
                               Fore.RED + self.from_to_stations[each_train_split[7]] + Fore.RESET]), 
                
                    '\n'.join([Fore.GREEN + each_train_split[8] + Fore.RESET,
                               Fore.RED + each_train_split[9] + Fore.RESET]),
                            
                    each_train_split[10],   #历时

                    each_train_split[11],   #网上购票
                    each_train_split[26] if each_train_split[26] else '--',     #无座
                    each_train_split[27] if each_train_split[27] else '--',     #硬座
                    each_train_split[24] if each_train_split[24] else '--',     #软座
                    each_train_split[28] if each_train_split[28] else '--',     #硬卧
                    each_train_split[33] if each_train_split[33] else '--',     #动卧
                    each_train_split[23] if each_train_split[23] else '--',     #软卧
                    each_train_split[21] if each_train_split[21] else '--',     #高级软卧
                    each_train_split[30] if each_train_split[30] else '--',     #二等座
                    each_train_split[31] if each_train_split[31] else '--',     #一等座
                    each_train_split[25] if each_train_split[25] else '--',     #特等座
                    each_train_split[32] if each_train_split[32] else '--',     #商务座
                    each_train_split[22] if each_train_split[22] else '--',     #其他
                ]
                yield trains


    def print_train_info(self):
        # 创建表格
        tb = prettytable.PrettyTable()
        # 设置表格标题
        tb.field_names = self.headers
        for train in self.trains:
            # 增加每行数据
            tb.add_row(train)
        print(tb)

 

def cli():
    """command-line interface"""
    arguments = docopt(__doc__)
    from_station = stations.get(arguments['<from>'])
    to_station = stations.get(arguments['<to>'])
    date = arguments['<date>']

    """获取查询得到的列车车次及起止车站信息"""
    url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'.format(date, from_station, to_station)
    r = requests.get(url)

    """
    available_trains 获取查询到的列车信息，返回值是车次信息列表
    from_to_stations 获取起止车站信息，返回值是车站英文代码和车站中文构成的字典
    options 获取从命令行输入的参数，将列表转为字符串，方便后续使用

    """
    available_trains = r.json()['data']['result']
    from_to_stations = r.json()['data']['map']
    options = ''.join([key for key, value in arguments.items() if value is True])

    TrainsInfo(available_trains, from_to_stations, options).print_train_info()


if __name__ == '__main__':
    cli()
