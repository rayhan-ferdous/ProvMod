import uuid
import logging
import configuration
import os.path
import couchdb
import getpass

# logger for the current script
logger_name = 'Model_Logger'

# log file for the whole experiment
log_file = 'workflow.log'

# create the loggers that you want to use in this file
# params : logger_name, output_file
info_start = configuration.logger_info_start(logger_name, log_file)
info_end   = configuration.logger_info_end(logger_name, log_file)
deb  = configuration.logger_debug(logger_name, log_file)
warn = configuration.logger_warn(logger_name, log_file)
err = configuration.logger_error(logger_name, log_file)
fatalerr = configuration.logger_fatal(logger_name, log_file)

class Data:

    def __init__(self):
        self.id = None
        self.reference = None
        self.user = None

class Object(Data):

    def __init__(self, reference):

        self.id = uuid.uuid4()
        self.user = User()

        if reference is not None:

            self.reference = reference

            deb.debug('Object Data Created. (flowID, type, value, user) =  (' + str(self.id) + ', ' + str(type(reference)) + ', ' + str(reference) + ', ' + str(self.user.id) + ')' )

        else:
            err.error('Reference Not Found. (flowID) = ' + '(' + str(self.id) + ')')
            raise ReferenceError

class File(Data):

    def __init__(self, file):

        self.id = uuid.uuid4()
        self.user = User()

        if os.path.exists(file):

            self.reference = file

            deb.debug('File Data Created. (flowID, type, value, user) =  (' + str(self.id) + ',' + str(type(file)) + ', ' + str(file) + ', ' + str(self.user.id) + ')' )

        else:
            err.error('File Not Found. (flowID) = ' + '(' + str(self.id) + ')')
            raise IOError

class Document(Data):

    def __init__(self, document):

        self.id = uuid.uuid4()
        self.user = User()

        if document is not None:

            self.reference = document

            deb.debug('Document Data Created. (flowID, type, value, user) =  (' + str(self.id) + ',' + str(type(document)) + ', ' + str(document) + ', ' + str(self.user.id) + ')' )

        else:
            err.error('Document Not Found. (flowID) = ' + '(' + str(self.id) + ')')
            raise IOError

class Module:

    def __init__(self, *args):

        self.id = uuid.uuid4()
        self.user = User()
        self.incoming = None
        self.args = args

        self.incoming = args[0]
        deb.debug('Incoming Dataflow Initiated. (inFlowID, type, moduleID, user) = ' + '(' + str(self.incoming.id) + ', ' + str(self.incoming.__class__.__name__) + ', ' + str(self.id) + ', ' + str(self.user.id) + ')')



    def logStart(self):
        deb.debug('Node Invokation Started. (moduleID) = ' + '(' + str(self.id) + ')')

    def logEnd(self):
        deb.debug('Node Invokation Ended. (moduleID) = ' + '(' + str(self.id) + ')')

    def body(self):
        return None

    def run(self):
        self.logStart()

        #add type checking for outgoing
        #add logging for outgoing flow
        self.outgoing = self.body()
        self.logEnd()

        return self.outgoing


class User:

    def __init__(self):
        self.id = uuid.uuid4()
        self.name =getpass.getuser()
