from py2neo import Graph
graph  = Graph(password = 'password')
import sys
import time

def parse(query, filename):
    data = graph.run(query)

    with open(filename, 'w') as f:
        header = data.keys()

        f.write('\t'.join(header) + '\n')


        for d in data:
            line = []
            for k in header:
                line.append(str(d[k]))

            f.write('\t'.join(line) + '\n')

# frequency
query_freq = 'match(n) return n.label as label, count(n) as freq'
# frequency of different modules
query_module_freq = 'match (n:Module) return n.NAME as tool, count(n) as count'
# fastqc only frequency
query_single_mod_freq = 'match(n:Module) where n.NAME = "FastQC" return n.NAME as name, count(n) as freq'
# time series of single modules' single property
query_time_single_mod_single_prop = 'match(n:Module) where n.NAME="FastQC" and n.cpu_run >= "0" return n.time as time, n.cpu_run as cpuload order by n.time'
# time series of multi-module single property
query_time_multi_mod_single_prop = 'match(n:Module) where n.cpu_run >= "0"  return n.time as time, n.NAME as tool, n.cpu_run as cpuload order by n.time'
# time series of module names, error and cross props
query_cross_prop = 'match(n:Module) where n.cpu_run >= "0" and n.duration_run >= "0"  return n.time as time, n.NAME as name, n.error as error, n.cpu_run as cpu, n.duration_run as duration order by n.time'
query_cross_prop_log = 'match(n:Module) where n.cpu_run >= "0" and n.duration_run >= "0"  return n.time as time, n.NAME as name, n.error as error,toFloat (n.cpu_run) as cpu, log(toFloat(n.duration_run)) as duration order by n.time'
# query module name vs error count group chart
query_error_count = 'match(n:Module) return n.NAME as name,  n.error as error, count(n) as freq'
# query module name vs error count group chart
query_error_cpu = 'match(n:Module) return n.NAME as name,  n.error as error, n.cpu_run as cpu'

while(True):
    time.sleep(1.5)
    print time.time()

    ''' parsing '''
    parse(query_freq, 'data/frequency.tsv')

    parse(query_module_freq, 'data/mod_freq.tsv')

    parse(query_single_mod_freq, 'data/single_freq.tsv')

    parse(query_time_single_mod_single_prop, 'data/single_mod_single_prop.tsv')

    parse(query_time_multi_mod_single_prop, 'data/multi_mod_single_prop.tsv')

    parse(query_cross_prop, 'data/mod_name_error.tsv')

    parse(query_cross_prop, 'data/cross.tsv')

    parse(query_error_count, 'data/error_group.tsv')

    parse(query_error_cpu, 'data/error_group_cpu.tsv')

    parse(query_cross_prop_log, 'data/cpu_vs_log_duration.tsv')