import os
from collections import defaultdict
import time
from datetime import datetime, timedelta
from http.client import HTTPException
from typing import List, Dict, Any

import warnings

from fastapi import UploadFile, File
from influxdb_client.client.warnings import MissingPivotFunction

import pandas as pd
from influxdb_client import InfluxDBClient

from app.domain.facility.model.facility_data import FacilityData, TGLifeData
from app.domain.facility.repository.influx_client import InfluxGTRClient
from app.domain.facility.service.facility_query import section_query, execute_query, field_by_time_query, \
    info_field_query, \
    info_measurements_query
from app.domain.section.model.section_data import SectionData
from config import settings

url = settings.influx_url
token = settings.influx_token
organization = settings.influx_org
bucket = settings.influx_bucket

warnings.simplefilter('ignore', MissingPivotFunction)


# --------- functions --------- #

def write_files(files: List[UploadFile] = File(...)):
    client = InfluxGTRClient(url=url, token=token, org=organization, bucket_name=bucket)
    contents = client.write_csv(files)
    return contents
def get_facilities_info():
    client = InfluxGTRClient(url=url, token=token, org=organization, bucket_name=bucket)
    contents = client.read_info()
    return contents
# get data
def get_datas(conditions: List[SectionData]):
    client = InfluxGTRClient(url=url, token=token, org=organization, bucket_name=bucket)
    contents = client.read_data(conditions)
    return contents

def get_TG_datas(condition: TGLifeData):
    client = InfluxGTRClient(url=url, token=token, org=organization, bucket_name=bucket)
    contents = client.read_TG_data(condition)
    return contents

# get df TRC
def get_df_TRC(condition: FacilityData):
    client = InfluxDBClient(url=url, token=token, org=organization)
    query = section_query(bucket, facility=condition.facility,
                          start_date=condition.startTime, end_date=condition.endTime)
    try:
        return execute_query(client, query)
    except Exception as e:
        raise HTTPException(500, str(e))
# get section information by FacilityData
def get_section(condition: FacilityData):
    client = InfluxDBClient(url=url, token=token, org=organization)
    query = section_query(bucket, facility=condition.facility,
                          start_date=condition.startTime, end_date=condition.endTime)
    try:
        return execute_query(client, query)
    except Exception as e:
        raise HTTPException(500, str(e))
