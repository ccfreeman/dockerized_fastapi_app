# Dynamic Route Optimizer API

## Introduction

This API acts a proxy to the scala code for the dynamic route 
optimizer. It validates the payload, store the request payload
on Azure Blob, and queues the request payload on Azure EventBus.

Open API Spec: http://localhost:8000/docs

### Sequence Diagram 

![alt text](dataflow.png)

### Request Body

```json
{
  "data" : [{
    "ups": false,
    "drivers": [{
        "initial_depot": "",
        "final_depot": "",
        "final_depot_open": true,
        "reefer": true,
        "team": true,
        "capacity": 1234,
        "changed_clock": true,
        "used_duty_time": 1,
        "used_driving_time": 1,
        "available_time": "2021-01-27T00013:00:00z",
        "available_city": "",
        "available_state": "",
        "last_load_served_load_id":"",
        "last_load_served_stop_type":"P|D"
      }],
      "primary_optimization": true,
      "reopt_same_day": true,
      "reoptimization": true,
      "excluded_load_ids": [
        1234
      ],
      "exclude_island_loads": true,
      "carrier_code": "",
      "fuel_cost": 1234.56,
      "miles_band": [{
            "id":0,
            "miles_band": 1999,
            "cpm_v_single_driver": 2.2,
            "cpm_r_single_driver": 2.2,
            "cpm_v_team_driver": 2.2,
            "cpm_r_team_driver": 2.2
        }],
        "maximum_dead_head": 300,
        "maximum_dead_head_between_loads": 300,
        "start_day_of_week": "Monday",
        "end_day_of_week": "Monday"
    }]
}
```

## How to run this project locally

### Starting the service locally

```shell
$ docker-compose up -d --build app
```

### Stopping the service locally

```shell
$ docker-compose down --remove-orphans
```