import logging

#def f():
    #logger = logging.getLogger("f")
    #logger.setLevel(logging.DEBUG)
    #logger.debug("in der funktion")

logging.basicConfig(filename="log.log", level=logging.INFO)

logger = logging.getLogger("meinLogger")
logger.setLevel(logging.DEBUG)
fileh = logging.FileHandler("logme.txt")
form = logging.Formatter('%(name)s - %(levelname)s : %(asctime)s - %(message)s')
fileh.setFormatter(form)
logger.addHandler(fileh)
logger.debug("debugging")

#logging.info("info")
#logging.warning("warning")
#logging.error("error")
#logging.critical("crititcal")
#f()

