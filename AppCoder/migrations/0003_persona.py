# Generated by Django 4.1.2 on 2022-12-16 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("AppCoder", "0002_alter_estudiante_nombre"),
    ]

    operations = [
        migrations.CreateModel(
            name="Persona",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("dni", models.IntegerField()),
                ("nombre", models.CharField(max_length=50)),
                ("apellido", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=254)),
                ("fechaNacimiento", models.DateField()),
                ("tieneObraSocial", models.BooleanField()),
            ],
        ),
    ]
