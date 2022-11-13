# python包的构建和分发

早期pkg管理工具easy_install，现在已经被pip取代。

其他细节：https://packaging.python.org/en/latest/key_projects/

早期的包构建和分发工具**distutils**，将在python3.12之后被移除，彻底采用**setuptools**

distutils：https://docs.python.org/zh-cn/3/library/distutils.html

```
打包工具推荐
1.使用setuptools定义项目。
2.使用build创建Source Distributions和wheel。如果您有二进制扩展并希望为多个平台分发轮子，请使用cibuildwheel作为 CI 设置的一部分来构建可分发轮子。
3.使用twine将分布上传到PyPI。（需要先pypi创建账号）
```

**源码包**

![image-20221113225608404](readme.assets/image-20221113225608404.png)

**二进制包**

.gg包已经过时。

![image-20221113205804360](readme.assets/image-20221113205804360.png)

![image-20221113225628849](readme.assets/image-20221113225628849.png)

## 目前主流构建方式

默认环境

```
# build是python的命令行工具，可以通过它来快捷构建project
pip install --upgrade build wheel setuptools
```

推荐的构筑方式

```
# wheel 二进制格式
python3 -m build --wheel source-tree-directory
# sdist 源码格式
python3 -m build --sdist source-tree-directory
```

```
# 命令行工具
python -m build -h
```

### 配置文件的三种形式

```
# 使用setuptools时，需要的包配置文件。任选一种or三种自由组合。。。
pyproject.toml
setup.cfg
setup.py

# 这里我们选择官方推荐的.toml格式的配置文件（python 内置了）
```

### 目录结构

结构1

```
mypackage
├── pyproject.toml  # and/or setup.cfg/setup.py (depending on the configuration method)
├── # README.rst or README.md (a nice description of your package)
├── # LICENCE (properly chosen license information, e.g. MIT, BSD-3, GPL-3, MPL-2, etc...)
└── mypackage1
|   ├── __init__.py
|   └── ... (other Python files)
└── mypackage2
    ├── __init__.py
    └── ... (other Python files)
.....
```

**结构2**本人强烈推荐这种布局

![image-20221114020726416](readme.assets/image-20221114020726416.png)

结构3

![image-20221114020832832](readme.assets/image-20221114020832832.png)

### 配置文件参数

简单目录结构，可以自己检查所有package。但是总有意外。。。算法并不是无敌的。

高级包管理tool.setuptools.packages

```
# 方法一，字典配置包所在目录
[tool.setuptools.packages]
find = {}

# 方法二，列表配置，一项项来
[tool.setuptools.packages.find]
where = ["src"]  # ["."] by default
include = ["mypackage*"]  # ["*"] by default
exclude = ["mypackage.tests*"]  # empty by default
namespaces = false  # true by default
```

系统构建build-system

```
[build-system]
requires = ["setuptools", "setuptools-scm"]
build-backend = "setuptools.build_meta"
```

入口点project.scripts

```
除了对pkg中加入__main__.py，然后使用python -m pkg外。
可以设置脚本script, 直接将命令放入shell中。可以全局调用。
```

待补充。。









### 开始build

```
python -m build
```







## **twine分发**

官网https://twine.readthedocs.io/en/latest/

```
安装上传工具
pip install twine
```

### 注册pypi账号

https://pypi.org/manage/account/

![image-20221113225315151](readme.assets/image-20221113225315151.png)

推荐生成token API密钥，**配置$HOME/.pypirc**文件进行上传包。

### 常用命令

推荐使用token配置文件，进行无登录的上传package。

$HOME/.pypirc

https://packaging.python.org/en/latest/specifications/pypirc/

```
python -m build
上传到Test PyPI并验证一切是否正确：

# Twine 将提示您输入用户名和密码。（这里是即时login in）
# 也可以使用.pypirc进行无登录上传文件。
# 测试库
twine upload -r testpypi dist/*

# 上传到PyPI：
twine upload dist/*

# 检查发行库
twine check -h

# 存储库注册名称
twine register -h
```

```
# file: $HOME/.pypirc 用户目录下

# 启用服务
[distutils]
index-servers =
    pypi
    testpypi
    private-repository

# 正式上传服务器
[pypi]
username = __token__
password = <PyPI token>

# 测试上传服务器
[testpypi]
repository = https://test.pypi.org/legacy/
username = <your TestPyPI username>
password = <your TestPyPI password>

# 其他上传服务器
[private-repository]
repository = <private-repository URL>
username = <private-repository username>
password = <private-repository password>
```

## 其他

### 可执行文件

- [pyInstaller](https://pyinstaller.readthedocs.io/en/stable/) - 跨平台
- [cx_Freeze](https://marcelotduarte.github.io/cx_Freeze/) - 跨平台
- [构造函数](https://github.com/conda/constructor)- 用于命令行安装程序
- [py2exe](http://www.py2exe.org/) - 仅限 Windows
- [py2app](https://py2app.readthedocs.io/en/latest/) - 仅限 Mac
- [osnap](https://github.com/jamesabel/osnap) - Windows 和 Mac
- [pynsist](https://pypi.org/project/pynsist/) - 仅限 Windows