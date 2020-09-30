#-*- coding:utf-8 -*-
import os
import sys
import time
import psutil
import glob
from psutil._common import bytes2human

def windows():
    now = time.strftime("%Y-%m-%d",time.localtime(time.time()))
    fname="./DeleteLog-"+now+r".log"
    savedStdout = sys.stdout
    f = open(fname,'a+')
    sys.stdout = f
    templ = "%-17s %8s %8s %8s %5s%% %9s  %s"
    for part in psutil.disk_partitions(all=False):
        if os.name == 'nt':
            if 'cdrom' in part.opts or part.fstype == '':
                continue
        usage = psutil.disk_usage(part.mountpoint)
        print('----------------------------------------------------------------------------')
        print(templ % ("Device", "Total", "Used", "Free", "Use ", "Type", "Mount"))
        print(templ % (
            part.device,
            bytes2human(usage.total),
            bytes2human(usage.used),
            bytes2human(usage.free),
            int(usage.percent),
            part.fstype,
            part.mountpoint))

        local_device = part.device;
        local_del_device = local_device.split(" ")
        excluded = ["C:\\"]
        dir_c = ["C:\\logs", "C:\\Users", "C:\\log", "C:\\home"]
        if local_del_device != excluded:
            path = dir_c + local_del_device;
            print(path)
            filename = ["**/*.log", "**/*.log.gz", "**/*.log.zip"]

            if path not in excluded:
                for del_file_name in filename:
                    for del_path in path:
                        for file in glob.iglob(del_path + del_file_name, recursive=True):
                            if os.path.isfile(file):
                                ltime = os.stat(file).st_mtime;
                                ntime = int(time.time())-2592000
                                if ltime<=ntime :
                                    #最后修改时间
                                    show_st_mitime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(os.stat(file).st_mtime))
                                    #文件大小，结果保留四位小数，单位为MB
                                    show_st_size = round(os.stat(file).st_size / 1024 / 1024,4)
                                    #删除并记录
                                    try:
                                        os.remove(file)
                                    except IOError:
                                        print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()), 'Error 删除文件失败，文件可能被占用：' + str(file), '最后修改时间:' + str(show_st_mitime), '文件大小:' + str(show_st_size) + 'MB' )
                                    else:
                                        print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()), '删除文件: ' + str(file), '最后修改时间:' + str(show_st_mitime), '文件大小:' + str(show_st_size) + 'MB' )
    f.close()

def linux():
    now = time.strftime("%Y-%m-%d",time.localtime(time.time()))
    fname="./DeleteLog-"+now+r".log"
    savedStdout = sys.stdout
    f = open(fname,'a+')
    sys.stdout = f
    templ = "%-17s %8s %8s %8s %5s%% %9s  %s"
    for part in psutil.disk_partitions(all=False):
        if os.name == 'nt':
            if 'cdrom' in part.opts or part.fstype == '':
                continue
        usage = psutil.disk_usage(part.mountpoint)
        print('----------------------------------------------------------------------------' )
        print(templ % ("Device", "Total", "Used", "Free", "Use ", "Type",
                   "Mount"))
        print(templ % (
            part.device,
            bytes2human(usage.total),
            bytes2human(usage.used),
            bytes2human(usage.free),
            int(usage.percent),
            part.fstype,
            part.mountpoint))

    path  = ["/home", "/mnt/logs", "/opt"]
    filename = ["/**/*.log", "/**/*.log.gz", "/**/*.log.zip"]

    for delpath in path:
        for del_file_name in filename:
            for file in glob.iglob(delpath + del_file_name, recursive=True):
                if os.path.isfile(file):
                    ltime = os.stat(file).st_mtime;
                    ntime = int(time.time())-604800
                    if ltime<=ntime :
                        #最后修改时间
                        show_st_mitime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(os.stat(file).st_mtime))
                        #文件大小，结果保留四位小数，单位为MB
                        show_st_size = round(os.stat(file).st_size / 1024 / 1024,4)
                        #删除并记录
                        try:
                            os.remove(file)
                        except IOError:
                            print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()), 'Error 删除文件失败，文件可能被占用：' + str(file), '最后修改时间:' + str(show_st_mitime), '文件大小:' + str(show_st_size) + 'MB' )
                        else:
                            print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()), '删除文件: ' + str(file), '最后修改时间:' + str(show_st_mitime), '文件大小:' + str(show_st_size) + 'MB' )
    f.close()

if os.name == 'nt':
    windows();
elif os.name == 'posix':
    linux();
