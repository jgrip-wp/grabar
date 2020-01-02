from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin


DEPARTMENT_CHOICES = (
    ('管理部', '管理部'),
    ('Webリレーション部', 'Webリレーション部'),
    ('事業推進室', '事業推進室'),
    ('クリエイティブ部', 'クリエイティブ部'),
    ('コンサルティング部', 'コンサルティング部'),
    ('PR部', 'PR部'),
)


class SystemUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('the given email must be set.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        return user

    def create_user(self, email, password=None, **extra_fields):
        # generate if password doesn't given
        if not password:
            password = self.make_random_password()

        # the user's default status is "active"
        extra_fields.setdefault('is_active', True)

        # the user must not be superuser
        user = self._create_user(email, password, **extra_fields)
        user.is_staff = False
        user.is_superuser = False
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        # the user's default status is "active"
        extra_fields.setdefault('is_active', True)

        # the user must not be superuser
        user = self._create_user(email, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save()


class SystemUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = SystemUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)


class Employee(SystemUser):
    number = models.CharField(max_length=3)
    name = models.CharField(max_length=256)
    name_kana = models.CharField(max_length=256)
    department = models.CharField(max_length=128, choices=DEPARTMENT_CHOICES)
    thumbnail = models.ImageField(upload_to='thumbnail/', blank=True, null=True)

    REQUIRED_FIELD = ['name', 'number']
