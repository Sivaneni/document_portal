import yaml
def load_config(config_path: str = "config\config.yaml") -> dict:
    """
    Load configuration from a YAML file.

    Args:
        config_path (str): Path to the YAML configuration file.

    Returns:
        dict: Configuration data loaded from the file.
    """
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
        #print(config)
    return config

load_config()  # Call the function to load the config
   