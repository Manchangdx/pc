import sys, csv, getopt, datetime, queue
from configparser import ConfigParser
from multiprocessing import Process, Queue as q

class Args:
    def __init__(self):
        l = sys.argv[1:]
        # 选项有“短选项”和“长选项”两种，短选项格式：一个减号一个字母；长选项格式：俩减号多个字母
        # getopt.getopt 方法有仨参数：要处理的对象列表、短选项组、长选项组
        # 短选项组为字符串，若选项有参数，后面加冒号；长选项组为列表，若选项有参数，后面加等号
        # 该方法返回值为二元元组，每个元素都是列表，一个是选项解析结果，另一个是其余参数
        options, args = getopt.getopt(l, 'hC:c:d:o:', ['help'])
        d = dict(options)
        if len(options) == 1 and list(d.keys())[0] in ['-h', '--help']:
            print('Usage: calculator.py -C cityname -c configfile -d userdata -o resultdata')
            exit()
        if d.get('-C'):
            self.C = d['-C'].upper()
        else:
            self.C = 'DEFAULT'
        self.c = d['-c']
        self.d = d['-d']
        self.o = d['-o']

args = Args()

class Config:
    def __init__(self):
        self.config = self._a()
    def _a(self):
        d = {'s':0}
        # 生成配置文件解析类的实例
        cfg = ConfigParser()
        # 解析配置文件
        cfg.read(args.c)
        # 获取某个配置组下的所有键值对，items 方法的返回值为列表，其中每个元素都是二元元组
        # 注意，每个元素的 key 都是全小写的字符串，不论配置文件里是什么样
        for m, n in cfg.items(args.C):
            if m == 'jishul' or m == 'jishuh':
                d[m] = float(n)
            else:
                d['s'] += float(n)
        return d

config = Config().config

def cal_tax(i):
    z = int(i)
    sb = z * config.get('s')
    if z < config.get('jishul'):
        sb = config['jishul'] * config.get('s')
    if z > config.get('jishuh'):
        sb = config['jishuh'] * config.get('s')
    x = (z-sb-3500)
    if x < 0:
        s = 0
    elif x <= 1500:
        s = x * 0.03
    elif x <= 4500:
        s = x * 0.1 - 105
    elif x <= 9000:
        s = x * 0.2 - 555
    elif x <= 35000:
        s = x * 0.25 - 1005
    elif x <= 55000:
        s = x * 0.3 - 2755
    elif x <= 80000:
        s = x * 0.35 - 5505
    else:
        s = x * 0.45 - 13505
    sh = z - sb - s
    return [z, format(sb, '.2f'), format(s, '.2f'), format(sh, '.2f')]

class Data:
    def __init__(self):
        with open(args.d) as f:
            l = list(csv.reader(f))
        self.value = l

data = Data().value


q1, q2 = q(), q()

def f1():
    for i in data:
        q1.put(i)

def f2():
    def haha():
        while True:
            try:
                a, b = q1.get(timeout=0.1)
                x = cal_tax(b)
                x.insert(0, a)
                yield x
            except queue.Empty:
                return
    for i in haha():
        q2.put(i)

def f3():
    with open(args.o, 'a') as f:
        while True:
            try:
                csv.writer(f).writerow(q2.get(timeout=0.1))
            except queue.Empty:
                return

Process(target=f1).start()
Process(target=f2).start()
Process(target=f3).start()
