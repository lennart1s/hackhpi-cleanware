import string
from typing import Optional, List
from flask import Flask, request
from pydantic import BaseModel
from flask import request
from flask_pydantic import validate
import json
from algo.algo import Algo

app = Flask("Cleanware")
algo = Algo()


class DataCenter(BaseModel):
    name: str
    tasks: List[int]
    racks: int
    rew_generated: float
    rew_used: float
    energy_overflow: float
    moved_tasks: float


class Status(BaseModel):
    datacenters: List[DataCenter]


class DataCenterRequest(BaseModel):
    kw: List[float]
    racks: int


@app.route("/<datacenter>/task/<int:usage>", methods=["PUT", "DELETE"])
@validate()
def create_task(datacenter: str, usage: int):

    if request.method == "DELETE":
        ret = algo.delete_task(datacenter, usage)
    else:
        ret = algo.add_task(datacenter, usage)

    return json.dumps({'success': ret}), 200, {'ContentType': 'application/json'}


@app.route("/<datacenter>", methods=["GET"])
@validate()
def add_datacenter(datacenter: str, req: DataCenterRequest):
    algo.add_datacenter(
        datacenter, req.kw, req.racks
    )


@app.route("/status", methods=["GET"])
@validate()
def status():
    dcs = algo.status()
    dc_objects = []

    for dc in dcs:
        dc_objects.append(
            DataCenter(
                name=dc["name"],
                tasks=dc["tasks"],
                racks=dc["racks"],
                rew_generated=dc["rewgen"],
                rew_used=dc["rewused"],
                energy_overflow=dc["overflow"],
                moved_tasks=dc["moved"],
            )
        )

    return Status(dc_objects)
