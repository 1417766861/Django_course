from django.db import models

# Create your models here.



class Category(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    class Meta:
        db_table = 'category'

def default_category():
    return Category.objects.get(pk=4) #默认分类

class Article(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    category = models.ForeignKey("Category",on_delete=models.SET_NULL,null=True)
    # category = models.ForeignKey("Category",on_delete=models.SET_DEFAULT,default=Category.objects.get(pk=4))
    # category = models.ForeignKey("Category",on_delete=models.SET(Category.objects.get(pk=4)),null=True)
    # category = models.ForeignKey("Category",on_delete=models.SET(default_category),null=True) #传递一个函数
    #删除了 指向分类===> 默认分类
    """
    CASCADE 级联删除，删除category，输出关联的article
    PROTECT:"Cannot delete some instances of model 'Category' because they are referenced through a protected foreign key
    SETNLL: 设置为空  catetory,此项可以为空 ：null=True
    SET_DEFAULT:设置默认值。如果外键的那条数据被删除了，那么本条数据上就将这个字段设置为默认值。如果设置这个选项，前提是要指定这个字段一个默认值。
    DO_NOTHING：不采取任何行为。一切全看数据库级别的约束。
    
    SET()：如果外键的那条数据被删除了。那么将会获取SET函数中的值来作为这个外键的值。
    SET函数可以接收一个可以调用的对象（比如函数或者方法），如果是可以调用的对象，
    那么会将这个对象调用后的结果作为值返回回去。
    """
    author = models.ForeignKey("front.FrontUser",on_delete=models.CASCADE)
    class Meta:
        db_table = 'article'


class Comment(models.Model):
    id = models.BigAutoField(primary_key=True)
    content = models.TextField()

    article = models.ForeignKey("Article",on_delete=models.CASCADE)
    origin_comment = models.ForeignKey("self",on_delete=models.CASCADE)
    author = models.ForeignKey("front.FrontUser", on_delete=models.CASCADE,null=True)


