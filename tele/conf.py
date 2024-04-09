import toml
import os
import logging

logger = logging.getLogger(__name__)
CONFIG_DIR = os.path.expanduser("~/.config/tele")
print(CONFIG_DIR)

if (not os.path.exists(CONFIG_DIR)):
    logger.info("Generating config folder")
    os.makedirs(CONFIG_DIR)
base_config = {
    "number": "",
    "notify-cmd": "notify-send"
}
toml_config = toml.dumps(base_config)
print(toml_config)
