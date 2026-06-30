import click
import json

from pipeline import run_pipeline
from projection.projector import project


@click.command()

@click.option('--csv')
@click.option('--ats')
@click.option('--resume')
@click.option('--notes')
@click.option('--config')

def main(csv, ats, resume, notes, config):

    profile = run_pipeline({
        "csv": csv,
        "ats": ats,
        "resume": resume,
        "notes": notes
    })

    with open(config) as f:
        cfg = json.load(f)

    output = project(profile, cfg)

    print(
        json.dumps(
            output,
            indent=2
        )
    )


if __name__ == "__main__":
    main()