# -*- coding:utf-8 -*- 
__author__ = 'John 2018/2/28 14:33'

import os
import sys
import re
import shutil
from PIL import Image
from datetime import datetime

from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client

secret_id = '******'      # 替换为用户的 secretId
secret_key = '******'      # 替换为用户的 secretKey
region = '******'     # 替换为用户的 Region
bucket = '******'
token = ''                 # 使用临时秘钥需要传入Token，默认为空,可不填
config = CosConfig(Region=region, Secret_id=secret_id, Secret_key=secret_key, Token=token)  # 获取配置对象
client = CosS3Client(config)


# 获取当前文件夹需要上传的img文件
def get_local_img():
    img_list = []
    for file in os.listdir(sys.path[0]):
        if re.match('.*?(\.jpg|\.jpeg|\.png|\.bmp|\.gif|\.JPG|\.JPEG|\.PNG|\.BMP|\.GIF)', file):
            img_list.append(file)
    return img_list


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


# 获取结果
def get_result(bucket_url, file_name):
    result_file = '{0}'.format(datetime.now().date())
    md_url_txt = "{0}.txt".format(datetime.now().date())
    # 创建归档的文件夹
    if not os.path.exists(result_file):
        os.mkdir(result_file)
    shutil.copy(file_name, result_file)
    os.remove(file_name)

    img_url = 'http://%s/%s' % (bucket_url, file_name)
    md_url = '![%s](%s)\n' % (file_name, img_url)

    with open(md_url_txt, 'a') as f:
        f.write(md_url)
    return


if __name__ == "__main__":
    img_list = get_local_img()
    for img in img_list:
        # ImgTransformation(img)
        file_name = img
        with open(file_name, 'rb') as fp:
            response = client.put_object(
                Bucket=bucket,  # Bucket由bucketname-appid组成
                Body=fp,  # 上传的文件内容，类型为文件流或字节流
                Key=file_name,  # Key(string): COS路径.
            )
        bucket_url = bucket + '.cos.' + region + '.myqcloud.com'
        get_result(bucket_url, file_name)