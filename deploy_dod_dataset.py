#!/usr/bin/env python
from io import BytesIO
import boto3
import click
import os
import logging

from libs.enums import Intervention
from libs.dataset_deployer import DatasetDeployer
from libs.validate_results import validate_states_df, validate_counties_df, validate_states_shapefile, validate_counties_shapefile
from libs.build_dod_dataset import get_usa_by_county_with_projection_df, get_usa_by_states_df
from libs.functions.generate_shapefiles import get_usa_county_shapefile, get_usa_state_shapefile

logger = logging.getLogger(__name__)
PROD_BUCKET = "data.covidactnow.org"

def upload_csv(key_name, csv, output_dir): 
    blob = {
        'key': f'{key_name}.csv',
        'body': csv,
        'output_dir': output_dir,
        }
    obj = DatasetDeployer(**blob)
    obj.persist()
    logger.info(f"Generated csv for {key_name}")


@click.command()
@click.option('--run_validation', '-r', default=True, help='Run the validation on the deploy command')
@click.option('--input', '-i', default='results', help='Input directory of state/county projections')
@click.option('--output', '-o', default='results/dod', help='Output directory for artifacts')
def deploy(run_validation, input, output):
    """The entry function for invocation"""

    for intervention_enum in list(Intervention): 
        logger.info(f"Starting to generate files for {intervention_enum.name}.")

        states_key_name = f'states.{intervention_enum.name}'
        states_df = get_usa_by_states_df(input, intervention_enum.value)
        if run_validation: 
            validate_states_df(states_key_name, states_df)
        upload_csv(states_key_name, states_df.to_csv(), output)

        states_shp = BytesIO()
        states_shx = BytesIO()
        states_dbf = BytesIO()
        get_usa_state_shapefile(states_df, states_shp, states_shx, states_dbf)
        if run_validation: 
            validate_states_shapefile(states_key_name, states_shp, states_shx, states_dbf)
        DatasetDeployer(key=f'{states_key_name}.shp', body=states_shp.getvalue(), output_dir=output).persist()
        DatasetDeployer(key=f'{states_key_name}.shx', body=states_shx.getvalue(), output_dir=output).persist()
        DatasetDeployer(key=f'{states_key_name}.dbf', body=states_dbf.getvalue(), output_dir=output).persist()
        logger.info(f"Generated state shape files for {intervention_enum.name}")

        counties_key_name = f'counties.{intervention_enum.name}'
        counties_df = get_usa_by_county_with_projection_df(input, intervention_enum.value)
        if run_validation: 
            validate_counties_df(counties_key_name, counties_df)
        upload_csv(counties_key_name, counties_df.to_csv(), output)

        counties_shp = BytesIO()
        counties_shx = BytesIO()
        counties_dbf = BytesIO()
        get_usa_county_shapefile(counties_df, counties_shp, counties_shx, counties_dbf)
        if run_validation: 
            validate_counties_shapefile(counties_key_name, counties_shp, counties_shx, counties_dbf)
        DatasetDeployer(key=f'{counties_key_name}.shp', body=counties_shp.getvalue(), output_dir=output).persist()
        DatasetDeployer(key=f'{counties_key_name}.shx', body=counties_shx.getvalue(), output_dir=output).persist()
        DatasetDeployer(key=f'{counties_key_name}.dbf', body=counties_dbf.getvalue(), output_dir=output).persist()
        logger.info(f"Generated counties shape files for {intervention_enum.name}")

    print('finished dod job')


if __name__ == "__main__":
    """Used for manual trigger

    # triggering persistance to s3
    AWS_PROFILE=covidactnow BUCKET_NAME=covidactnow-deleteme python deploy_dod_dataset.py

    # deploy to the data bucket
    AWS_PROFILE=covidactnow BUCKET_NAME=data.covidactnow.org python deploy_dod_dataset.py

    # triggering persistance to local
    python deploy_dod_dataset.py
    """
    # pylint: disable=no-value-for-parameter
    deploy()
