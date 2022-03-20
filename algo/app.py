
from pydantic import BaseModel
from typing import Optional, List
from flask import Flask, request
from pydantic import BaseModel
from flask import request
from flask_pydantic import validate
import json
from algo import Algo

app = Flask("Cleanware")
algo = Algo()


class DataCenter(BaseModel):
    name: str
    tasks: List[int]
    racks: int
    rew_generated: float
    rew_used: float
    energy_overflow: float
    moved_tasks: int


class Status(BaseModel):
    datacenters: List[DataCenter]


class DataCenterRequest(BaseModel):
    datacenter: str
    kw: List[float]
    racks: int


class TaskRequest(BaseModel):
    datacenter: str
    usage: int


@app.route("/dc/task", methods=["PUT", "DELETE"])
@validate()
def create_task(body: TaskRequest):

    if request.method == "DELETE":
        ret = algo.delete_task(body.datacenter, body.usage)
    else:
        ret = algo.add_task(body.datacenter, body.usage)

    return json.dumps({'success': ret}), 200, {'ContentType': 'application/json'}


@app.route("/dc", methods=["POST"])
@validate()
def add_datacenter(body: DataCenterRequest):
    algo.add_datacenter(
        body.datacenter, body.kw, body.racks
    )
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


@app.route("/status", methods=["GET"])
@validate()
def status():
    dcs = algo.status()
    dc_objects = []

    for dc in dcs:
        dc_objects.append(
            dict(
                name=dc["name"],
                tasks=dc["tasks"],
                racks=dc["racks"],
                rew_generated=dc["rewgen"],
                rew_used=dc["rewused"],
                energy_overflow=dc["overflow"],
                moved_tasks=dc["moved"],
            )
        )

    return Status(datacenters=dc_objects)
