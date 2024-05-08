import os
from fastapi import APIRouter, File, UploadFile, HTTPException

from influxdb_client import InfluxDBClient

from collections import defaultdict
from typing import List
from config import settings
from starlette.responses import JSONResponse

from app.domain.facility.service.facility_function import get_facilities_info

url = settings.influx_url
token = settings.influx_token
organization = settings.influx_org
bucket = settings.influx_bucket

facility_router = APIRouter(prefix="/facility", tags=['request'])


@facility_router.post("/write")
async def write_influxdb(files: List[UploadFile] = File(...)):
    client = InfluxDBClient(url=url, token=token, org=organization, bucket_name=bucket)
    content = client.write_csv(files)
    return JSONResponse(status_code=200, content=content)


@facility_router.get("/info")
async def get_info_test():
    return get_facilities_info()


@facility_router.post("/read")
async def read_influxdb():
    return
