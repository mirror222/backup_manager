import logging
import logging.handlers
import datetime

log_filename = 'backup_events.log'
log_filesize = 100000000


log = logging.getLogger('backup_manager')
log.setLevel(logging.INFO)
handler = logging.handlers.RotatingFileHandler(log_filename, maxBytes=log_filesize, backupCount=5)
log.addHandler(handler)

log.info('Application started @ ' + str(datetime.datetime.now()))


