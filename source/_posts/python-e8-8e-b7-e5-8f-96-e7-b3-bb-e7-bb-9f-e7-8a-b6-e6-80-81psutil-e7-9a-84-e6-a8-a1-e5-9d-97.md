---
title: python获取系统状态psutil的模块
id: 1420
categories:
  - Python
date: 2016-12-01 06:45:35
tags:
---

# 前言

最近需要一个可以实时访问系统信息的模块，网上搜索以后，发现了psutil可以大致满足我的要求。

# psutil简介

psutil(Python system and process utilities)是一个跨平台的进程管理和系统工具的python库，可以处理系统CPU，memory，disks，network等信息。主要用于系统资源的监控，分析，以及对进程进行一定的管理。通过psutil可以实现如`ps`，`top`，`lsof`，`netstat`，`ifconfig`， `who`，`df`，`kill`，`free`，`nice`，`ionice`，`iostat`，`iotop`，`uptime`，`pidof`，`tty`，`taskset`，`pmap`。在Linux，windows，OSX，freebsdSun，Solaris等系统上工作，最新的版本python是要高于2.6(Python 2.4 Python2.5 可以用2.1.3版本)

# 安装

首先确定下当前系统有没有psutil模块

```python
import psutil
```


如果有的话，就直接导入模块成功，如果没有，就会提示错误然后到官网上下载psutil-2.0.0.tar.gz源码包

```sh
tar -zxf psutil-2.0.0.tar.gz & cd psutil-2.0.0
python setup.py install
```


也可以直接使用pip install psutil 来安装

# 系统相关功能

## CPU信息

### cpu_times

```python
psutil.cpu_times(precpu=False) 
```


返回系统CPU运行时间的元组，时间为秒。

### cpu_percent

```python
psutil.cpu_percent(interval=None, percpu=False)
```


返回一个浮点数，代表当前cpu的利用率的百分比，包括sy+user. 当`interval`为0或者None时，表示的是interval时间内的sys的利用率。 当`percpu`为True返回是每一个cpu的利用率。

### cpu_count

```python
psutil.cpu_count()
```


返回CPU的逻辑个数

```python
psutil.cpu_count(logical=True)
```


返回CPU的物理个数

## 内存

```python
psutil.virtual_memory()
```


返回一个内存信息的元组，大小为字节

*   total: 内存的总大小.
*   available: 可以用来的分配的内存，不同系统计算方式不同； Linux下的计算公式:free+ buffers +cached
*   percent: 已经用掉内存的百分比 (total - available) / total 100.
*   used: 已经用掉内存大小，不同系统计算方式不同
*   *free: 空闲未被分配的内存，Linux下不包括buffers和cached

Platform-specific fields:

*   active: (UNIX): 最近使用内存和正在使用内存。
*   inactive: (UNIX): 已经分配但是没有使用的内存
*   buffers: (Linux, BSD): 缓存，linux下的Buffers
*   cached:(Linux, BSD): 缓存，Linux下的cached.
*   wired: (BSD, OSX): 一直存在于内存中的部分，不会被移除
*   shared: (BSD): 缓存

内存总大小不等于Used+available,在windows系统可用内存和空闲内存是用一个。

```default
psutil.swap_memory()
```


返回系统的swap信息

*   total: swap的总大小 单位为字节
*   used: 已用的swap大小 bytes
*   free: 空闲的swap大小 bytes
*   percent: 已用swap的百分比
*   sin: 从磁盘调入是swap的大小
*   sout: 从swap调出到disk的大小
> `sin`，` sout`在windows**没有意义**。

## 分区

```python
psutil.disk_partitions(all=False)
```


返回所有挂载的分区的信息的列表，列表中的每一项类似于df命令的格式输出，包括分区，挂载点，文件系统格式，挂载参数等，会忽略掉`/dev/shm`,`/proc/filesystem`等，windows上分区格式 "`removable`", "`fixed`", "`remote`", "`cdrom`", "`unmounted`" or "`ramdisk`"。

```default
>>> import psutil
>>> psutil.disk_partitions()
[sdiskpart(device='/dev/sda3', mountpoint='/', fstype='ext4', opts='rw,errors=remount-ro'),
 sdiskpart(device='/dev/sda7', mountpoint='/home', fstype='ext4', opts='rw')]
```

```python
psutil.disk_usage(path) 
```


返回硬盘，分区或者目录的使用情况，单位字节

如果不存在会报“`OSError`”错误。

```default
>>> import psutil
>>> psutil.disk_usage('/')
sdiskusage(total=21378641920, used=4809781248, free=15482871808, percent=22.5)
```

```python
psutil.disk_io_counters(perdisk=False)
```


返回当前磁盘的io情况

*   read_count: number of reads
*   write_count: number of writes
*   read_bytes: number of bytes read
*   write_bytes: number of bytes written
*   read_time: time spent reading from disk (in milliseconds)
*   write_time: time spent writing to disk (in milliseconds)

## 网络信息

返回整个系统的网络信息

```python
psutil.net_io_counters(pernic=False)
```


*   bytes_sent: 发送的字节数
*   bytes_recv: 接收的字节数
*   packets_sent: 发送到数据包的个数
*   packets_recv: 接受的数据包的个数
*   errin:
*   errout: 发送数据包错误的总数
*   dropin: 接收时丢弃的数据包的总数
*   dropout: 发送时丢弃的数据包的总数(OSX和BSD系统总是0)

如果 `pernic`值为True，会显示具体各个网卡的信息。

```default
>>> import psutil
>>> psutil.net_io_counters()
snetio(bytes_sent=14508483, bytes_recv=62749361, packets_sent=84311, packets_recv=94888, errin=0, errout=0, dropin=0, dropout=0)
>>>
>>> psutil.net_io_counters(pernic=True)
{'lo': snetio(bytes_sent=547971, bytes_recv=547971, packets_sent=5075, packets_recv=5075, errin=0, errout=0, dropin=0, dropout=0),
'wlan0': snetio(bytes_sent=13921765, bytes_recv=62162574, packets_sent=79097, packets_recv=89648, errin=0, errout=0, dropin=0, dropout=0)}
```

```python
psutil.net_connections(kind='inet') 
```


返回系统的整个socket连接的信息，可以选择查看哪些类型的连接信息，类似于netstat命令

 

**fd**:

 **family**: the address family, either AF_INET, AF_INET6 or AF_UNIX.

 **type**: the address type, either SOCK_STREAM or SOCK_DGRAM.

 **laddr**: the local address as a (ip, port) tuple or a path in case of AF_UNIX sockets.

 **raddr**: the remote address as a (ip, port) tuple or an absolute path in case of UNIX sockets. When the remote endpoint is not connected you’ll **get an empty tuple (AF_INET*) or None (AF_UNIX). On Linux AF_UNIX sockets will always have this set to None. **status**: represents the status of a TCP connection. The return value is one of the psutil.CONN_* constants (a string). For UDP and UNIX **sockets this is always going to be psutil.CONN_NONE.

 **pid**: the PID of the process which opened the socket, if retrievable, else None. On some platforms (e.g. Linux) the availability of this field **changes depending on process privileges (root is needed).

参数kind的类型：

 “inet” IPv4 and IPv6

 “inet4” IPv4

 “inet6” IPv6

 “tcp” TCP

 “tcp4” TCP over IPv4

 “tcp6” TCP over IPv6

 “udp” UDP

 “udp4” UDP over IPv4

 “udp6” UDP over IPv6

 “unix” UNIX socket (both UDP and TCP protocols)

 “all” the sum of all the possible families and protocols

    >>>
    >>> import psutil
    >>> psutil.net_connections()
    [pconn(fd=115, family=2, type=1, laddr=('10.0.0.1', 48776), raddr=('93.186.135.91', 80), status='ESTABLISHED', pid=1254),
     pconn(fd=117, family=2, type=1, laddr=('10.0.0.1', 43761), raddr=('72.14.234.100', 80), status='CLOSING', pid=2987),
     pconn(fd=-1, family=2, type=1, laddr=('10.0.0.1', 60759), raddr=('72.14.234.104', 80), status='ESTABLISHED', pid=None),
     pconn(fd=-1, family=2, type=1, laddr=('10.0.0.1', 51314), raddr=('72.14.234.83', 443), status='SYN_SENT', pid=None)
     ...]`
```


    ## Other system info

    `psutil.users()`

     返回当前系统用户登录信息

    **user**: 用户的名称

     **terminal**: 运行终端，tty还是pts等

     **host**: 登录的IP

     **started**: 登录了多长时间

    
```
`>>>
    >>> import psutil
    >>> psutil.users()
    [suser(name='giampaolo', terminal='pts/2', host='localhost', started=1340737536.0),
     suser(name='giampaolo', terminal='pts/3', host='localhost', started=1340737792.0)]`
```


    `psutil.boot_time()`

     返回当前的时间

    
```
`>>>
    >>> import psutil, datetime
    >>> psutil.boot_time()
    1389563460.0
    >>> datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
    '2014-01-12 22:51:00'`
```


    * * *

    ## Processes

    ### Functions

    `psutil.pids()`

     返回当前运行的进程pid列表

    `psutil.pid_exists(pid)`

     是否存在次pid，快速的验证方式`pid in psutil.pids()`

    `psutil.process_iter()`

     返回一个包含Process对象的迭代器。每一个对象只创建一次，创建后缓存起来。当一个进程更新时，会更新缓存。遍历所有进程首选psutil.pids().迭代器排序是根据pid。

    
```
`import psutil

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name'])
        except psutil.NoSuchProcess:
            pass
        else:
            print(pinfo)`
```


    `psutil.wait_procs(procs, timeout=None, callback=None)`

    Convenience function which waits for a list of Process instances to terminate. Return a (gone, alive) tuple indicating which processes are gone and which ones are still alive. The gone ones will have a new returncode attribute indicating process exit status (it may be None). callback is a function which gets called every time a process terminates (a Process instance is passed as callback argument). Function will return as soon as all processes terminate or when timeout occurs. Tipical use case is:

    send SIGTERM to a list of processes

     give them some time to terminate

     send SIGKILL to those ones which are still alive

    Example:

    
```
`import psutil

    def on_terminate(proc):
        print("process {} terminated".format(proc))

    procs = [...]  # a list of Process instances
    for p in procs:
        p.terminate()
    gone, alive = wait_procs(procs, timeout=3, callback=on_terminate)
    for p in alive:
        p.kill()`
```


    ### Exceptions

    `class psutil.Error`

     基础异常，psutil的其他异常都继承这个

    `class psutil.NoSuchProcess(pid, name=None, msg=None)`

     当进程不在进程列表中，或者进程不存在时触发。

    `class psutil.AccessDenied(pid=None, name=None, msg=None)`

     没有权限时，被触发

    `class psutil.TimeoutExpired(seconds, pid=None, name=None, msg=None)`

     当Process.wait() 超时，并且Process 一直在运行时.

    # psutil

    标签（空格分隔）： Python

    * * *

    ## Process class

    `class psutil.Process(pid=None)`

     Process类是一个带有pid的进程。如果没有指定pid，则默认的进程为`os.getpid()`所得进程。Process会触发`NoSuchProcess`（当进程不存在时）和`AccessDenied`异常，

    **注意**

    > Process是通过pid绑定的。如果在一个Process实例，在psutil运行中pid进程死掉，而
> 
>      这个pid又绑定给了别的新的进程。为了保证Process的安全性可以通过pid+createion time
> 
>      方式来确认进程是否是同一个。

    `pid`

     进程的PID

    `ppid()`

     父进程pid. On Windows the return value is cached after first call.

    `name()`

     进程名.

    `exe()`

     进程运行命令的绝对路径。

    `cmdline()`

     The command line this process has been called with.

    `create_time()`

     进程创建时间

    
```
`>>>
    >>> import psutil, datetime
    >>> p = psutil.Process()
    >>> p.create_time()
    1307289803.47
    >>> datetime.datetime.fromtimestamp(p.create_time()).strftime("%Y-%m-%d %H:%M:%S")
    '2011-03-05 18:03:52'`
```


    `as_dict(attrs=None, ad_value=None)`

     返回进程信息的哈希字典的实用方法，`attrs`指定的值必须是Process的属性值，例如（['cpu_times','name']）

    
```
`>>>
    >>> import psutil
    >>> p = psutil.Process()
    >>> p.as_dict(attrs=['pid', 'name', 'username'])
    {'username': 'giampaolo', 'pid': 12366, 'name': 'python'}`
```


    `parent()`

     返回父进程，如果不存在父进程，则返回None。

    `status()`

     进程当前运行状态，string形式。

    `cwd()`

     进程运行的所在的目录

    `username()`

     哪个用户下运行的进程

    `uids()`

     返回real=uid，effective，saved用户的uid

    **Availability**: UNIX

    `gids()`

    **Availability**: UNIX

    `terminal()`

     The terminal associated with this process, if any, else None. This is similar to “tty” command but can be used for every process PID.

    **Availability**: UNIX

    `nice(value=None)`

     获取或者设置进程的nice值，

    
```
`>>>
    >>> import psutil
    >>> p = psutil.Process()
    >>> p.nice(10)  # set
    >>> p.nice()  # get
    10
    >>>`
```


    在windows系统上，只能通过`GetProrityClass`和`SetPriorityClass`的`psutil.*_PRIORITY_CLASS`包含的值来设定

    
```
`>>>
    >>> p.nice(psutil.HIGH_PRIORITY_CLASS)`
```


    `ionice(ioclass=None, value=None)`

     获取或者设置进程I/O的优先级。Linux上的`ioclass`的值`psutil.IOPRO_CLASS_*`值在0-7，windows 2 为正常，1为优先级低，0为非常低。

    
```
`>>>
    >>> import psutil
    >>> p = psutil.Process()
    >>> p.ionice(psutil.IOPRIO_CLASS_IDLE)  # set
    >>> p.ionice()  # get
    pionice(ioclass=3, value=0)
    >>>`
```


    `rlimit(resource, limits=None)`

     Get or set process resource limits (see man prlimit). resource is one of the psutil.RLIMIT_* constants. limits is a (soft, hard) tuple. This is the same as resource.getrlimit() and resource.setrlimit() but can be used for every process PID and only on Linux. Example:

    
```
`>>>
    >>> import psutil
    >>> p = psutil.Process()
    >>> # process may open no more than 128 file descriptors
    >>> p.rlimit(psutil.RLIMIT_NOFILE, (128, 128))
    >>> # process may create files no bigger than 1024 bytes
    >>> p.rlimit(psutil.RLIMIT_FSIZE, (1024, 1024))
    >>> # get
    >>> p.rlimit(psutil.RLIMIT_FSIZE)
    (1024, 1024)
    >>>`
```


    **Availability**: Linux

    `io_counters()`

     返回这个进程的IO情况

    
```
`>>>
    >>> import psutil
    >>> p = psutil.Process()
    >>> p.io_counters()
    pio(read_count=454556, write_count=3456, read_bytes=110592, write_bytes=0)`
```


    **Availability**: all platforms except OSX

    `num_ctx_switches()`

     The number voluntary and involuntary context switches performed by this process.

    `num_fds()`

     The number of file descriptors used by this process.

    **Availability**: UNIX

    `num_handles()`

     The number of handles used by this process.

    **Availability**: Windows

    `num_threads()`

     The number of threads currently used by this process.

    `threads()`

     Return threads opened by process as a list of namedtuples including thread id and thread CPU times (user/system).

    `cpu_times()`

     Return a tuple whose values are process CPU user and system times which means the amount of time expressed in seconds that a process has spent in user / system mode. This is similar to os.times() but can be used for every process PID.

    `cpu_percent(interval=None)`

     Return a float representing the process CPU utilization as a percentage. When interval is > 0.0 compares process times to system CPU times elapsed before and after the interval (blocking). When interval is 0.0 or None compares process times to system CPU times elapsed since last call, returning immediately. That means the first time this is called it will return a meaningless 0.0 value which you are supposed to ignore. In this case is recommended for accuracy that this function be called a second time with at least 0.1 seconds between calls. Example:

    
```
`>>>
    >>> import psutil
    >>> p = psutil.Process()
    >>>
    >>> # blocking
    >>> p.cpu_percent(interval=1)
    2.0
    >>> # non-blocking (percentage since last call)
    >>> p.cpu_percent(interval=None)
    2.9
    >>>`
```


    Note a percentage > 100 is legitimate as it can result from a process with multiple threads running on different CPU cores.

     Warning the first time this method is called with interval = 0.0 or None it will return a meaningless 0.0 value which you are supposed to ignore.

     cpu_affinity(cpus=None)

     Get or set process current CPU affinity. CPU affinity consists in telling the OS to run a certain process on a limited set of CPUs only. The number of eligible CPUs can be obtained with list(range(psutil.cpu_count())).

    
```
`>>>
    >>> import psutil
    >>> psutil.cpu_count()
    4
    >>> p = psutil.Process()
    >>> p.cpu_affinity()  # get
    [0, 1, 2, 3]
    >>> p.cpu_affinity([0])  # set; from now on, process will run on CPU #0 only
    >>> p.cpu_affinity()
    [0]
    >>>
    >>> # reset affinity against all CPUs
    >>> all_cpus = list(range(psutil.cpu_count()))
    >>> p.cpu_affinity(all_cpus)
    >>>`
```


    **Availability**: Linux, Windows, BSD

    Changed in version 2.2.0: added support for FreeBSD

    `memory_info()`

     Return a tuple representing RSS (Resident Set Size) and VMS (Virtual Memory Size) in bytes. On UNIX rss and vms are the same values shown by ps. On Windows rss and vms refer to “Mem Usage” and “VM Size” columns of taskmgr.exe. For more detailed memory stats use memory_info_ex().

    `memory_info_ex()`

     Return a namedtuple with variable fields depending on the platform representing extended memory information about the process. All numbers are expressed in bytes.

    <table>
    <thead>
    <tr>
    <th>Linux</th>
    <th>OSX</th>
    <th>BSD</th>
    <th>SunOS</th>
    <th>Windows</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>rss</td>
    <td>rss</td>
    <td>rss</td>
    <td>rss</td>
    <td>num_page_faults</td>
    </tr>
    <tr>
    <td>vms</td>
    <td>vms</td>
    <td>vms</td>
    <td>vms</td>
    <td>peak_wset</td>
    </tr>
    <tr>
    <td>shared</td>
    <td>pfaults</td>
    <td>text</td>
    <td> </td>
    <td>wset</td>
    </tr>
    <tr>
    <td>text</td>
    <td>pageins</td>
    <td>data</td>
    <td> </td>
    <td>peak_paged_pool</td>
    </tr>
    <tr>
    <td>lib</td>
    <td> </td>
    <td>stack</td>
    <td> </td>
    <td>paged_pool</td>
    </tr>
    <tr>
    <td>data</td>
    <td> </td>
    <td> </td>
    <td> </td>
    <td>peak_nonpaged_pool</td>
    </tr>
    <tr>
    <td>dirty</td>
    <td> </td>
    <td> </td>
    <td> </td>
    <td>nonpaged_pool</td>
    </tr>
    <tr>
    <td> </td>
    <td> </td>
    <td> </td>
    <td> </td>
    <td>pagefile</td>
    </tr>
    <tr>
    <td> </td>
    <td> </td>
    <td> </td>
    <td> </td>
    <td>peak_pagefile</td>
    </tr>
    <tr>
    <td> </td>
    <td> </td>
    <td> </td>
    <td> </td>
    <td>private</td>
    </tr>
    </tbody>
    </table>

    Windows metrics are extracted from PROCESS_MEMORY_COUNTERS_EX structure. Example on Linux:

    
```
`>>>
    >>> import psutil
    >>> p = psutil.Process()
    >>> p.memory_info_ex()
    pextmem(rss=15491072, vms=84025344, shared=5206016, text=2555904, lib=0, data=9891840, dirty=0)`
```


    `memory_percent()`

     Compare physical system memory to process resident memory (RSS) and calculate process memory utilization as a percentage.

    `memory_maps(grouped=True)`

     Return process’s mapped memory regions as a list of nameduples whose fields are variable depending on the platform. As such, portable applications should rely on namedtuple’s path and rss fields only. This method is useful to obtain a detailed representation of process memory usage as explained here. If grouped is True the mapped regions with the same path are grouped together and the different memory fields are summed. If grouped is False every mapped region is shown as a single entity and the namedtuple will also include the mapped region’s address space (addr) and permission set (perms). See examples/pmap.py for an example application.

    
```
`>>>
    >>> import psutil
    >>> p = psutil.Process()
    >>> p.memory_maps()
    [pmmap_grouped(path='/lib/x8664-linux-gnu/libutil-2.15.so', rss=16384, anonymous=8192, swap=0),
     pmmap_grouped(path='/lib/x8664-linux-gnu/libc-2.15.so', rss=6384, anonymous=15, swap=0),
     pmmap_grouped(path='/lib/x8664-linux-gnu/libcrypto.so.0.1', rss=34124, anonymous=1245, swap=0),
     pmmap_grouped(path='[heap]', rss=54653, anonymous=8192, swap=0),
     pmmap_grouped(path='[stack]', rss=1542, anonymous=166, swap=0),
     ...]
    >>>`
```


    `children(recursive=False)`

     Return the children of this process as a list of Process objects, pre-emptively checking whether PID has been reused. If recursive is True return all the parent descendants. Example assuming A == this process:

    A ─┐

     │

     ├─ B (child) ─┐

     │ └─ X (grandchild) ─┐

     │ └─ Y (great grandchild)

     ├─ C (child)

     └─ D (child)

    
```
`>>> p.children()
    B, C, D
    >>> p.children(recursive=True)
    B, X, Y, C, D`
```


    Note that in the example above if process X disappears process Y won’t be returned either as the reference to process A is lost.

    `open_files()`

     Return regular files opened by process as a list of namedtuples including the absolute file name and the file descriptor number (on Windows this is always -1). Example:

    
```
`>>>
    >>> import psutil
    >>> f = open('file.ext', 'w')
    >>> p = psutil.Process()
    >>> p.open_files()
    [popenfile(path='/home/giampaolo/svn/psutil/file.ext', fd=3)]`
```


    `connections(kind="inet")`

     Return socket connections opened by process as a list of namedutples. To get system-wide connections use psutil.net_connections(). Every namedtuple provides 6 attributes:

    **fd:** the socket file descriptor. This can be passed to socket.fromfd() to obtain a usable socket object. This is only available on UNIX; on Windows -1 is always returned.

     **family:** the address family, either AF_INET, AF_INET6 or AF_UNIX.

     **type:** the address type, either SOCK_STREAM or SOCK_DGRAM.

     **laddr:** the local address as a (ip, port) tuple or a path in case of AF_UNIX sockets.

     **raddr:** the remote address as a (ip, port) tuple or an absolute path in case of UNIX sockets. When the remote endpoint is not connected you’ll get an empty tuple (AF_INET) or None (AF_UNIX). On Linux AF_UNIX sockets will always have this set to None.

     **status:** represents the status of a TCP connection. The return value is one of the psutil.CONN_* constants. For UDP and UNIX sockets this is always going to be `psutil.CONN_NONE`.

    The kind parameter is a string which filters for connections that fit the following criteria:

    <table>
    <thead>
    <tr>
    <th>Kind value</th>
    <th>Connections using</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>“inet”</td>
    <td>IPv4 and IPv6</td>
    </tr>
    <tr>
    <td>“inet4”</td>
    <td>IPv4</td>
    </tr>
    <tr>
    <td>“inet6”</td>
    <td>IPv6</td>
    </tr>
    <tr>
    <td>“tcp”</td>
    <td>TCP</td>
    </tr>
    <tr>
    <td>“tcp4”</td>
    <td>TCP over IPv4</td>
    </tr>
    <tr>
    <td>“tcp6”</td>
    <td>TCP over IPv6</td>
    </tr>
    <tr>
    <td>“udp”</td>
    <td>UDP</td>
    </tr>
    <tr>
    <td>“udp4”</td>
    <td>UDP over IPv4</td>
    </tr>
    <tr>
    <td>“udp6”</td>
    <td>UDP over IPv6</td>
    </tr>
    <tr>
    <td>“unix”</td>
    <td>UNIX socket (both UDP and TCP protocols)</td>
    </tr>
    <tr>
    <td>“all”</td>
    <td>the sum of all the possible families and protocols</td>
    </tr>
    </tbody>
    </table>

    Example:

    
```
`>>>
    >>> import psutil
    >>> p = psutil.Process(1694)
    >>> p.name()
    'firefox'
    >>> p.connections()
    [pconn(fd=115, family=2, type=1, laddr=('10.0.0.1', 48776), raddr=('93.186.135.91', 80), status='ESTABLISHED'),
     pconn(fd=117, family=2, type=1, laddr=('10.0.0.1', 43761), raddr=('72.14.234.100', 80), status='CLOSING'),
     pconn(fd=119, family=2, type=1, laddr=('10.0.0.1', 60759), raddr=('72.14.234.104', 80), status='ESTABLISHED'),
     pconn(fd=123, family=2, type=1, laddr=('10.0.0.1', 51314), raddr=('72.14.234.83', 443), status='SYN_SENT')]`
```


    `is_running()`

     判断进程是否存活

     Return whether the current process is running in the current process list. This is reliable also in case the process is gone and its PID reused by another process, therefore it must be preferred over doing psutil.pid_exists(p.pid).

    Note this will return True also if the process is a zombie (p.status() == psutil.STATUS_ZOMBIE).

     `send_signal(signal)`

     发送新号给进程

     Send a signal to process (see signal module constants) pre-emptively checking whether PID has been reused. This is the same as os.kill(pid, sig). On Windows only SIGTERM is valid and is treated as an alias for kill().

    `suspend()`

     Suspend process execution with SIGSTOP signal pre-emptively checking whether PID has been reused. On UNIX this is the same as os.kill(pid, signal.SIGSTOP). On Windows this is done by suspending all process threads execution.

    `resume()`

     Resume process execution with SIGCONT signal pre-emptively checking whether PID has been reused. On UNIX this is the same as os.kill(pid, signal.SIGCONT). On Windows this is done by resuming all process threads execution.

    `terminate()`

     Terminate the process with SIGTERM signal pre-emptively checking whether PID has been reused. On UNIX this is the same as os.kill(pid, signal.SIGTERM). On Windows this is an alias for kill().

    `kill()`

     Kill the current process by using SIGKILL signal pre-emptively checking whether PID has been reused. On UNIX this is the same as os.kill(pid, signal.SIGKILL). On Windows this is done by using TerminateProcess.

    `wait(timeout=None)`

     Wait for process termination and if the process is a children of the current one also return the exit code, else None. On Windows there’s no such limitation (exit code is always returned). If the process is already terminated immediately return None instead of raising NoSuchProcess. If timeout is specified and process is still alive raise TimeoutExpired exception. It can also be used in a non-blocking fashion by specifying timeout=0 in which case it will either return immediately or raise TimeoutExpired. To wait for multiple processes use psutil.wait_procs().

    ### Popen class

    `class psutil.Popen(*args, **kwargs)`

     A more convenient interface to stdlib subprocess.Popen. It starts a sub process and deals with it exactly as when using subprocess.Popen but in addition it also provides all the methods of psutil.Process class in a single interface. For method names common to both classes such as send_signal(), terminate() and kill() psutil.Process implementation takes precedence. For a complete documentation refer to subprocess module documentation.

    Note Unlike subprocess.Popen this class pre-emptively checks wheter PID has been reused on send_signal(), terminate() and kill() so that you don’t accidentally terminate another process, fixing [http://bugs.python.org/issue6973](http://bugs.python.org/issue6973).

    
```
`>>>
    >>> import psutil
    >>> from subprocess import PIPE
    >>>
    >>> p = psutil.Popen(["/usr/bin/python", "-c", "print('hello')"], stdout=PIPE)
    >>> p.name()
    'python'
    >>> p.username()
    'giampaolo'
    >>> p.communicate()
    ('hello\n', None)
    >>> p.wait(timeout=2)
    0
    >>>

### Constants

> psutil.STATUS_RUNNING
> 
>  psutil.STATUS_SLEEPING
> 
>  psutil.STATUS_DISK_SLEEP
> 
>  psutil.STATUS_STOPPED
> 
>  psutil.STATUS_TRACING_STOP
> 
>  psutil.STATUS_ZOMBIE
> 
>  psutil.STATUS_DEAD
> 
>  psutil.STATUS_WAKE_KILL
> 
>  psutil.STATUS_WAKING
> 
>  psutil.STATUS_IDLE
> 
>  psutil.STATUS_LOCKED
> 
>  psutil.STATUS_WAITING

A set of strings representing the status of a process. Returned by psutil.Process.status().

> psutil.CONN_ESTABLISHED
> 
>  psutil.CONN_SYN_SENT
> 
>  psutil.CONN_SYN_RECV
> 
>  psutil.CONN_FIN_WAIT1
> 
>  psutil.CONN_FIN_WAIT2
> 
>  psutil.CONN_TIME_WAIT
> 
>  psutil.CONN_CLOSE
> 
>  psutil.CONN_CLOSE_WAIT
> 
>  psutil.CONN_LAST_ACK
> 
>  psutil.CONN_LISTEN
> 
>  psutil.CONN_CLOSING
> 
>  psutil.CONN_NONE
> 
>  psutil.CONN_DELETE_TCB(Windows)
> 
>  psutil.CONN_IDLE(Solaris)
> 
>  psutil.CONN_BOUND(Solaris)

A set of strings representing the status of a TCP connection. Returned by psutil.Process.connections() (status field).

> psutil.ABOVE_NORMAL_PRIORITY_CLASS
> 
>  psutil.BELOW_NORMAL_PRIORITY_CLASS
> 
>  psutil.HIGH_PRIORITY_CLASS
> 
>  psutil.IDLE_PRIORITY_CLASS
> 
>  psutil.NORMAL_PRIORITY_CLASS
> 
>  psutil.REALTIME_PRIORITY_CLASS
> 
>  A set of integers representing the priority of a process on Windows (see MSDN documentation). They can be used in conjunction with psutil.Process.nice() to get or set process priority.

**Availability**: Windows

psutil.IOPRIO_CLASS_NONE

 psutil.IOPRIO_CLASS_RT

 psutil.IOPRIO_CLASS_BE

 psutil.IOPRIO_CLASS_IDLE

 A set of integers representing the I/O priority of a process on Linux. They can be used in conjunction with psutil.Process.ionice() to get or set process I/O priority. IOPRIO_CLASS_NONE and IOPRIO_CLASS_BE (best effort) is the default for any process that hasn’t set a specific I/O priority. IOPRIO_CLASS_RT (real time) means the process is given first access to the disk, regardless of what else is going on in the system. IOPRIO_CLASS_IDLE means the process will get I/O time when no-one else needs the disk. For further information refer to manuals of ionice command line utility or ioprio_get system call.

**Availability**: Linux

> psutil.RLIMIT_INFINITY
> 
>  psutil.RLIMIT_AS
> 
>  psutil.RLIMIT_CORE
> 
>  psutil.RLIMIT_CPU
> 
>  psutil.RLIMIT_DATA
> 
>  psutil.RLIMIT_FSIZE
> 
>  psutil.RLIMIT_LOCKS
> 
>  psutil.RLIMIT_MEMLOCK
> 
>  psutil.RLIMIT_MSGQUEUE
> 
>  psutil.RLIMIT_NICE
> 
>  psutil.RLIMIT_NOFILE
> 
>  psutil.RLIMIT_NPROC
> 
>  psutil.RLIMIT_RSS
> 
>  psutil.RLIMIT_RTPRIO
> 
>  psutil.RLIMIT_RTTIME
> 
>  psutil.RLIMIT_RTPRIO
> 
>  psutil.RLIMIT_SIGPENDING
> 
>  psutil.RLIMIT_STACK
> 
>  Constants used for getting and setting process resource limits to be used in conjunction with psutil.Process.rlimit(). See man prlimit for futher information.

**Availability**: Linux