

from datetime import datetime
import uuid
import logging
import configuration
import os.path
import couchdb
import getpass
from typing import Any
import collections
from Operators import jsonify
import os
import psutil

''' GDB part '''
from py2neo import Graph

graph  = Graph(password = 'password')
#graph.delete_all()

''' modelling part '''
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

def elasticuser(id, name, time):
    #print 'curl XPUT 127.0.0.1:9200/provenance/users/' + str(id) + ' -d\' {"time": "' + str(time) + '", "name": "' + str(name) + '"}\' '
    os.system('curl --silent --output XPUT 127.0.0.1:9200/userindex/users/' + str(id) + ' -d\' {"time": "' + str(time) + '", "name": "' + str(name) + '"}\' ')


class User:

    def __init__(self):
        self.id = uuid.uuid4()
        self.name = getpass.getuser()

        msg = {"event": "USR-INVK", "id": str(self.id), "name": str(self.name), 'time': str( datetime.utcnow() )}

        deb.debug(jsonify(msg))

        elasticuser(msg['id'], msg['name'], msg['time'])







USER = User()

class Data:
    def __init__(self):
        self.id = None
        self.ref = None
        self.user = None

def elasticobject(id, type, value, user, memory, cpu, time, error):
    #print 'curl XPUT 127.0.0.1:9200/objectindex/modules/' + str(id) + ' -d\' {"time": "' + str(time) + '", "type": "' + str(type) + '", "value": "' + str(value) + '", "user": "' + str(user) + '", "memory": ' + str(memory) + ', "cpu": ' + str(cpu) + ', "error": "' + str(error) + '"    }\' '
    os.system('curl --silent --output XPUT 127.0.0.1:9200/objectindex/objects/' + str(id) + ' -d\' {"time": "' + str(time) + '", "type": "' + str(type) + '", "value": "' + str(value) + '", "user": "' + str(user) + '", "memory": ' + str(memory) + ', "cpu": ' + str(cpu) + ', "error": "' + str(error) + '"    }\' ')



class Object(Data):

    def __init__(self, reference):
        # type: (Any) -> None

        self.id = uuid.uuid4()
        self.user = USER.id

        if failure is True:
            # precondition management
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
                    'user': str(USER.id),
                    'memory': (psutil.virtual_memory()[3]),
                    'cpu': (psutil.cpu_percent()),
                    'time': str(datetime.utcnow()),
                    'label': 'object',
                    'error': 'success'
                }



                deb.debug(jsonify(msg))

                elasticobject(msg['id'], msg['type'], msg['value'], msg['user'], msg['memory'], msg['cpu'], msg['time'], msg['error'])

                ''' GDB part '''
                props = ['VALUE:\"' + msg['value'] + '\"', 'id:\"' + msg['id'] + '\"', 'type:\"' + msg['type'] + '\"', 'user:\"' + msg['user'] + '\"', 'error:\"null\"', 'time:\"' + str(msg['time']) + '\"', 'memory:\"' + str(msg['memory']) + '\"', 'cpu:\"' + str(msg['cpu']) + '\"', 'label:\"' + str(msg['label']) + '\"']
                propsQuery = ','.join(props)
                #print propsQuery
                query = 'create (n:Object{' + propsQuery + '})'
                graph.run(query)







            except Exception as e:
                # if any further error occurs somehow

                #pid = os.getpid()
                #py = psutil.Process(pid)
                #memoryUse = py.memory_info()[0] / 2. ** 30

                msg = {
                    'event': 'OB-CRTN',
                    'id': str(self.id),
                    'type': str(type(reference)),
                    'value': str(reference),
                    'user': str(USER.id),
                    'error': 'OCE',
                    'memory': (psutil.virtual_memory()[3]),
                    'cpu': (psutil.cpu_percent()),
                    'time': str(datetime.utcnow()),
                    'label': 'object'
                }


                err.error(jsonify(msg))

                elasticobject(msg['id'], msg['type'], msg['value'], msg['user'], msg['memory'], msg['cpu'],
                               msg['time'], msg['error'])


                ''' GDB part '''
                props = ['VALUE:\"' + msg['value'] + '\"', 'id:\"' + msg['id'] + '\"', 'type:\"' + msg['type'] + '\"', 'user:\"' + msg['user'] + '\"', 'error:\"' + msg['error'] + '\"', 'time:\"' + str(msg['time']) + '\"', 'memory:\"' + str(msg['memory']) + '\"', 'cpu:\"' + str(msg['cpu']) + '\"', 'label:\"' + str(msg['label']) + '\"']
                propsQuery = ','.join(props)
                #print propsQuery
                query = 'create (n:Object{' + propsQuery + '})'
                graph.run(query)



def elasticfile(id, user, source, memory, cpu, time, error):
    #print 'curl XPUT 127.0.0.1:9200/fileindex/files/' + str(id) + ' -d\' {"time": "' + str(time) + '", "user": "' + str(user) + '", "source": "' + str(source) + '", "memory": ' + str(memory) + ', "cpu": ' + str(cpu) + ', "error": "' + str(error) + '"    }\' '
    os.system('curl --silent --output XPUT 127.0.0.1:9200/fileindex/files/' + str(id) + ' -d\' {"time": "' + str(time) + '", "user": "' + str(user) + '", "source": "' + str(source) + '", "memory": ' + str(memory) + ', "cpu": ' + str(cpu) + ', "error": "' + str(error) + '"    }\' ')


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
                'error': 'FCE',
                'memory': (psutil.virtual_memory()[3]),
                'cpu': (psutil.cpu_percent()),
                'time': str(datetime.utcnow()),
                'label': 'file'
            }

            err.error(jsonify(msg))

            elasticfile(msg['id'], msg['user'], 'InvalidFile', msg['memory'], msg['cpu'], msg['time'], msg['error'])

            ''' GDB part   this part is never executed
            props = ['SOURCE:\"' + msg['source'] + '\"', 'id:\"' + msg['id'] + '\"', 'type:\"' + msg['type'] + '\"',
                     'user:\"' + msg['user'] + '\"', 'error:\"' + msg['error'] + '\"', 'time:\"' + str(msg['time']) + '\"',
                     'memory:\"' + str(msg['memory']) + '\"', 'cpu:\"' + str(msg['cpu']) + '\"']
            propsQuery = ','.join(props)
            # print propsQuery
            query = 'create (n:File{' + propsQuery + '})'
            graph.run(query)
            '''

        else:
            # if all exceptions passed
            try:
                self.ref = f



                msg = {
                    'event': 'FIL-CRTN',
                    'id': str(self.id),
                    'type': str(type(f)),
                    'source': str(f.name),
                    'user': str(USER.id),
                    'memory': (psutil.virtual_memory()[3]),
                    'cpu': (psutil.cpu_percent()),
                    'time': str(datetime.utcnow()),
                    'label': 'file',
                    'error': 'success'
                }

                deb.debug(jsonify(msg))

                elasticfile(msg['id'], msg['user'], msg['source'] ,msg['memory'], msg['cpu'], msg['time'], msg['error'])

                ''' GDB part '''
                props = ['SOURCE:\"' + msg['source'] + '\"', 'id:\"' + msg['id'] + '\"', 'type:\"' + msg['type'] + '\"', 'user:\"' + msg['user'] + '\"', 'error:\"null\"', 'time:\"' + str(msg['time']) + '\"',
                         'memory:\"' + str(msg['memory']) + '\"', 'cpu:\"' + str(msg['cpu']) + '\"', 'label:\"' + str(msg['label']) + '\"']
                propsQuery = ','.join(props)
                #print propsQuery
                query = 'create (n:File{' + propsQuery + '})'
                graph.run(query)




            except Exception as e:
                # if any further exception occurs



                msg = {
                    'event': 'FIL-CRTN',
                    'id': str(self.id),
                    'type': str(type(f)),
                    'source': str(f.name),
                    'user': str(USER.id),
                    'error': 'OE',
                    'memory': (psutil.virtual_memory()[3]),
                    'cpu': (psutil.cpu_percent()),
                    'time': str(datetime.utcnow()),
                    'label': 'file'
                }

                err.error(jsonify(msg))

                elasticfile(msg['id'], msg['user'], msg['source'], msg['memory'], msg['cpu'], msg['time'], msg['error'])

                ''' GDB part '''
                props = ['SOURCE:\"' + msg['source'] + '\"', 'id:\"' + msg['id'] + '\"', 'type:\"' + msg['type'] + '\"',
                         'user:\"' + msg['user'] + '\"', 'error:\"' + msg['error'] + '\"', 'time:\"' + str(msg['time']) + '\"',
                         'cpu:\"' + str(msg['cpu']) + '\"', 'memory:\"' + str(msg['memory']) + '\"', 'label:\"' + str(msg['label']) + '\"']
                propsQuery = ','.join(props)
                # print propsQuery
                query = 'create (n:File{' + propsQuery + '})'
                graph.run(query)


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
                'error': 'error',
                'memory': (psutil.virtual_memory()[3]),
                'cpu': (psutil.cpu_percent()),
                'time': str(datetime.utcnow()),
                'label': 'document'
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
                    'user': str(USER.id),
                    'memory': (psutil.virtual_memory()[3]),
                    'cpu': (psutil.cpu_percent()),
                    'time': str(datetime.utcnow()),
                    'label': 'document'
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
                    'error':  'error',
                    'memory': (psutil.virtual_memory()[3]),
                    'cpu': (psutil.cpu_percent()),
                    'time': str(datetime.utcnow()),
                    'label': 'document'
                }



                err.error(jsonify(msg))


def elasticmodule(id, time, name, user, memory_run, memory_init, cpu_run, cpu_init, duration_run, duration_init, error):
    #print 'curl XPUT 127.0.0.1:9200/moduleindex/modules/' + str(id) + ' -d\' {"time": "' + str(time) + '", "name": "' + str(name) + '", "user": "' + str(user) + '", "memory_run": ' + str(memory_run) + ', "memory_init": ' + str(memory_init) + ', "cpu_run": ' + str(cpu_run) + ', "cpu_init": ' + str(cpu_init) + ', "duration_run": "' + str(duration_run) + '", "duration_init": "' + str(duration_init) + '", "error": "' + str(error) + '"    }\' '
    os.system('curl --silent --output XPUT 127.0.0.1:9200/moduleindex/modules/' + str(id) + ' -d\' {"time": "' + str(time) + '", "name": "' + str(name) + '", "user": "' + str(user) + '", "memory_run": ' + str(memory_run) + ', "memory_init": ' + str(memory_init) + ', "cpu_run": ' + str(cpu_run) + ', "cpu_init": ' + str(cpu_init) + ', "duration_run": "' + str(duration_run) + '", "duration_init": "' + str(duration_init) + '", "error": "' + str(error) + '"    }\' ')


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

        start_time = datetime.utcnow()

        self.id = uuid.uuid4()
        self.user = USER.id

        self.P = args

        try:
            param_ids = []

            for i in args:

                if isinstance(i, Object) or isinstance(i, File) or isinstance(i, Document):
                    param_ids.append(str(i.id))

                else:
                    param_ids.append(str(i))



            msg = {
                'p@': param_ids,
                'event': 'MOD-CRTN',
                'id': str(self.id),
                'name': str(self.__class__.__name__),
                'user': str(USER.id),
                'memory_init': (psutil.virtual_memory()[3]),
                'cpu_init': (psutil.cpu_percent()),
                'duration_init': str(datetime.utcnow()-start_time),
                'time': str(datetime.utcnow()),
                'cpu_run': 0,
                'memory_run': 0,
                'duration_run': "00:00:00.000000",
                'label': 'module',
                'error': 'success'
            }

            deb.debug(jsonify(msg))

            elasticmodule(msg['id'], msg['time'], msg['name'], msg['user'], msg['memory_run'], msg['memory_init'], msg['cpu_run'], msg['cpu_init'], msg['duration_run'], msg['duration_init'], msg['error'])

            ''' GDB part '''
            props = ['NAME:\"' + msg['name'] + '\"', 'id:\"' + msg['id'] + '\"',
                     'user:\"' + msg['user'] + '\"', 'error:\"null\"', 'time:\"' + str(msg['time']) + '\"', 'memory_init:\"' + str(msg['memory_init']) + '\"',
                     'cpu_init:\"' + str(msg['cpu_init']) + '\"', 'duration_init:\"' + str(msg['duration_init']) + '\"',
                     'duration_run:\"' + str(msg['duration_run']) + '\"', 'memory_run:\"' + str(msg['memory_run']) + '\"', 'cpu_run:\"' + str(msg['cpu_run']) + '\"',
                     'label:\"' + str(msg['label']) + '\"']
            propsQuery = ','.join(props)
            #print propsQuery
            query = 'create (n:Module{' + propsQuery + '})'
            graph.run(query)


            ''' relationships '''
            for uninqid in param_ids:
                # match (n:Object{id:uniqid}), (m:Module{id:id})
                # create (n)-[:IN]-> (m)

                query = ' match (n),(m) where n.id = \"' + uninqid + '\" and m.id = \"' + msg['id'] + '\" create (n)-[:IN]-> (m)'
                #print query
                graph.run(query)



        except Exception as e:

            param_ids = []

            for i in args:
                if isinstance(i, Object) or isinstance(i, File) or isinstance(i, Document):
                    param_ids.append(str(i.id))

                else:
                    param_ids.append(str(i))



            msg = {
                'p@': param_ids,
                'event': 'MOD-CRTN',
                'id': str(self.id),
                'name': str(self.__class__.__name__),
                'user': str(USER.id),
                'error': 'MIE',
                'memory_init': (psutil.virtual_memory()[3]),
                'cpu_init': (psutil.cpu_percent()),
                'duration_init': str(datetime.utcnow()-start_time),
                'time': str(datetime.utcnow()),
                'cpu_run': 0,
                'memory_run': 0,
                'duration_run': "00:00:00.000000",
                'label': 'module'
            }

            #print msg
            err.error(jsonify(msg))

            elasticmodule(msg['id'], msg['time'], msg['name'], msg['user'], msg['memory_run'], msg['memory_init'],
                          msg['cpu_run'], msg['cpu_init'], msg['duration_run'], msg['duration_init'], msg['error'])

            ''' GDB part '''
            props = ['NAME:\"' + msg['name'] + '\"', 'id:\"' + msg['id'] + '\"',
                     'user:\"' + msg['user'] + '\"', 'error:\"' + msg['error'] + '\"', 'time:\"' + str(msg['time']) + '\"',
                     'memory_init:\"' + str(msg['memory_init']) + '\"', 'cpu_init:\"' + str(msg['cpu_init']) + '\"',
                     'duration_init:\"' + str(msg['duration_init']) + '\"',
                     'cpu_run:\"' + str(msg['cpu_run']) + '\"', 'memory_run:\"' + str(msg['memory_run']) + '\"', 'duration_run:\"' + str(msg['duration_run']) + '\"',
                     'label:\"' + str(msg['label']) + '\"']
            propsQuery = ','.join(props)
            #print propsQuery
            query = 'create (n:Module{' + propsQuery + '})'
            graph.run(query)


    def run(self, when = True, false_return = None):

        start_time = datetime.utcnow()

        if when is True:

            try:
                self.logStart()
                self.outgoing = self.body()

                ret_ids = []

                if isinstance(self.outgoing, collections.Iterable):
                    for i in self.outgoing:
                        if isinstance(i, Object) or isinstance(i, File) or isinstance(i, Document):
                            ret_ids.append(str(i.id))

                else:
                    if isinstance(self.outgoing, Object) or isinstance(self.outgoing, File) or isinstance(self.outgoing,
                                                                                                          Document):
                        ret_ids.append(str(self.outgoing.id))



                msg = {
                    'o@': ret_ids,
                    'event': 'BODY-TRU',
                    'id': str(self.id),
                    'name': str(self.__class__.__name__),
                    'user': str(USER.id),
                    'duration_run': str(datetime.utcnow()-start_time),
                    'memory_run': (psutil.virtual_memory()[3]),
                    'cpu_run': (psutil.cpu_percent()),
                    'time_run': str(datetime.utcnow()),
                    'error': 'success'
                }

                deb.debug(jsonify(msg))

                elasticmodule(msg['id'], msg['time_run'], msg['name'], msg['user'], msg['memory_run'], 0,
                              msg['cpu_run'], 0, msg['duration_run'], "00:00:00.000000", msg['error'])

                ''' relationships '''
                for uninqid in ret_ids:
                    # match (n:Object{id:uniqid}), (m:Module{id:id})
                    # create (m)-[:OUT]-> (n)

                    query = ' match (n),(m) where n.id = \"' + uninqid + '\" and m.id = \"' + msg['id'] + '\" create (m)-[:OUT]-> (n) ' + 'set m.duration_run = \"' + str(msg['duration_run']) + '\"' + ', m.cpu_run = \"' + str(msg['cpu_run']) + '\"' + ', m.memory_run = \"' + str(msg['memory_run']) + '\"' + ', m.time_run = \"' + str(msg['time_run']) + '\"'
                    #print query
                    graph.run(query)

                self.logEnd()



                return self.outgoing


            except Exception as e:



                msg = {
                    'event': 'MOD-RUN',
                    'id': str(self.id),
                    'name': str(self.__class__.__name__),
                    'user': str(USER.id),
                    'error': 'MRE',
                    'duration_run': str(datetime.utcnow() - start_time),
                    'memory_run': (psutil.virtual_memory()[3]),
                    'cpu_run': (psutil.cpu_percent()),
                    'time_run': str(datetime.utcnow()),
                    'label': 'module'
                }

                err.error(jsonify(msg))

                elasticmodule(msg['id'], msg['time_run'], msg['name'], msg['user'], msg['memory_run'], 0,
                              msg['cpu_run'], 0, msg['duration_run'], "00:00:00.000000", msg['error'])

                ''' GDB part '''
                #props = ['NAME:\"' + msg['name'] + '\"', 'id:\"' + msg['id'] + '\"',
                #         'user:\"' + msg['user'] + '\"', 'error:\"' + msg['error'] + '\"', 'time:\"' + str(msg['time']) + '\"']
                #propsQuery = ','.join(props)
                # print propsQuery

                query = 'match (n:Module{id:\"' + msg['id'] + '\"}) set n.error = \"' + str(msg['error']) + '\"' + ', n.duration_run = \"' + str(msg['duration_run']) + '\"' + ', n.cpu_run = \"' + str(msg['cpu_run']) + '\"' + ', n.memory_run = \"' + str(msg['memory_run']) + '\"' + ', n.time_run = \"' + str(msg['time_run']) + '\"' + ', n.label = \"' + str(msg['label']) + '\"'
                #print query
                graph.run(query)



        else:
            '''not using this part for implementation'''

            ret_ids = []

            for i in false_return:
                ret_ids.append(str(i))



            msg = {
                'o@': ret_ids,
                'event': 'BODY-FLS',
                'id': str(self.id),
                'name': str(self.__class__.__name__),
                'user': str(USER.id),
                'duration': str(datetime.utcnow() - start_time),
                'memory': (psutil.virtual_memory()[3]),
                'cpu': (psutil.cpu_percent()),
                'time': str(datetime.utcnow()),
                'error': 'success'
            }


            deb.debug(jsonify(msg))


            return false_return


