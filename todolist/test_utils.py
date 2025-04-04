from django.db import connections

def teardown_database():
    try:
        # Clean up any test data here
        MyModel.objects.all().delete()
        if connections['default'].is_usable():
            connections['default'].close()
    except Exception as e:
        print(f"Error tearing down database: {e}")