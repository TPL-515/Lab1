from dagster import asset

@asset(description="The purpose of this asset is to show off the basic capability of the definiton. This asset simply prints the hello world string.", metadata={"Demo": "Capability", "Add stuff": "here", "num_strings": 1})
def hello_world():
    print('hello world')

