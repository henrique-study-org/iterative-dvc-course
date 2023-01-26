import yaml
import argparse
from sklearn.datasets import load_iris


def data_load(config_path: str) -> None:
    try:
        config = yaml.safe_load(open(config_path, "r"))
    except Exception as e:
        raise ValueError(
            f"Could not load the config file at '{config_path}'. Error: {e}")

    data = load_iris(as_frame=True)
    dataset = data.frame

    dataset.to_csv(config["data"]["dataset_csv"], index=False)
    print("Data load completed!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", dest="config", required=True)
    args = parser.parse_args()

    data_load(config_path=args.config)
