import sys, socket

def scan():
    l = sys.argv
    try:
        host = l[l.index('--host')+1]
        port = l[l.index('--port')+1]
        assert len(host.split('.')) == 4
        if '-' in port:
            a, b = port.split('-')
            assert int(a) < int(b)
            port = range(int(a), int(b)+1)
        else:
            port = [int(port)]
    except (ValueError, IndexError, AssertionError):
        print('Parameter Error')
        exit()
    l = []
    for i in port:
        s = socket.socket()  # 创建套接字
        s.settimeout(0.1)    # 设置套接字操作的超时期，timeout 是一个浮点数，单位是秒
        # connect 方法的作用是初始化 TCP 服务器连接
        # 这个方法是 connect 方法的扩展版本, 出错时返回出错码, 而不是抛出异常
        # 出错码是非零数字
        if s.connect_ex((host, i)) == 0:  
            l.append(i)
            print(i, 'open')
        else:
            print(i, 'close')
        s.close()
    print('Complted scan. Opening ports at {}'.format(l))

if __name__ == '__main__':
    scan()
