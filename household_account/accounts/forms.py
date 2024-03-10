from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User # 連携するカスタムユーザーモデル
        fields = ( # フォームで使用するフィールド
            "account_id",
            "email",
            "first_name",
            "last_name",
        )

class LoginForm(AuthenticationForm): # ログインフォームを追加
    class Meta:
        model = User