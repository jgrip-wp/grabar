import os


environment_name = os.getenv('ENVIRONMENT_NAME')
if environment_name == 'development':
  print('開発環境として設定を読み込みます。')
  from .development import *
elif environment_name == 'production':
  from .production import *
else:
  print('環境変数ENVIRONMENT_NAMEが定義されていません。開発環境として設定を読み込みます。')
  from .development import *
