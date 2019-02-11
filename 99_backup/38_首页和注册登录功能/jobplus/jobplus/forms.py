from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, SubmitField, BooleanField,
    ValidationError, IntegerField, TextAreaField)
from wtforms.validators import Length, Email, EqualTo, Required
from .models import db, User, CompanyDetail, Resume, Job

class RegisterForm(FlaskForm):
    name = StringField('用户名', validators=[Required(), Length(3, 32)])
    email = StringField('邮箱', validators=[Required(), Email()])
    password = PasswordField('密码', validators=[Required(), Length(6, 24)])
    repeat_password = PasswordField('重复密码', 
        validators=[Required(), EqualTo('password')])
    submit = SubmitField('提交')

    def validate_name(self, f):
        if User.query.filter_by(name=f.data).first():
            raise ValidationError('用户名已经存在')

    def validate_email(self, f):
        if User.query.filter_by(email=f.data).first():
            raise ValidationError('邮箱已经被注册')

    def create_user(self):
        user = User()
        self.populate_obj(user)
        db.session.add(user)
        db.session.commit()
        return user


class LoginForm(FlaskForm):
    name = StringField('用户名/邮箱', validators=[Required()])
    password = PasswordField('密码', validators=[Required(), Length(6, 24)])
    remember_me = BooleanField('记住我')
    submit = SubmitField('提交')

    def validate_name(self, f):
        u1 = User.query.filter_by(name=f.data).first()
        u2 = User.query.filter_by(email=f.data).first()
        if not u1 and not u2:
            raise ValidationError('用户名或邮箱不存在')

    def validate_password(self, f):
        user = User.query.filter_by(name=self.name.data).first()
        if user and not user.check_password(f.data):
            raise ValidationError('密码错误')
        user = User.query.filter_by(email=self.name.data).first()
        if user and not user.check_password(f.data):
            raise ValidationError('密码错误')
        
