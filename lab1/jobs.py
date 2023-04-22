from dagster import define_asset_job

from lab1.assets import hello_world, complex_asset

hello_world_job = define_asset_job(name="hello_world_job", selection="hello_world")

complex_job = define_asset_job(name='complex_hello_world_job', selection="complex_asset")

