# Generated by Django 2.2.4 on 2020-01-23 03:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('oily', models.SmallIntegerField()),
                ('dry', models.SmallIntegerField()),
                ('sensitive', models.SmallIntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='item',
            name='quantity',
        ),
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.CharField(db_index=True, default='etc', max_length=256),
        ),
        migrations.AddField(
            model_name='item',
            name='dryScore',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='item',
            name='gender',
            field=models.CharField(db_index=True, default='all', max_length=6),
        ),
        migrations.AddField(
            model_name='item',
            name='imageId',
            field=models.CharField(max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='ingredients',
            field=models.TextField(default='', max_length=512),
        ),
        migrations.AddField(
            model_name='item',
            name='monthlySales',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='item',
            name='oilyScore',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='item',
            name='price',
            field=models.PositiveIntegerField(db_index=True, default=9999999),
        ),
        migrations.AddField(
            model_name='item',
            name='sensitiveScore',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='item',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(db_index=True, max_length=100),
        ),
        migrations.CreateModel(
            name='ItemToIngredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient', models.CharField(db_index=True, default='', max_length=100)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='item.Item', verbose_name='itemID')),
            ],
        ),
    ]