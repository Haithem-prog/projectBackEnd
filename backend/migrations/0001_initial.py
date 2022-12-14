# Generated by Django 4.1.1 on 2022-09-16 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('AuthorImageUrl', models.URLField(blank=True, default='https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/Blank_button.svg/1200px-Blank_button.svg.png', null=True)),
                ('is_active', models.BooleanField(verbose_name='is active')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('bookImageUrl', models.URLField(blank=True, default='https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/Blank_button.svg/1200px-Blank_button.svg.png', null=True)),
                ('published', models.DateField(verbose_name='Published Data')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='price')),
                ('rate', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True, verbose_name='rate')),
                ('pages', models.IntegerField(verbose_name='pages')),
                ('total_sales', models.IntegerField()),
                ('language', models.CharField(choices=[('Arabic', 'Arabic'), ('English', 'English')], max_length=10, verbose_name='Language')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('GenreImageUrl', models.URLField(blank=True, default='https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/Blank_button.svg/1200px-Blank_button.svg.png', null=True)),
                ('is_active', models.BooleanField(verbose_name='is active')),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField(default=1)),
                ('inCart', models.BooleanField(default=False)),
                ('isBought', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Saved_Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saved', models.BooleanField(verbose_name='isSaved')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='here', to='backend.book', verbose_name='saved_Books')),
            ],
        ),
    ]
