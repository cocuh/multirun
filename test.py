import multirun as mr
import time

def worker( id, sec, msg): # multiple args
    print('start {}: {}'.format(id, msg))
    time.sleep(sec)
    print('end   {}: {}'.format(id, msg))
    return msg

def arg_gen():
    for i in range(30):
        yield {
            'id': i,
            'sec': i,
            'msg': 'youjo No.{}'.format(i),
        }

p = mr.Multirun()
res = p.map(worker, arg_gen())
print(res)