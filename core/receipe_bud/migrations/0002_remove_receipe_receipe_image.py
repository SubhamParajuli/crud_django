from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('receipe_bud', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receipe',
            name='receipe_image',
        ),
    ]
