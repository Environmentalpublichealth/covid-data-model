import click 

from libs.dataset_deployer import DatasetDeployer

@click.command()
@click.option('--input', '-i', default='results', help='Input directory of state/county projections')
@click.option('--output', '-o', default='results/dod', help='Output directory for artifacts')
def deploy(input, output):
    # for counties
    # get the state intervention 
    # load the file for that state intervention &
    pass 
    
if __name__ == "__main__":
    """Used for manual trigger

    # triggering persistance to s3
    AWS_PROFILE=covidactnow BUCKET_NAME=covidactnow-deleteme python deploy_critical_counties_dataset.py

    # deploy to the data bucket
    AWS_PROFILE=covidactnow BUCKET_NAME=data.covidactnow.org python deploy_critical_counties_dataset.py

    # triggering persistance to local
    python deploy_critical_counties_dataset.py
    """
    # pylint: disable=no-value-for-parameter
    deploy()
