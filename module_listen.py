# 导入socket库
import socket

# 导入弹窗库
from win32api import MessageBox
from win32con import MB_ICONWARNING

# 创建s作为广播实例
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

# 配置进程端口
PORT = 1060

# 配置s绑定的地址，可空白
s.bind(('', PORT))

# 循环执行监听代码
while True:
    # 获取数据包
    data, address = s.recvfrom(65535)
    # 在控制台输出
    print('Server received from {}:{}'.format(address, data.decode('utf-8')))
    # 弹出警报窗口
    MessageBox(0, '午时已到', '警报', MB_ICONWARNING)