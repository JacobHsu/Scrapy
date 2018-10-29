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

`$ scrapy crawl angelspider`

### Notes

angelspider.py  `http://www.angelimg.com/index/\d+` 翻頁規則


Scrapy\www.angelimg.com (master)  
`$ scrapy list` 查看當下有多少爬蟲  
> angelspider  

`$ scrapy crawl angelspider`  執行 
> Crawled (200) `<GET http://www.angelimg.com/index/2> (referer: http://www.angelimg.com/)`  

#### debug

[Python運行scrapy報錯:ImportError: No module named win32api](https://blog.csdn.net/u011781521/article/details/70170783)  
`$ pip install pypiwin32`