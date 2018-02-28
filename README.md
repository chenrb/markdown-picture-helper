## Markdown-Picture助手
这个脚本方便上传图片文件到七牛云/腾讯云，并得到可以在Markdown展示的图片链接。
### 七牛云Qiniucloud.py
[七牛云的Python SDK](https://developer.qiniu.com/kodo/sdk/1242/python)
```
	Python: Python2.7
    IED: Pycharm
    
    # 安装七牛云sdk
    pip install qiniu
    
    # 需要填写你的 Access Key 和 Secret Key
	access_key = "******"
	secret_key = "******"

	# 要上传的空间
	bucket_name = "******"

	# 测试域名
	bucket_url = "******"
```
1. 把图片文件复制到`Qiniucloud.py`所在文件夹；
2. 运行`Qiniucloud.py`；
3. 得到结果并按日期归档。

![qiniu.gif](http://ows764enq.bkt.clouddn.com/qiniu.gif)

### 腾讯云Qcloud.py
[腾讯云的Python SDK](hhttps://cloud.tencent.com/document/product/436/12270)
```
	Python: Python2.7
    IED: Pycharm
    
    # 安装腾讯云sdk
    pip install -U cos-python-sdk-v5
    
    secret_id = 'AKIDkIbeS0mK6csrcBSieNtBFArLdkdJ53EE'      # 替换为用户的 secretId
	secret_key = 'zkGWWGkyvc4JK7fXAXfZDbjgX8VeXAWe'      # 替换为用户的 secretKey
	region = 'ap-guangzhou'     # 替换为用户的 Region
	bucket = 'blog-1256123589'  # 替换为用户的存储桶
```
1. 把图片文件复制到`Qcloud.py`所在文件夹；
2. 运行`Qcloud.py`；
3. 得到结果并按日期归档。

![qcloud.gif](http://blog-1256123589.cos.ap-guangzhou.myqcloud.com/qcloud.gif)
