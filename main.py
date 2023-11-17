from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel


# object_store_italy_S3_01:
#   latitude: 50.0689816
#   longitude: 19.9070188
#   other_stuff_that_we_find_useful: foobar


# destinations:
#   pulsar_italy:
#     runner: general_pulsar_1
#     max_accepted_cores: 8
#     max_accepted_mem: 32
#     scheduling:
#       accept:
#         - general
#       require:
#         - pulsar
#     context:
#       latitude: 50.0689816
#       longitude: 19.9070188


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    return item