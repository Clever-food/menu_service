import peewee

from src.models.db_connection import db

class MenuModel(peewee.Model):
    menu_id = peewee.PrimaryKeyField(
        db_column="menu_id",
    )
    name = peewee.CharField(
        max_length=1000,
        null=False,
    )
    price = peewee.IntegerField(
        null=False,
    )
    volume = peewee.IntegerField(
        null=False,
    )
    class Meta:
        database = db
        db_table = "menu"


MenuModel.create_table()