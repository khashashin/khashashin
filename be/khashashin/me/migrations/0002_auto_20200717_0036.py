# Generated by Django 3.0.8 on 2020-07-16 22:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('me', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmessages',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='education',
            name='doc1',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='education',
            name='doc2',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='education',
            name='doc3',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='education',
            name='end_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='is_current',
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='start_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='education', to='me.Me'),
        ),
        migrations.AlterField(
            model_name='me',
            name='phone_number',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='projects',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='me.Me'),
        ),
        migrations.AlterField(
            model_name='skills',
            name='doc1',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='skills',
            name='doc2',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='skills',
            name='doc3',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='skills',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='skills', to='me.Me'),
        ),
        migrations.AlterField(
            model_name='socialaccounts',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='social_accounts', to='me.Me'),
        ),
        migrations.AlterField(
            model_name='work',
            name='doc1',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='work',
            name='doc2',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='work',
            name='doc3',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='work',
            name='end_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='work',
            name='is_current',
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name='work',
            name='start_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='work',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='work', to='me.Me'),
        ),
    ]
