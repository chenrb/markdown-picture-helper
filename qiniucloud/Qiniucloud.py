# -*- coding:utf-8 -*-
#!python2

__author__ = 'John 2018/2/27 22:27'

import os
import sys
import shutil
import re
from datetime import datetime

from qiniu import Auth, put_file


# 需要填写你的 Access Key 和 Secret Key
access_key = "******"
secret_key = "******"

# 要上传的空间
bucket_name = "******"

# 测试域名
bucket_url = "******"

img_suffix = ["jpg", "jpeg", "png", "bmp", "gif"]

# 转换结果
result_file = '{0}'.format(datetime.now().date())
md_url_txt = "{0}.txt".format(datetime.now().date())


# 获取当前文件夹需要上传的img文件
def get_local_img():
    img_list = []
    for file in os.listdir(sys.path[0]):
        if re.match('.*?(\.jpg|\.jpeg|\.png|\.bmp|\.gif)', file):
            img_list.append(file)
    return img_list


# 获取结果
def get_result(result_file, md_url_txt, bucket_url, key, localfile):
    # 创建归档的文件夹
    if not os.path.exists(result_file):
        os.mkdir(result_file)
    shutil.copy(localfile, os.path.join(sys.path[0], result_file))
    os.remove(localfile)

    img_url = 'http://%s/%s' % (bucket_url, key)
    md_url = '![%s](%s)\n' % (key, img_url)

    with open(md_url_txt, 'a') as f:
        f.write(md_url)
    return


if __name__ == '__main__':
    q = Auth(access_key, secret_key)
    img_list = get_local_img()
    for img in img_list:
        key = img.strip()  # 上传到七牛后保存的文件名
        token = q.upload_token(bucket_name, key, 3600)
        localfile = os.path.join(sys.path[0], img)  # 要上传文件的本地路径
        print '正在上传%s' % (localfile)
        info = put_file(token, key, localfile)
        get_result(result_file, md_url_txt, bucket_url, key, localfile)