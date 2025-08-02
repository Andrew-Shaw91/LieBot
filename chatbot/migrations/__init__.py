from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
          
            name = 'Chat',
            fields = [
                ('ChatID', models.AutoField(auto_created = True, primary_key = True)),
                ('prompt', models.CharField(max_length = 255)),
                ('answer', models.CharField(max_length = 255))
            ],

           name = 'Account',
            fields = [
                ('username', models.CharField(max_length = 30, primary_key = True)),
                ('password', models.CharField(max_length = 30)),
                ('savedChats', models.ForeignKey(Chat, on_delete = models.CASCADE))
            ],
          
        ),
    ]
