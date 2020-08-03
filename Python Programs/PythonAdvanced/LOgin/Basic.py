import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
fh = logging.FileHandler(r'gtec.log')
fh.setLevel(logging.INFO)
logger.addHandler(fh)
formatter = logging.Formatter('%asctime)s- %(name)s-%(levelname)s- %(message)s')
fh.setFormatter(formatter)
