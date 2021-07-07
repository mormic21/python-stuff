import logging

def f():
    logger = logging.getLogger("f")
    logger.setLevel(logging.DEBUG)
    logging.debug("in der funktion")

logging.basicConfig(filename="log.log", level=logging.INFO)
logging.debug("debugging")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("crititcal")
f()

