'''
Logging in Python: Logging is a means of tracking events that happen when some software runs.
Logging is important for software developing, debugging and running.
If you don't have any logging record and your program crashes,
 there are very little chances that you detect the cause of the problem.
'''



import logging


logging.basicConfig(filename="MyFIle",level=logging.DEBUG)
logging.critical("Error")
logging.error("Error")
logging.warning("Error")
logging.info("Error")
logging.debug("Error")

