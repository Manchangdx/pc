from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Length, Email, EqualTo, Required
from simpledu.models import db, User
from wtforms import ValidationError

class RegisterForm(FlaskForm):
    username = StringField('用户名', validators=[Required(), Length(3, 24)])
    email = StringField('邮箱', validators=[Required(), Email()])
    password = PasswordField('密码', validators=[Required(), Length(6, 24)])
    repeat_password = PasswordField('确认密码', 
        validators=[Required(), EqualTo('password')])
    submit = SubmitField('提交')

    def validate_username(self, field):
        if not field.data.isalnum():
            raise ValidationError('用户名只能由数字和字母组成')
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('用户已经存在')
    def create_user(self):
        user = User()
        self.populate_obj(user)
        '''
        user.username = self.username.data
        user.email = self.email.data
        user.password = self.password.data
        '''
        db.session.add(user)
        db.session.commit()
        return user


class LoginForm(FlaskForm):
    username = StringField('用户名', validators=[Required(), Length(3, 24)])
    password = PasswordField('密码', validators=[Required(), Length(6, 24)])
    remember_me = BooleanField('记住我')
    submit = SubmitField('提交')
    def validate_username(self, field):
        if not User.query.filter_by(username=field.data).first():
            raise ValidationError('用户名未注册')

    def validate_password(self, field):
        user = User.query.filter_by(username=self.username.data).first()
        if user and not user.check_password(field.data):
            raise ValidationError('密码错误')
