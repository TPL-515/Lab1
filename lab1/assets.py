from dagster import asset

@asset
def hello_world():
    return 'hello world'

@asset
def complex_asset():
    message = hello_world()
    print(message)
    print('woo')
