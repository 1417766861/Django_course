#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/5/22 20:15
from .models import UserModel
from django import forms


class UserForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = "__all__"
        error_messages = {
            'username':{
                'required':"请输入用户名"
            },
            'password':{
                'required':"请输入密码"
            }
        }

    def get_error(self):
        news_errors = []
        errors = self.errors.get_json_data()
        for messages in errors.values():
            for message_dict in messages:
                for key,message in message_dict.items():
                    if key == 'message':
                        news_errors.append(message)
        return news_errors
