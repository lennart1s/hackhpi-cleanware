import string
from typing import Optional, List
from flask import Flask, request
from pydantic import BaseModel

from flask_pydantic import validate

app = Flask("Cleanware")


datacenters = dict()


class Task(BaseModel):
    cpu_usage: int


class DataCenter(BaseModel):
    ident: string
    lang: float
    lon: float
    tasks: List[Task]

    racks: int


@app.route("/<datacenter>/task/<usage>", methods=["PUT"])
@validate()
def create_task(datacenter: str, usage: int):
    pass


@app.route("/<datacenter>/task/<usage>", methods=["PUT"])
@validate()
def delte_task(datacenter: str, usage: int):
    pass


@app.route("/<datacenter>/task", methods=["DELETE"])
@validate()
def create_task(datacenter: str):
    pass


@app.route("/<datacenter>/task", methods=["DELETE"])
@validate()
def create_task(datacenter: str):
    pass


@app.route("/<datacenter>", methods=["PUT"])
@validate()
def create_task(datacenter: str):
    pass


@app.route("/users/<datacenter>", methods=["DELETE"])
@validate()
def create_task(datacenter: str):
    pass


@app.route("/status", methods=["GET"])
@validate()
def get(query: QueryModel):
    age = query.age
    return ResponseModel(
        age=age,
        id=0, name="abc", nickname="123"
    )
