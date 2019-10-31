'''
编程日志
2019。09。19
    1、搭建开发环境
        source env/bin/activate # 开始使用虚拟环境前先激活：
        deactivate # 停用虚拟环境：
    2、创建APP，以及相关的配置
    3、编写Model层；数据迁移（* 注意，每当对数据库进行了更改（添加、修改、删除等）操作，都需要进行数据迁移
            *python manage.py makemigrations
            *python manage.py migrate
        再重复一次：每当你修改了models.py文件，都需要用makemigrations和migrate这两条指令迁移数据。
        在迁移之后，Model的编写就算完成了。
        )
    4、创建管理员账号
    5、将ArticlePost注册到后台中(* 这里因为版本原因报错OperationalError: no such table: main.auth_user__old
        解决办法：
            1、降级Django到pip install Django==2.1.5
            2、重新迁移数据
            3、重新创建超级管理员
            )
    6、改写视图函数
    7、使用Form表单类发表新文章; 优化写文章入口           知识点：提交表单
    8、编写删除文章功能（* 此处遇到一个bug：今天解决问题，是因为我在创建jquery和layer的js文件时，命名错误导致）
        反向解析 url 实现的跳转：Reverse for 'article_delete' not found. 'article_delete' is not a valid view function or pattern name.
        还是url指向名称的问题
2019。10。8
    1、完成修改文章功能
    2、用户的登录和登出
    3、重置用户密码
    4、扩展用户信息
    5、上传头像图片
    6、文章分页
    7、统计文章浏览量
    8、根据浏览量对最热文章排序
2019.10.9
    1、根据浏览量对最热文章排序
    2、简单搜索博客文章
    3、渲染Markdown文章目录
    4、在博文中发表评论
    5、设置文章的栏目

2019.10.10
    1、文章标签功能
    2、给文章加个漂亮的标题图 & 将标题图和标签功能添加到编辑文章
    3、使用django-ckeditor富文本编辑器 & 在前台使用Ckeditor
2019。10。11
    1、回到顶部浮动按钮 & 矢量图标 & 页脚沉底 & 粘性侧边栏
2019。10。11
    1、用django-mptt实现多级评论功能
        1、首先安装django-mptt
        2、安装成功后，在配置中注册
        3、「轻车熟路」修改评论模型
2019。10。22
        4、Ajax提交表单（这里碰见一个错误，最后是因为迁移数据库的原因，再次记录一下）
2019。10。23
    1、新功能：消息通知，以django-notifications为基础
    2、后端逻辑
    3、小红点：前端现实消息通知
    4、未读与已读：通知是一个独立的功能
2019。10。24
    1、锚点定位：三种实现
        1、html拼接
        2、视图拼接
        3、流动的数据
2019。10。28
    今天做项目总结：
    功能点：
    文章系统：增删改查，文章详情，列表，文章浏览量
    用户系统：登陆，注册，删除，个人信息，退出
    评论系统：一级评论，二级评论
    通知系统：已读，未读，通知
2019。10。29
    服务器部署：
    1、配置服务器
    2、正式部署
    3、远程连接
    4、代码部署
        1、安装 nginx、python3、pip、git、virtualenv
        2、改一下 Django 的配置文件 settings.py
    5、Gunicorn及测试
'''