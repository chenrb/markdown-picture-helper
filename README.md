## Markdown-Picture助手
这个脚本方便上传图片文件到七牛云/腾讯云，并得到可以在Markdown展示的图片链接。
### Qiniucloud.py
[七牛云的Python SDK](https://developer.qiniu.com/kodo/sdk/1242/python)
```
	Python: Python2.7
    IED: Pycharm
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