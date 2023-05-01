from dagster import Definitions, load_assets_from_modules

from . import assets
from lab1.jobs import hello_world_job

all_assets = load_assets_from_modules([assets])


defs = Definitions(
    assets=all_assets,
    jobs=[hello_world_job]
)
