# Linux命令学习

## 上传下载

```
yum install lrzsz
```

## 升级GCC

升级gcc 10.2.1

```
su root
yum install centos-release-scl
yum install devtoolset-10-gcc*
scl enable devtoolset-10 bash
gcc --version
vim ~/.bash_profile
```

在最后添加

```
source /opt/rh/devtoolset-10/enable
```

刷新

```
source ~/.bash_profile
```



## 解压tar.gz压缩包

tar -zxvf pg14.1.tar.gz

tar -zxvf JinFengKeJi-20220225-05.tar.gz

## file查看文件是x64还是x32

https://www.zhihu.com/question/23027723/answer/23396208
