#数据库设计

#创建blog数据库

# 包括user表,post(文章)表,content表

#user表:包含以下字段
        #id:唯一标识
        #name:用户名
        #email:注册用信息,应该唯一,可做登陆名
        #passwd:密码.MD5单向加密

#post表:包含以下字段
        #id:
        #title:
        #author:
        #postdate:发布日期,日期类型
        #content:文章内容,博文内容可能很长,不小于256个字符
        #        (考虑:
        #              字段类型:大文本,TEXT
        #              大小:longtest                                           )
        #              图片存储:博文类似HTMl,图片是通过路径信息将图片嵌入在内容中,保存的内容还是字符串
        #                       图片来源:外链(通过url链接访问,本站不同存储图片,易引起盗链问题)
        #                               本站存储(提供博文的文本编辑器,提供图片上传到网站存储,生成url,把url嵌入博客正文中,不会有盗链问题,但须解决众多图片存储问题,水印问题,临时图片清理,在线压缩问题等
        #此项目不实现图片功能

#content表 (单独的一张表,把文本类型大字段,一般不和数据频繁查询的字段放在一个表中)
            # 包含字段
            #id
            # content字段



#注: 登陆,注册,退出等功能 user表基本满足(用户方面)
#    用户发文,文章列表,文章详情 post,content表基本满足(博文方面)





#数据库相关配置

USERNAME = 'root'
PASSWD = 'qiangli'
IP = '172.16.101.70'
PORT = 3306
DBNMAME = 'blog'
PARAMS = "charset=utf-8"
URL = 'mysql+pymysql://{}:{}@{}:{}/{}?{}'.format(USERNAME,PASSWD,IP,PORT,DBNMAME,PARAMS )

DATABASE_DEBUG = True
#将配置信息放在配置文件中,如ini,xml,json等文件中


