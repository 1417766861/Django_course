from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()

    price = models.FloatField(verbose_name='价格')
    author = models.CharField(max_length=100)
"""
makemigrations：将模型生成迁移脚本。模型所在的app，必须放在settings.py中的INSTALLED_APPS中。这个命令有以下几个常用选项：

app_label：后面可以跟一个或者多个app，那么就只会针对这几个app生成迁移脚本。如果没有任何的app_label，那么会检查INSTALLED_APPS中所有的app下的模型，针对每一个app都生成响应的迁移脚本。
--name：给这个迁移脚本指定一个名字。
--empty：生成一个空的迁移脚本。如果你想写自己的迁移脚本，可以使用这个命令来实现一个空的文件，然后自己再在文件中写迁移脚本。
migrate：将新生成的迁移脚本。映射到数据库中。创建新的表或者修改表的结构。以下一些常用的选项：

app_label：将某个app下的迁移脚本映射到数据库中。如果没有指定，那么会将所有在INSTALLED_APPS中的app下的模型都映射到数据库中。
app_label migrationname：将某个app下指定名字的migration文件映射到数据库中。
--fake：可以将指定的迁移脚本名字添加到数据库中。但是并不会把迁移脚本转换为SQL语句，修改数据库中的表。
--fake-initial：将第一次生成的迁移文件版本号记录在数据库中。但并不会真正的执行迁移脚本。
showmigrations：查看某个app下的迁移文件。如果后面没有app，那么将查看INSTALLED_APPS中所有的迁移文件。

sqlmigrate：查看某个迁移文件在映射到数据库中的时候，转换的SQL语句。

--fake：可以将指定的迁移脚本名字添加到数据库中。但是并不会把迁移脚本转换为SQL语句，修改数据库中的表。

--fake-initial：将第一次生成的迁移文件版本号记录在数据库中。但并不会真正的执行迁移脚本。
"""

"""
migrations中的迁移版本和数据库中的迁移版本对不上怎么办？
找到哪里不一致，然后使用python manage.py --fake [版本名字]，将这个版本标记为已经映射。

删除指定app下migrations和数据库表django_migrations中和这个app相关的版本号，然后将模型中的字段和数据库中的字段保持一致，
再使用命令python manage.py makemigrations重新生成一个初始化的迁移脚本，
之后再使用命令python manage.py makemigrations --fake-initial来将这个初始化的迁移脚本标记为已经映射。
以后再修改就没有问题了。"""