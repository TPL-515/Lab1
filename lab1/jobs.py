from dagster import define_asset_job

from lab1.assets import hello_world

hello_world_job = define_asset_job(name="hello_world_job", selection="hello_world")


