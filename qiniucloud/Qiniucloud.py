# -*- coding:utf-8 -*-
#!python2

__author__ = 'John 2018/2/27 22:27'

import os
import sys
import shutil
import re
from PIL import Image
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


# 获取当前文件夹需要上传的img文件
def get_local_img():
    img_list = []
    for file in os.listdir(sys.path[0]):
        if re.match('.*?(\.jpg|\.jpeg|\.png|\.bmp|\.gif|\.JPG|\.JPEG|\.PNG|\.BMP|\.GIF)', file):
            img_list.append(file)
    return img_list


# 获取结果
def get_result(bucket_url, key, localfile):
    result_file = '{0}'.format(datetime.now().date())
    md_url_txt = "{0}.txt".format(datetime.now().date())
    # 创建归档的文件夹
    if not os.path.exists(result_file):
        os.mkdir(result_file)
    shutil.copy(localfile, result_file)
    os.remove(localfile)

    img_url = 'http://%s/%s' % (bucket_url, key)
    md_url = '![%s](%s)\n' % (key, img_url)

    with open(md_url_txt, 'a') as f:
        f.write(md_url)
    return


# 若图片过大，可执行该函数
def ImgTransformation(img):
    im = Image.open(img)
    print('格式', im.format, '，分辨率', im.size, '，色彩', im.mode)
    if max(im.size[0], im.size[1]) > 1000:
        if im.size[0] > im.size[1]:
            im.thumbnail((1280, 1280))
        else:
            im.thumbnail((1000, 1000))
        im.save(img, 'JPEG', quality=90)
    return 'OK'


if __name__ == '__main__':
    q = Auth(access_key, secret_key)
    img_list = get_local_img()
    for img in img_list:
        key = img.strip()  # 上传到七牛后保存的文件名
        token = q.upload_token(bucket_name, key, 3600)
        localfile = os.path.join(sys.path[0], img)  # 要上传文件的本地路径
        print '正在上传%s' % (localfile)
        info = put_file(token, key, localfile)
        get_result(bucket_url, key, localfile)