# OpenTelemetryFlaskExample

## Prerequisites

You need to have valid Datadog agent. If you don't have one you can create one [here](https://www.datadoghq.com/).

## Running with docker-compose

First of all, you have to copy `.env_sample` file as `.env`
and add yours Datadog API Key. Then you have to check if `DD_SITE`
environment variables is set to your region in the `docker-compose.yml` file.

After that you should be ready to go. To run the containers execute the following command:
```sh
docker-compose up --b
```

This should open two containers one for `OpenTelemetryCollector` and one with Flask application.
You can enter `http://localhost:9000/hello` in your browser and see the trace and spans.

## Authors

Kamil Kucharski - kamil.kucharski95@gmail.com
