# Generated by Django 4.1.7 on 2023-02-23 02:44
from datetime import datetime

from django.db import migrations
from faker import Faker
from store.models import Category

fake = Faker()


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20230222_1706'),
    ]

    # Create migration data for table store_product
    length = 100
    product_range = range(length)
    product_data = ""
    for i in product_range:
        title = fake.name()
        description = fake.sentence()
        slug = 'product'
        unit_price = fake.pyfloat(positive=True, right_digits=2, left_digits=2)
        inventory = 100
        created_date = datetime.now()
        updated_date = datetime.now()
        # get random category id
        category_id = Category.objects.order_by('?').values_list('id', flat=True)[0]

        product_data += "('" \
                        + title + "','" \
                        + description + "','" \
                        + slug + "','" \
                        + str(unit_price) + "','" \
                        + str(inventory) + "','" \
                        + str(created_date) + "','" \
                        + str(updated_date) + "','" \
                        + str(category_id) \
                        + "')"
        if i != length - 1:
            product_data += ',\n'
    product_data = f"""{product_data}"""

    operations = [
        migrations.RunSQL(f"""
                                    INSERT INTO store_product (
                                        'title', 
                                        'description', 
                                        'slug', 
                                        'unit_price', 
                                        'inventory', 
                                        'created_date', 
                                        'updated_date', 
                                        'category_id'
                                    )
                                    VALUES {product_data} ON CONFLICT DO NOTHING;
                                """, """
                                    DELETE FROM store_product
                                """)
    ]

