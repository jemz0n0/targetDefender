# targetDefender
基于UDP广播的局域网协助报警程序（适用于信息课等场景）

## 使用

### 封装流程
1. 使用`pyinstaller`对两个module进行封装
2. 封装`mainGUI`，并且添加两个已经封装好的module可执行文件
3. 使用Enigma Virtual Box将`.ui`文件添加至`mainGUI`文件内（否则需将`.ui`文件与主程序置于同一文件夹才可正常运行）

### Tip
- `pyinstaller`是Python的一个库，可以使用`pip`进行安装。建议同时安装`auto-py-to-exe`库，提供pyinstaller的可视化支持。使用方法为在cmd中执行

    ```bash
    auto-py-to-exe
    ```

    即可

- Enigma Virtual Box为第三方软件

## TODO

- 系统学习，避免补丁式的封装过程
