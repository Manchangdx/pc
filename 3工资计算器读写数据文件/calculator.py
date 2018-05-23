import sys, csv

class Args:
    def __init__(self):
        l = sys.argv[1:]
        self.c = l[l.index('-c')+1] 
        self.d = l[l.index('-d')+1]
        self.o = l[l.index('-o')+1]

args = Args()

class Config:
    def __init__(self):
        self.config = self._a()
    def _a(self):
        d = {'s':0}
        with open(args.c) as f:
            for i in f.readlines():
                l = i.split('=')
                m, n = l[0].strip(), l[1].strip()
                if m == 'JiShuL' or m == 'JiShuH':
                    d[m] = float(n)
                else:
                    d['s'] += float(n)
        return d

config = Config().config

def cal_tax(i):
    z = int(i)
    sb = z * config.get('s')
    if z < config.get('JiShuL'):
        sb = config['JiShuL'] * config.get('s')
    if z > config.get('JiShuH'):
        sb = config['JiShuH'] * config.get('s')
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

with open(args.o, 'w') as f:
    for a, b in data:
        x = cal_tax(b)
        x.insert(0, a)
        csv.writer(f).writerow(x)
