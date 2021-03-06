# Scrapy

### pip install

`$ pip --version`  
`$ pip list`  
`$ pip install scrapy`  

> building 'twisted.test.raiser' extension  
>  error: [WinError 3] 系統找不到指定的路徑。: 'C:\\Program Files (x86)\\Microsoft Visual Studio 14.0\\VC\\Pla
tformSDK\\lib' 

[Unofficial Windows Binaries for Python Extension Packages](https://www.lfd.uci.edu/~gohlke/pythonlibs/)
download Twisted-18.9.0-cp36-cp36m-win32.whl


D:\chrome_download
`$ pip install Twisted-18.9.0-cp36-cp36m-win32.whl`  


`$ pip list`   
> Twisted-18.9.0-cp36-cp36m-win32.whl  

`$ pip install scrapy`   
`$ scrapy`  

C:\Users\Jacob\Desktop  
`$ scrapy startproject demo`  


### conda install
[Anaconda](https://www.anaconda.com/) is the most popular Python data science platform with 6 million users.
> `$ conda install scrapy=1.5`    


[angelimg](http://www.angelimg.com/)  
`$ scrapy startproject angelimg www.angelimg.com`

Scrapy\www.angelimg.com  
`$ scrapy genspider -t crawl angelspider www.angelimg.com`  
> spiders\angelspider.py


### Usage

Scrapy\www.angelimg.com (master)  
`$ scrapy crawl angelspider`

### Notes

angelspider.py  `http://www.angelimg.com/index/\d+` 翻頁規則


Scrapy\www.angelimg.com (master)  
`$ scrapy list` 查看當下有多少爬蟲  
> angelspider  

`$ scrapy crawl angelspider`  執行 
> Crawled (200) `<GET http://www.angelimg.com/index/2> (referer: http://www.angelimg.com/)`  


#### 圖片下載鏈接 

圖片的下載通常需要解決防盜鏈問題，也就是請求圖片內容需要指定請求頭部的Referer字段。   
只需要將Referer值寫成爬取的目標網站的域名。 

爬蟲的請求頭設置
settings.py
```
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
  'Referer':'http://www.angelimg.com',
}
```
####  圖片保存本地

得到圖片的鏈接，下載的話，可以使用scrapy內部的圖片管道

1. 在配置文件中註冊圖片管道
settings.py
```
ITEM_PIPELINES = {
   'scrapy.pipelines.images.ImagesPipeline': 300,
}

``` 
2. 指定存儲地址 
```
IMAGES_STORE = 'imgs'
```
檔案會在 imgs\full  

#### debug

[Python運行scrapy報錯:ImportError: No module named win32api](https://blog.csdn.net/u011781521/article/details/70170783)  
`$ pip install pypiwin32`

ImportError: No module named PIL 
`$ pip install Pillow`

chrome F12 / Ctrl+F5 打開搜索 `.//div[@id="content"]/a/img`  

from ..items import `AngelimgItem` 對應 items.py 的 class `AngelimgItem`  