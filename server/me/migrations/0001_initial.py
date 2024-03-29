# Generated by Django 3.0.8 on 2020-07-16 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=500)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField(blank=True, default='')),
            ],
        ),
        migrations.CreateModel(
            name='Me',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, default='', max_length=500)),
                ('last_name', models.CharField(blank=True, default='', max_length=500)),
                ('img_width', models.SmallIntegerField(blank=True, default=250)),
                ('img_height', models.SmallIntegerField(blank=True, default=250)),
                ('tmb_width', models.SmallIntegerField(blank=True, default=250)),
                ('tmb_height', models.SmallIntegerField(blank=True, default=250)),
                ('image', models.ImageField(blank=True, height_field=models.SmallIntegerField(blank=True, default=250), upload_to='', width_field=models.SmallIntegerField(blank=True, default=250))),
                ('tmb_image', models.ImageField(blank=True, height_field=models.SmallIntegerField(blank=True, default=250), upload_to='', width_field=models.SmallIntegerField(blank=True, default=250))),
                ('slogan', models.CharField(blank=True, default='', max_length=500)),
                ('title', models.CharField(blank=True, default='', max_length=500)),
                ('about', models.TextField(blank=True, default='')),
                ('phone_number', models.TextField(blank=True, default='')),
                ('email', models.EmailField(blank=True, default='', max_length=254)),
                ('website', models.CharField(blank=True, default='', max_length=500)),
                ('street', models.CharField(blank=True, default='', max_length=500)),
                ('street_number', models.SmallIntegerField(blank=True, default=0)),
                ('state', models.CharField(blank=True, default='', max_length=500)),
                ('land', models.CharField(blank=True, default='', max_length=500)),
                ('zip', models.SmallIntegerField(blank=True, default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=500)),
                ('company', models.CharField(blank=True, default='', max_length=500)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('is_current', models.BooleanField()),
                ('conclusion', models.TextField(blank=True, default='')),
                ('doc1', models.FileField(upload_to='')),
                ('doc2', models.FileField(upload_to='')),
                ('doc3', models.FileField(upload_to='')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='me.Me')),
            ],
        ),
        migrations.CreateModel(
            name='SocialAccounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(blank=True, default='', max_length=500)),
                ('url', models.CharField(blank=True, default='', max_length=500)),
                ('icon', models.ImageField(blank=True, upload_to='')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='me.Me')),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scope', models.CharField(blank=True, default='', max_length=500)),
                ('percentage', models.SmallIntegerField(blank=True, default=100)),
                ('doc1', models.FileField(upload_to='')),
                ('doc2', models.FileField(upload_to='')),
                ('doc3', models.FileField(upload_to='')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='me.Me')),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=500)),
                ('subtitle', models.CharField(blank=True, default='', max_length=500)),
                ('img_width', models.SmallIntegerField(blank=True, default=250)),
                ('img_height', models.SmallIntegerField(blank=True, default=250)),
                ('tmb_width', models.SmallIntegerField(blank=True, default=250)),
                ('tmb_height', models.SmallIntegerField(blank=True, default=250)),
                ('image', models.ImageField(blank=True, height_field=models.SmallIntegerField(blank=True, default=250), upload_to='', width_field=models.SmallIntegerField(blank=True, default=250))),
                ('tmb_image', models.ImageField(blank=True, height_field=models.SmallIntegerField(blank=True, default=250), upload_to='', width_field=models.SmallIntegerField(blank=True, default=250))),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='me.Me')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=500)),
                ('university', models.CharField(blank=True, default='', max_length=500)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('is_current', models.BooleanField()),
                ('conclusion', models.TextField(blank=True, default='')),
                ('doc1', models.FileField(upload_to='')),
                ('doc2', models.FileField(upload_to='')),
                ('doc3', models.FileField(upload_to='')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='me.Me')),
            ],
        ),
    ]
