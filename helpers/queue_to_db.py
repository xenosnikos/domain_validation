from sys import exc_info
import logging
from datetime import datetime
from helpers import common_strings
from helpers.mongo_connection import db


def domainverify_response_db_addition(value, output):
    try:
        db.domainverify.find_one_and_update({common_strings.strings['mongo_value']: value},
            {'$set': {'status':common_strings.strings['status_finished'], 'timeStamp':datetime.utcnow(), 'output':output}})
    except Exception as e:
        logger = logging.getLogger(common_strings.strings['domain_verify'])
        logger.critical(common_strings.strings['database_issue'], exc_info=e)
