import logging
import time,os

Date = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
log = '{0}/log/{1}-log'.format(os.getcwd(), Date)
FORMAT = '%(asctime)s |%(levelname)6s | %(module)s- %(message)s'
DATEFMT = '%Y-%m-%d %H:%M:%S'
logging.basicConfig(level=logging.DEBUG, format=FORMAT,
  datefmt=DATEFMT,
  filename=log,
  filemode='a')
consoleLog = logging.StreamHandler()
consoleLog.setLevel(logging.DEBUG)
consoleLog.setFormatter(logging.Formatter(FORMAT, DATEFMT))
logging.getLogger('').addHandler(consoleLog)

