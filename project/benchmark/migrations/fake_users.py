from django.db import migrations, transaction

def create_fake_users(apps, schema_editor):
    from benchmark.base_data import FakeUsers
    from django.contrib.auth.models import User

    fake_users = FakeUsers().get_content()
    users = [User(**fake_user) for fake_user in fake_users]
    with transaction.atomic():
        User.objects.bulk_create(users)


class Migration(migrations.Migration):
    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length')
    ]

    operations = [
        migrations.RunPython(create_fake_users)
    ]
