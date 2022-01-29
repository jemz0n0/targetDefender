# 导入PyQt5的GUI库
# 选择Qt5的原因：自带Qt Designer图形化设计程序
# 只需在Qt Designer中设计好窗体，在代码中导入.ui工程文件即可
import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit,
    QTextEdit, QGridLayout, QApplication)
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIcon

# 导入弹窗库
from win32api import MessageBox
from win32con import MB_ICONWARNING

# 导入os库
# 1.用于获取当前目录，以执行相同目录下的可执行模块。不使用相对目录的原因是，os库默认的path为python安装位置。
# 2.用于执行DOS命令，启动或结束程序
from os import system
from os import path

# 导入time.sleep
# sleep原因：防止系统kill进程过慢，导致下一进程无法正常启动
from time import sleep

# 定义监听状态
# 用于sendWarning()中判断是否需要启动监听程序
# 不在class的__init__()内定义的原因：声明全局变量需要变量已被定义
status = False
# 定义计数器
# 用于程序最下方显示当前操作前的序号
counter = 0

############################################################# MAIN BODY

# GUI窗口实例及其主要函数

## PS 由于直接在网上搬的导入模块，所以就没有改类的名字(Example)
class Example(QWidget):
    # 初始化窗口实例
    def __init__(self):
        # 加载.ui文件
        super().__init__()
        self.ui = loadUi(r'targetDefender.ui', self)
        # 设置窗体标题
        self.ui.setWindowTitle("Target Defender")
        # 设置窗体图标
        #self.ui.setWindowIcon("")
        # 设置按钮绑定的动作
        self.ui.warningButton.clicked.connect(self.sendWarning)
        self.ui.startReceiving.clicked.connect(self.startListening)
        self.ui.stopReceiving.clicked.connect(self.stopListening)
        self.ui.testButton.clicked.connect(self.testShowWindow)
        # 初始化程序时，检查是否有监听或发报程序正在运行，如有则kill掉
        system('taskkill /im module_listen.exe /f')
        system('taskkill /im module_alarm.exe /f')
        # 全局化计数器
        global counter
        # 初始化成功提醒
        self.updateText("初始化成功")
    
    # 工具：更新状态框内容
    def updateText(self, text):
        global counter
        self.ui.lineEdit_status.setText(f"[{counter}]{text}")
        counter+=1


    # 操作：警报按钮
    def sendWarning(self):
        # 设置监听状态与计数器的全局变量
        global status, counter
        # 发出警报前先结束监听模块
        system('taskkill /im module_listen.exe /f')
        sleep(0.5)
        # 启动警报模块
        # Tip 运行程序使用start命令的原因：直接运行可执行文件需要等待程序结束才能继续执行代码，而start不需要
        system('start '+str(path.dirname(path.abspath(__file__) ))+'\\module_alarm.exe')
        sleep(0.5)
        # 如果事先就是监听模式，则重新把监听模块启动
        if status:
            system('start '+str(path.dirname(path.abspath(__file__) ))+'\\module_listen.exe')
        # 在程序最下面的状态框中输出操作结果，计数器+1
        self.ui.lineEdit_status.setText(f"[{counter}]发出警报成功")
        counter+=1

    # 操作：开始侦测按钮
    def startListening(self):
        global status,counter
        # 修改提示文字，设置status
        self.ui.label_status.setText('正在侦测')
        status = True
        # 结束警报模块如有，启动监听模块
        system('taskkill /im module_alarm.exe /f')
        system('start '+str(path.dirname(path.abspath(__file__) ))+'\\module_listen.exe')
        # 输出操作结果，计数器+1
        self.updateText('启动侦测成功')

    # 操作：停止侦测按钮
    def stopListening(self):
        global status,counter
        self.ui.label_status.setText('停止侦测')
        status = False
        system('taskkill /im module_listen.exe /f')
        self.updateText('结束侦测成功')

    # 操作：测试按钮
    def testShowWindow(self):
        global counter
        # 显示测试窗口
        MessageBox(0, '午时已到', '警报', MB_ICONWARNING)
        self.updateText('测试窗口出现成功')


############################################################### ELSE

# 如果该脚本作为主程序执行（而非作为模块被导入）
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    # 显示窗体
    ex.show()
    # 结束程序
    sys.exit(app.exec_())