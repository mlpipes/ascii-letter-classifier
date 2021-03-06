import fire

from .dataset import save_datasets
from .train import train_model


def main():
    fire.Fire({
        'save-datasets': save_datasets,
        'train-model': train_model,
    })
