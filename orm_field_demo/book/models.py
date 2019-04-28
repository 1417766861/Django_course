from django.db import models
from django.utils.timezone import now
# Create your models here.

class ArticleModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    #默认是不为空 null = False
    #is_remove = models.BooleanField()
                    # models.BooleanField(null=True) BooleanField为空代替
    name = models.CharField(max_length=100)
    create_time = models.DateTimeField(auto_now_add=True)
    # auto_now_add: 第一次更新
    # auto_now:每次save时候都会更新

    class Meta:
        db_table = 'book' #定义表的名
        ordering = ['-create_time'] #做排序

    def __str__(self):
        return '<Article %s> name %s'%(self.id,self.name)


class Person(models.Model):
    #在表单验证时，会起作用
    email = models.EmailField() #不会验证数据

    signature = models.TextField() #longtext


class Author(models.Model):
    username = models.CharField(max_length=100)
    age = models.IntegerField(null=True)

    #blank 类似null，但针对数据库层面，表单验证这一层起作用

    #db_column 映射到数据库中的名字
    place = models.CharField(max_length=1,db_column="address")

    #defalut 默认值

    create_time = models.DateTimeField(default=now) #aware time

    #unuque 唯一
    phone = models.CharField(max_length=11,unique=True,null=True) #null=True，防止之前数据唯一报错

"""
常用字段：
在Django中，定义了一些Field来与数据库表中的字段类型来进行映射。以下将介绍那些常用的字段类型。

AutoField：
映射到数据库中是int类型，可以有自动增长的特性。一般不需要使用这个类型，如果不指定主键，那么模型会自动的生成一个叫做id的自动增长的主键。如果你想指定一个其他名字的并且具有自动增长的主键，使用AutoField也是可以的。

BigAutoField：
64位的整形，类似于AutoField，只不过是产生的数据的范围是从1-9223372036854775807。

BooleanField：
在模型层面接收的是True/False。在数据库层面是tinyint类型。如果没有指定默认值，默认值是None。

CharField：
在数据库层面是varchar类型。在Python层面就是普通的字符串。这个类型在使用的时候必须要指定最大的长度，也即必须要传递max_length这个关键字参数进去。

DateField：
日期类型。在Python中是datetime.date类型，可以记录年月日。在映射到数据库中也是date类型。使用这个Field可以传递以下几个参数：

auto_now：在每次这个数据保存的时候，都使用当前的时间。比如作为一个记录修改日期的字段，可以将这个属性设置为True。
auto_now_add：在每次数据第一次被添加进去的时候，都使用当前的时间。比如作为一个记录第一次入库的字段，可以将这个属性设置为True。
DateTimeField：
日期时间类型，类似于DateField。不仅仅可以存储日期，还可以存储时间。映射到数据库中是datetime类型。这个Field也可以使用auto_now和auto_now_add两个属性。

TimeField：
时间类型。在数据库中是time类型。在Python中是datetime.time类型。

EmailField：
类似于CharField。在数据库底层也是一个varchar类型。最大长度是254个字符。

FileField：
用来存储文件的。这个请参考后面的文件上传章节部分。

ImageField：
用来存储图片文件的。这个请参考后面的图片上传章节部分。

FloatField：
浮点类型。映射到数据库中是float类型。

IntegerField：
整形。值的区间是-2147483648——2147483647。

BigIntegerField：
大整形。值的区间是-9223372036854775808——9223372036854775807。

PositiveIntegerField：
正整形。值的区间是0——2147483647。

SmallIntegerField：
小整形。值的区间是-32768——32767。

PositiveSmallIntegerField：
正小整形。值的区间是0——32767。

TextField：
大量的文本类型。映射到数据库中是longtext类型。

UUIDField：
只能存储uuid格式的字符串。uuid是一个32位的全球唯一的字符串，一般用来作为主键。

URLField：
类似于CharField，只不过只能用来存储url格式的字符串。并且默认的max_length是200。

Field的常用参数：
null：
如果设置为True，Django将会在映射表的时候指定是否为空。默认是为False。在使用字符串相关的Field（CharField/TextField）的时候，官方推荐尽量不要使用这个参数，也就是保持默认值False。因为Django在处理字符串相关的Field的时候，即使这个Field的null=False，如果你没有给这个Field传递任何值，那么Django也会使用一个空的字符串""来作为默认值存储进去。因此如果再使用null=True，Django会产生两种空值的情形（NULL或者空字符串）。如果想要在表单验证的时候允许这个字符串为空，那么建议使用blank=True。如果你的Field是BooleanField，那么对应的可空的字段则为NullBooleanField。

blank：
标识这个字段在表单验证的时候是否可以为空。默认是False。
这个和null是有区别的，null是一个纯数据库级别的。而blank是表单验证级别的。

db_column：
这个字段在数据库中的名字。如果没有设置这个参数，那么将会使用模型中属性的名字。

default：
默认值。可以为一个值，或者是一个函数，但是不支持lambda表达式。并且不支持列表/字典/集合等可变的数据结构。

primary_key：
是否为主键。默认是False。

unique：
在表中这个字段的值是否唯一。一般是设置手机号码/邮箱等。

更多Field参数请参考官方文档：https://docs.djangoproject.com/zh-hans/2.0/ref/models/fields/

模型中Meta配置：
对于一些模型级别的配置。我们可以在模型中定义一个类，叫做Meta。然后在这个类中添加一些类属性来控制模型的作用。比如我们想要在数据库映射的时候使用自己指定的表名，而不是使用模型的名称。那么我们可以在Meta类中添加一个db_table的属性。示例代码如下：

class Book(models.Model):
    name = models.CharField(max_length=20,null=False)
    desc = models.CharField(max_length=100,name='description',db_column="description1")

    class Meta:
        db_table = 'book_model'
以下将对Meta类中的一些常用配置进行解释。

db_table：
这个模型映射到数据库中的表名。如果没有指定这个参数，那么在映射的时候将会使用模型名来作为默认的表名。

ordering：
设置在提取数据的排序方式。后面章节会讲到如何查找数据。比如我想在查找数据的时候根据添加的时间排序，那么示例代码如下：

class Book(models.Model):
    name = models.CharField(max_length=20,null=False)
    desc = models.CharField(max_length=100,name='description',db_column="description1")
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'book_model'
        ordering = ['pub_date']
"""