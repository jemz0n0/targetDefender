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
# 配置接收对象为广播
network = '<broadcast>'

# 配置s绑定的地址，可空白
s.bind(('', PORT))

# 发送报文
s.sendto('Warning!'.encode('utf-8'), (network, PORT))
