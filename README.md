# Basic Mission

![image](https://user-images.githubusercontent.com/72116811/163842639-1efe8ae4-22d9-41f1-9e28-88c6b83e17cc.png)
![image](https://user-images.githubusercontent.com/72116811/163842767-ee2d1fc1-cd1e-44fd-96cc-d412db3849a4.png)

## models.py

```python
class Faq(models.Model):
    CHOICES =(
        (0,'일반'),
        (1,'계정'),
        (2,'기타'),
        )
    category = models.CharField(max_length=2,choices=CHOICES,default=0)
    question = models.TextField(verbose_name='질문')
    writer = models.ForeignKey(to=User,on_delete=models.CASCADE,null=True,blank=True)
    answer = models.TextField(verbose_name='답변')
    modifier = models.CharField(max_length=20,unique=True)
    created_at = models.DateTimeField(verbose_name='작성일', auto_now_add =True)
    modified_date = models.DateTimeField(auto_now=True)
    ```
    
    ## admin.py
    
    ```python
    @admin.register(Faq)
class FqaModelAdmin(admin.ModelAdmin):
    list_display = (
'writer',
'created_at',
'modifier',
'modified_date',
    )
    search_fields = ('category','writer','modifier')
    search_help_text = '카테고리, 작성자, 수정자 검색'
    readonly_fields = ('created_at','modified_date',)
    ```
    
