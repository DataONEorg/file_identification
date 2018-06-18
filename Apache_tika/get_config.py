import tika
from tika import config
print(config.getParsers())
print(config.getMimeTypes())
print(config.getDetectors())
