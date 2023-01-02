from .models import Category, Post
from faker import Faker
from datetime import datetime

def run():
    fake = Faker(['en-US'])
    categories = (
        "Politics",
        "Sports",
        "Millitary",
        "Travel",
        "Showbiz"
    )

    for category_id in categories:
        new_category = Category.objects.create(category_name = category_id)
        for _ in range(30):
            Post.objects.create(category_id = new_category, title = fake.company(), content = fake.text(), status = fake.pybool(), created_date = fake.date_time_this_year(), updated_date = fake.date_time_this_year() )
    
    print('Finished')