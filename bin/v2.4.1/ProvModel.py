# version 2.4.1

import uuid
import logging
import configuration
import os.path
import couchdb
import getpass
from typing import Any
import collections

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
info_end   = configuration.logger_info_end(logger_name, log_file)
deb  = configuration.logger_debug(logger_name, log_file)
warn = configuration.logger_warn(logger_name, log_file)
err = configuration.logger_error(logger_name, log_file)
fatalerr = configuration.logger_fatal(logger_name, log_file)


class User:

    def __init__(self):
        self.id = uuid.uuid4()
        self.name =getpass.getuser()

        msg = []
        msg.append('event :: ' + 'user invocation')
        msg.append('id :: ' + str(self.id))
        msg.append('name :: ' + str(self.name))

        deb.debug(';'.join(msg))


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

                msg = []
                msg.append('event :: ' + 'object data creation')
                msg.append('id :: ' + str(self.id))
                msg.append('type :: ' + str(type(reference)) )
                msg.append('value :: ' + str(reference))
                msg.append('user :: ' + str(USER.id))

                deb.debug(';'.join(msg))

            except Exception as e:
                # if any further error occurs somehow

                msg = []
                msg.append('event :: ' + 'object data creation')
                msg.append('id :: ' + str(self.id))
                msg.append('type :: ' + str(type(reference)))
                msg.append('value :: ' + str(reference))
                msg.append('user :: ' + str(USER.id))
                msg.append('error :: ' + str(e))

                err.error(';'.join(msg))


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
            msg = []
            msg.append('event :: ' + 'file data creation')
            msg.append('id :: ' + str(self.id))
            msg.append('user :: ' + str(USER.id))
            msg.append('error :: ' + 'file not found')

            err.error(';'.join(msg))

        else:
            # if all exceptions passed
            try:
                self.ref = f

                msg = []
                msg.append('event :: ' + 'file data creation')
                msg.append('id :: ' + str(self.id))
                msg.append('type :: ' + str(type(f)))
                msg.append('source :: ' + str(f.name))
                msg.append('user :: ' + str(USER.id))

                deb.debug(';'.join(msg))

            except Exception as e:
                # if any further exception occurs

                msg = []
                msg.append('event :: ' + 'file data creation')
                msg.append('id :: ' + str(self.id))
                msg.append('type :: ' + str(type(f)))
                msg.append('source :: ' + str(f.name))
                msg.append('user :: ' + str(USER.id))
                msg.append('error :: ' + str(e))

                err.error(';'.join(msg))


class Document(Data):

    def __init__(self, document):
        # type: (couchdb.Document) -> None

        self.id = uuid.uuid4()
        self.user = USER.id

        if failure is True:
            # precondition management
            pass
        elif not isinstance(document, couchdb.Document):
            msg = []
            msg.append('event :: ' + 'document data creation')
            msg.append('id :: ' + str(self.id))
            msg.append('user :: ' + str(USER.id))
            msg.append('error :: ' + 'document not found')
            err.error(';'.join(msg))

        else:
            # if all exceptions passed

            try:
                self.ref = document

                msg = []
                msg.append('event :: ' + 'document data creation')
                msg.append('id :: ' + str(self.id))
                msg.append('type :: ' + str(type(document)))
                msg.append('address :: ' + str(document))
                msg.append('user :: ' + str(USER.id))

                deb.debug(';'.join(msg))

            except Exception as e:
                # if any further exception occurs

                msg = []
                msg.append('event :: ' + 'document data creation')
                msg.append('id :: ' + str(self.id))
                msg.append('type :: ' + str(type(document)))
                msg.append('address :: ' + str(document))
                msg.append('user :: ' + str(USER.id))
                msg.append('error :: ' + str(e))

                err.error(';'.join(msg))


class Module:

    def logStart(self):
        msg = []
        msg.append('event :: ' + 'module start')
        msg.append('id :: ' + str(self.id))
        msg.append('user :: ' + str(USER.id))
        deb.debug(';'.join(msg))

    def logEnd(self):
        msg = []
        msg.append('event :: ' + 'module end')
        msg.append('id :: ' + str(self.id))
        msg.append('user :: ' + str(USER.id))
        deb.debug(';'.join(msg))

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

            msg = []
            count = 0

            for i in args:
                if isinstance(i, Object) or isinstance(i, File) or isinstance(i, Document):
                    msg.append('p@' + str(count) + ' :: ' + str(i.id))
                    msg.append('p@@' + str(count) + ' :: ' + str(i.__class__.__name__))
                    count += 1
                else:
                    msg.append('p@' + str(count) + ' :: ' + str(i))
                    msg.append('p@@' + str(count) + ' :: ' + str(i.__class__.__name__))
                    count += 1

            msg.append('event :: ' + 'module creation')
            msg.append('id :: ' + str(self.id))
            msg.append('name :: ' + str(self.__class__.__name__))
            msg.append('user :: ' + str(USER.id))

            deb.debug(';'.join(msg))

        except Exception as e:

            msg = []
            count = 0

            for i in args:
                if isinstance(i, Object) or isinstance(i, File) or isinstance(i, Document):
                    msg.append('p@' + str(count) + ' :: ' + str(i.id))
                    msg.append('p@@' + str(count) + ' :: ' + str(i.__class__.__name__))
                    count += 1
                else:
                    msg.append('p@' + str(count) + ' :: ' + str(i))
                    msg.append('p@@' + str(count) + ' :: ' + str(i.__class__.__name__))
                    count += 1

            msg.append('event :: ' + 'module creation')
            msg.append('id :: ' + str(self.id))
            msg.append('name :: ' + str(self.__class__.__name__))
            msg.append('user :: ' + str(USER.id))
            msg.append('error :: ' + str(e))

            err.error(';'.join(msg))

    def run(self, when = True, false_return = None):

        if when is True:
            self.logStart()
            self.outgoing = self.body()

            msg = []

            if isinstance(self.outgoing, collections.Iterable):
                count = 0

                for i in self.outgoing:
                    if isinstance(i, Object) or isinstance(i, File) or isinstance(i, Document):
                        msg.append('o@' + str(count) + ' :: ' + str(i.id))
                        msg.append('o@@' + str(count) + ' :: ' + str(i.__class__.__name__))
                        count += 1
            else:
                if isinstance(self.outgoing, Object) or isinstance(self.outgoing, File) or isinstance(self.outgoing, Document):
                    msg.append('o@' + '0' + ' :: ' + str(self.outgoing.id))
                    msg.append('o@@' + '0' + ' :: ' + str(self.outgoing.__class__.__name__))


            msg.append('event :: ' + 'module execution true')
            msg.append('id :: ' + str(self.id))
            msg.append('name :: ' + str(self.__class__.__name__))
            msg.append('user :: ' + str(USER.id))

            deb.debug(';'.join(msg))

            self.logEnd()

            return self.outgoing

        else:
            msg = []
            count = 0

            for i in false_return:
                msg.append('o@' + str(count) + ' :: ' + str(i))
                msg.append('o@@' + str(count) + ' :: ' + str(i.__class__.__name__))
                count += 1

            msg.append('event :: ' + 'module execution false')
            msg.append('id :: ' + str(self.id))
            msg.append('name :: ' + str(self.__class__.__name__))
            msg.append('user :: ' + str(USER.id))

            deb.debug(';'.join(msg))

            return false_return


