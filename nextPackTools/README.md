# 下一代python包管理工具pdm

使用方法：https://cloud.tencent.com/developer/article/1997107
官网：https://pdm.fming.dev/latest/

## 本项目创建方式

1.安装pdm
```shell
brew install pdm
```

2.常用命令
```shell
pdm self update
pdm --version
```

3.开启虚拟环境，创建package项目文件夹
```shell
conda activate dash-apps
pdm init
········开始填写项目基本信息
```

4.为项目安装三方库
```shell
pdm config pypi.url https://pypi.douban.com/simple/
pdm add -v flask flask-login
```

5.目录基本结构
```shell
pack
|
|__.pdm-build
|__.gitignore
|__.pdm-python
|__pdm.lock
|__pyproject.toml
|__readme.md
```

6.类似npm中的package.js的环境配置指令
```
如果你想要在其他路径或其他机器上还原某个pdm项目，则仅需要将pyproject.toml与pdm.lock文件拷贝过去，再在对应目录下执行pdm sync -v命令即可
```
7.可以使用build构建python包


8.可以使用twine上传构建的python包