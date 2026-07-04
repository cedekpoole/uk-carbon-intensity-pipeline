# Carbon Intensity Analytics Mart

A data engineering portfolio project for collecting and modelling UK electricity carbon intensity data.

## Current Milestone

Milestone 1 focuses on local API ingestion only. The goal is to understand the Carbon Intensity API, fetch current carbon intensity and generation mix data, validate response shapes, and save timestamped raw JSON snapshots locally.

Snowflake, dbt, Prefect, and dashboards are intentionally out of scope for this milestone.

## Data Source

This project uses the public Carbon Intensity API:

- Base URL: `https://api.carbonintensity.org.uk`
- Initial endpoints: `/intensity` and `/generation`

## API Exploration

### `/intensity`

Purpose: fetch the current national carbon intensity period.

Expected response shape:

- Top-level `data` field is a list.
- Each record contains `from`, `to`, and `intensity`.
- `intensity` contains `forecast`, `actual`, and `index`.

### `/generation`

Purpose: fetch the current national generation mix.

Expected response shape:

- Top-level `data` field is an object.
- `data` contains `from`, `to`, and `generationmix`.
- `generationmix` is a list of records with `fuel` and `perc`.

## Milestone 1 Goals

- Explore the API before building against it.
- Fetch current intensity and generation mix responses.
- Validate that responses contain the expected fields.
- Wrap raw responses with metadata such as fetch time, source URL, endpoint, and data.
- Save raw JSON snapshots under `data/raw/carbon/`.
- Add simple pytest coverage for validation and saving.

## Roadmap

- Current: local API ingestion setup and API exploration.
- In progress: response validation, metadata wrapping, and raw JSON snapshot saving.
- Planned: Snowflake warehouse loading, dbt-snowflake analytics models, Prefect orchestration, expanded pytest coverage, and an optional Streamlit dashboard.
