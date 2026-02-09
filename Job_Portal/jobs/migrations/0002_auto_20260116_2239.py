from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),  # your last migration
    ]

    operations = [
        migrations.AddField(
            model_name='jobapplication',
            name='resume',
            field=models.FileField(default='', upload_to='resumes/'),
            preserve_default=False,
        ),
    ]
