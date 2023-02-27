# Generated by Django 4.1.6 on 2023-02-22 02:15
import pandas as pd
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_customer_store_custo_firstna_18af8c_idx'),
    ]

    # Sample about how we can insert raw sql to migration
    # Also, when we revert migration by running command "python3 manage.py migration store 0004",
    # it will run the 2nd sql command and delete the inserted record.

    # operations = [
    #     migrations.RunSQL("""
    #             INSERT INTO store_category (title) VALUES ('cat1')
    #         """, """
    #             DELETE FROM store_category WHERE title='cat1'
    #         """)
    # ]

    # Simple example of bulk insert to db

    # CUSTOMER_DATA = """
    #     ('firstname1','lastname1','email1@gmail.com','1234567890','2023-01-01','B'),
    #     ('firstname2','lastname2','email2@gmail.com','1234567890','2023-01-01','B'),
    #     ('firstname3','lastname3','email3@gmail.com','1234567890','2023-01-01','B'),
    #     ('firstname4','lastname4','email4@gmail.com','1234567890','2023-01-01','B'),
    #     ('firstname5','lastname5','email5@gmail.com','1234567890','2023-01-01','B')
    #     """

    # operations = [
    #             migrations.RunSQL(f"""
    #                     INSERT INTO store_customer ('firstname','lastname','email','phone','birth_date','membership')
    #                     VALUES {CUSTOMER_DATA} ON CONFLICT DO NOTHING;
    #                 """)
    #         ]

    # Insert data to database by import CSV

    # define header
    header_list = {'firstname', 'lastname', 'email', 'phone', 'birth_date', 'membership'}

    # read file
    path = 'sample_data/MOCK_DATA_CUSTOMER.csv'
    df = pd.read_csv(filepath_or_buffer=path)

    # check if header matched
    df_list = set(df.columns)
    check_matched_header = list(header_list - set(df.columns))
    if check_matched_header:
        # throw error
        print(f'There are some column that does not match: {check_matched_header}')
    else:
        # handle data
        customer_data = ''
        for i, values in enumerate(df.values):
            # join from array to string
            customer_data += "('" + "','".join(str(x) for x in values) + "')"
            # check if this is the last row
            if i != len(df) - 1:
                customer_data += ',\n'
        customer_data = f"""{customer_data}"""

        # insert to db
        # please note that when we run this migration,
        # we need to make sure that it's not counted in table django_migrations yet
        # if it's already exists, please remove it manually in table django_migrations and try again
        operations = [
            migrations.RunSQL(f"""
                    INSERT INTO store_customer ('firstname','lastname','email','phone','birth_date','membership')
                    VALUES {customer_data} ON CONFLICT DO NOTHING;
                """, """
                    DELETE FROM store_customer
                """)
        ]

