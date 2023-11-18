from typing import List

from fastapi import FastAPI

from pydantic import BaseModel

from tpv.core.entities import Destination


from closest_location import closest_destination
objectstore_loc_path = "tests/fixtures/object_store_locations.yml"
selected_object_store = "object_store_australia"
# print(type(candidate_destinations))
print(candidate_destinations[0])
# print(candidate_destinations)
final_destinations = closest_destination(candidate_destinations, objectstore_loc_path, selected_object_store)

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


# Pydantic model for request input
class DestinationRequest(BaseModel):
    destinations: List[Destination]


# Pydantic model for response
class ProcessedResult(BaseModel):
    processed_destinations: List[str]


app = FastAPI()

@app.post("/process_destinations", response_model=ProcessedResult)
async def process_destinations(destinations_request: DestinationRequest):
    processed_destinations = []

    for destination in destinations_request.destinations:
        # Example processing: extracting destination name and runner
        processed_info = f"Runner: {destination.runner}, Destination Name: {destination.dest_name}"
        processed_destinations.append(processed_info)

    return {"processed_destinations": processed_destinations}