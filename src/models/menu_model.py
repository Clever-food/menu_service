import peewee

from src.models.db_connection import db

class MenuModel(peewee.Model):
    id = peewee.AutoField()

    dish_class = peewee.IntegerField(
        null=False,
    )

    dish_name = peewee.CharField(
        unique=True,
        null=False,
        max_length=50,
    )

    is_portionable = peewee.BooleanField(
        null=True
    )

    weight_volume = peewee.IntegerField(
        null=True,
    )

    price = peewee.IntegerField(
        null=True,
    )

    class Meta:
        database = db
        db_table = "dish"

MenuModel.create_table()
