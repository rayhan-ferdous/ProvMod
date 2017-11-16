import uuid
import logging
import configuration
import os.path
import couchdb
import getpass
from typing import Any

failure = False

# to disable all logging
#logging.disable(logging.CRITICAL)

# to re-enable all logging
logging.disable(logging.DEBUG)

# logger for the current script
logger_name = 'Model_Logger'

# log file for the whole experiment
log_file = 'workflow.log'

# create the loggers that you want to use in this file
# params : logger_name, output_file
info = configuration.logger_info(logger_name, log_file)
info_start = configuration.logger_info_start(logger_name, log_file)
info_end   = configuration.logger_info_end(logger_name, log_file)
deb  = configuration.logger_debug(logger_name, log_file)
warn = configuration.logger_warn(logger_name, log_file)
err = configuration.logger_error(logger_name, log_file)
fatalerr = configuration.logger_fatal(logger_name, log_file)


class Data:

    def __init__(self):
        self.id = None
        self.ref = None
        self.user = None

class Object(Data):

    def __init__(self, reference):
        # type: (Any) -> None

        self.id = uuid.uuid4()
        self.user = User()

        if failure is True:
            # preoondition management
            pass

        else:
            # if all preconditions passed
            try:
                self.ref = reference

                deb.debug('Object Data Created. (flowID, type, value, user) =  (' + str(self.id) + ', ' + str(
                    type(reference)) + ', ' + str(reference) + ', ' + str(self.user.id) + ')')
                info.info('object data created >>> (objID, obj) = (' + str(self.id) + ', ' + str(self.ref) + ')')

            except Exception as e:
                # if any further error occurs somehow
                err.error(str(e) + '. (flowID) = ' + '(' + str(self.id) + ')')

class File(Data):

    def __init__(self, f):
        # type: (file) -> None

        self.id = uuid.uuid4()
        self.user = User()

        if failure is True:
            # precondition management
            pass

        elif not isinstance(f, file):
            # if file not found
            err.error(str(IOError) + '. (flowID) = ' + '(' + str(self.id) + ')')

        else:
            # if all exceptions passed
            try:
                self.ref = f

                deb.debug('File Data Created. (flowID, type, value, user) =  (' + str(self.id) + ',' + str(
                    type(f)) + ', ' + str(f) + ', ' + str(self.user.id) + ')')
                info.info('file data created >>> (fileID, name) = (' + str(self.id) + ', ' + str(self.ref) + ')')

            except Exception as e:
                # if any further exception occurs
                err.error(str(e) + '. (flowID) = ' + '(' + str(self.id) + ')')

class Document(Data):

    def __init__(self, document):
        # type: (couchdb.Document) -> None

        self.id = uuid.uuid4()
        self.user = User()

        if failure is True:
            # precondition management
            pass
        elif not isinstance(document, couchdb.Document):
            err.error(str(IOError) + '. (flowID) = ' + '(' + str(self.id) + ')')

        else:
            # if all exceptions passed

            try:
                self.ref = document

                deb.debug('Document Data Created. (flowID, type, value, user) =  (' + str(self.id) + ',' + str(
                    type(document)) + ', ' + str(document) + ', ' + str(self.user.id) + ')')

                info.info(
                    'document data created >>> (docID, doc) = (' + str(self.id) + ', ' + str(self.ref) + ')')

            except Exception as e:
                # if any further exception occurs
                err.error(str(e) + '. (flowID) = ' + '(' + str(self.id) + ')')


class Module:

    def logStart(self):
        deb.debug('Node Invokation Started. (moduleID) = ' + '(' + str(self.id) + ')')

        info.info('module start >>> (modID) = (' + str(self.__class__.__name__) + ')')

    def logEnd(self):
        deb.debug('Node Invokation Ended. (moduleID) = ' + '(' + str(self.id) + ')')

        info.info('module end >>> (modID) = (' + str(self.__class__.__name__) + ')')

    def body(self):
        '''
        :param interfaceParam:
        :return:
        '''

    def __init__(self, *args):

        self.id = uuid.uuid4()
        self.user = User()

        self.P = args

        try:

            log = ''
            for i in args:
                if isinstance(i, Object) or isinstance(i, File) or isinstance(i, Document):
                    log = log + '(' + str(i.id) + ', ' + str(i.__class__.__name__) + '), '
                else:
                    log = log +  str(i) + ', '

            deb.debug('Module Initiated. (inFlow, moduleID, user) = ' + '(' + log + ', ' + str(
                self.id) + ', ' + str(
                self.user.id) + ')')

            info.info('module initiated >>> (modID, input) = (' + str(self.id) + ', ' + log)

        except Exception as e:
            err.error(str(e))

    def run(self, when = True):

        if when is True:
            self.logStart()
            self.outgoing = self.body()

            log = ''
            for i in self.outgoing:
                log = log + str(i.id) + ', '

            info.info('module flows >>> (modID, outIDs) = (' + str(self.id) + ', ' + log + ')')
            self.logEnd()

            return self.outgoing

        else:
            return None

class User:

    def __init__(self):
        self.id = uuid.uuid4()
        self.name =getpass.getuser()

        #info.info('user targeted with id ' + str(self.name))
