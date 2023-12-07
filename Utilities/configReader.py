"""
This is the utility for reading the various ECAT locators that are stored in the configuration file.
Configparser needs to be imported for it to work seamlessly.
"""

from configparser import ConfigParser
import os

file_path = os.path.join(os.path.dirname(__file__), '..', 'Locators','locators.ini')  # this will help in reading the configurationData file


# config = ConfigParser()
# config.read("config.ini")
# print(config.get("locator", "username"))
# print(config.get("common info", "testsiteurl"))

def readconfig(section, key):
    config = ConfigParser()
    config.read(file_path)
    return config.get(section, key)
