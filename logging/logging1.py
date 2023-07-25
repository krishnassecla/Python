import logging

# start loggging mesasges from level DEBUG
# logging.basicConfig(level=logging.DEBUG)


# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')

logging.basicConfig(filename='file.log', filemode='w', format="%(name) %(levelname) - %(message)")
logging.error("This will get loggged")
