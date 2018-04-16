# version 2.4.1

import uuid
import logging
import configuration
import os.path
import couchdb
import getpass
from typing import Any
import collections
from Operators import jsonify

failure = False

# to disable all logging
#logging.disable(logging.CRITICAL)

# to re-enable all logging
logging.disable(logging.NOTSET)

# logger for the current script
logger_name = 'Model_Logger'

# log file for the whole experiment
log_file = 'workflow.log'

# create the loggers that you want to use in this file
# params : logger_name, output_file
info = configuration.logger_info(logger_name, log_file)
info_start = configuration.logger_info_start(logger_name, log_file)
info_end = configuration.logger_info_end(logger_name, log_file)
deb = configuration.logger_debug(logger_name, log_file)
warn = configuration.logger_warn(logger_name, log_file)
err = configuration.logger_error(logger_name, log_file)
fatalerr = configuration.logger_fatal(logger_name, log_file)


class User:

    def __init__(self):
        self.id = uuid.uuid4()
        self.name = getpass.getuser()

        msg = {"event": "USR-INVK", "id": str(self.id), "name": str(self.name)}

        deb.debug(jsonify(msg))







USER = User()

class Data:
    def __init__(self):
        self.id = None
        self.ref = None
        self.user = None


class Object(Data):

    def __init__(self, reference):
        # type: (Any) -> None

        self.id = uuid.uuid4()
        self.user = USER.id

        if failure is True:
            # preoondition management
            pass

        else:
            # if all preconditions passed
            try:
                self.ref = reference

                msg = {
                    'event': 'OB-CRTN',
                    'id': str(self.id),
                    'type': str(type(reference)),
                    'value': str(reference),
                    'user': str(USER.id)}

                deb.debug(jsonify(msg))

            except Exception as e:
                # if any further error occurs somehow

                msg = {
                    'event': 'OB-CRTN',
                    'id': str(self.id),
                    'type': str(type(reference)),
                    'value': str(reference),
                    'user': str(USER.id),
                    'error': str(e)}


                err.error(jsonify(msg))


class File(Data):

    def __init__(self, f):
        # type: (file) -> None

        self.id = uuid.uuid4()
        self.user = USER.id

        if failure is True:
            # precondition management
            pass

        elif not isinstance(f, file):
            # if file not found
            msg = {
                'event': 'FIL-CRTN',
                'id': str(self.id),
                'user': str(USER.id),
                'error': 'file not found'
            }

            err.error(jsonify(msg))

        else:
            # if all exceptions passed
            try:
                self.ref = f

                msg = {
                    'event': 'FIL-CRTN',
                    'id': str(self.id),
                    'type': str(type(f)),
                    'source': str(f.name),
                    'user': str(USER.id)
                }

                deb.debug(jsonify(msg))

            except Exception as e:
                # if any further exception occurs

                msg = {
                    'event': 'FIL-CRTN',
                    'id': str(self.id),
                    'type': str(type(f)),
                    'source': str(f.name),
                    'user': str(USER.id),
                    'error': str(e)
                }

                err.error(jsonify(msg))


class Document(Data):

    def __init__(self, document):
        # type: (couchdb.Document) -> None

        self.id = uuid.uuid4()
        self.user = USER.id

        if failure is True:
            # precondition management
            pass
        elif not isinstance(document, couchdb.Document):

            msg = {
                'event': 'DOC-CRTN',
                'id': str(self.id),
                'user': str(USER.id),
                'error': 'document not found'
            }


            err.error(jsonify(msg))

        else:
            # if all exceptions passed

            try:
                self.ref = document

                msg = {
                    'event': 'DOC-CRTN',
                    'id': str(self.id),
                    'type': str(type(document)),
                    'address': str(document),
                    'user': str(USER.id)
                }

                deb.debug(jsonify(msg))

            except Exception as e:
                # if any further exception occurs

                msg = {
                    'event': 'DOC-CRTN',
                    'id':  str(self.id),
                    'type':  str(type(document)),
                    'address':  str(document),
                    'user':  str(USER.id),
                    'error':  str(e)
                }



                err.error(jsonify(msg))


class Module:

    def logStart(self):
        msg = {
            'event': 'MOD-STRT',
            'id': str(self.id),
            'user': str(USER.id)
        }


        deb.debug(jsonify(msg))

    def logEnd(self):
        msg = {
            'event': 'MOD-END',
            'id': str(self.id),
            'user': str(USER.id)
        }

        deb.debug(jsonify(msg))

    def body(self):
        """
        :param interfaceParam:
        :return:
        """

    def __init__(self, *args):

        self.id = uuid.uuid4()
        self.user = USER.id

        self.P = args

        try:
            param_ids = []

            for i in args:

                if isinstance(i, Object) or isinstance(i, File) or isinstance(i, Document):
                    param_ids.append(str(i.id))

                else:
                    param_ids.append(i)

            msg = {
                'p@': param_ids,
                'event': 'MOD-CRTN',
                'id': str(self.id),
                'name': str(self.__class__.__name__),
                'user': str(USER.id)
            }

            deb.debug(jsonify(msg))

        except Exception as e:

            param_ids = []

            for i in args:
                if isinstance(i, Object) or isinstance(i, File) or isinstance(i, Document):
                    param_ids.append(str(i.id))

                else:
                    param_ids.append(i)

            msg = {
                'p@': param_ids,
                'event': 'MOD-CRTN',
                'id': str(self.id),
                'name': str(self.__class__.__name__),
                'user': str(USER.id),
                'error': str(e)
            }

            err.error(jsonify(msg))

    def run(self, when = True, false_return = None):

        if when is True:
            self.logStart()
            self.outgoing = self.body()

            ret_ids = []

            if isinstance(self.outgoing, collections.Iterable):
                for i in self.outgoing:
                    if isinstance(i, Object) or isinstance(i, File) or isinstance(i, Document):
                        ret_ids.append(str(i.id))

            else:
                if isinstance(self.outgoing, Object) or isinstance(self.outgoing, File) or isinstance(self.outgoing, Document):
                    ret_ids.append(str(self.outgoing.id))

            msg = {
                'o@': ret_ids,
                'event': 'BODY-TRU',
                'id': str(self.id),
                'name': str(self.__class__.__name__),
                'user': str(USER.id)
            }

            deb.debug(jsonify(msg))

            self.logEnd()

            return self.outgoing

        else:
            ret_ids = []

            for i in false_return:
                ret_ids.append(str(i))

            msg = {
                'o@': ret_ids,
                'event': 'BODY-FLS',
                'id': str(self.id),
                'name': str(self.__class__.__name__),
                'user': str(USER.id)
            }


            deb.debug(jsonify(msg))

            return false_return


