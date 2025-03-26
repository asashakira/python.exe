from pathlib import Path

import yaml


def read_config(file_path: str) -> dict[str, str | None] | None:
    """Read configs from a YAML file."""
    try:
        with Path(file_path).open("r", encoding="utf-8") as file:
            data = yaml.safe_load(file)
            return {
                "custid": data.get("custid"),
                "apikey": data.get("apikey"),
                "host": data.get("host"),
                "username": data.get("username"),
                "password": data.get("password"),
                "slack_webhook_url": data.get("slack_webhook_url"),
                "remote_path": data.get("remote_path"),
            }
    except FileNotFoundError:
        print("Error: File '%s' not found.", file_path)
        return None

    except yaml.YAMLError:
        print("Error parsing YAML")
        return None


def main():
    config = read_config("config.yaml")
    print(config)


if __name__ == "__main__":
    main()
