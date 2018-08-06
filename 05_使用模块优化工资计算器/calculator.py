import sys, csv, getopt, datetime, queue
from configparser import ConfigParser
from multiprocessing import Process, Queue as q

class Args:
    def __init__(self):
        l = sys.argv[1:]
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
        cfg = ConfigParser()
        cfg.read(args.c)
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
