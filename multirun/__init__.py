import multiprocessing as mp


def _generator_args(func, normal_args):
    for arg in normal_args:
        list_args = []
        kw_args = {}
        if isinstance(arg, list):
            list_args = arg
        elif isinstance(arg, dict):
            kw_args = arg
        else:
            list_args = [arg]
        yield {
            'func': func,
            'list_args': list_args,
            'kw_args': kw_args,
        }


def _run(arg_set):
    func = arg_set.get('func', lambda *args, **kwargs: None)
    list_args = arg_set.get('list_args', [])
    kw_args = arg_set.get('kw_args', {})
    return func(*list_args, **kw_args)


class Multirun(object):
    def __init__(self, worker_num=mp.cpu_count() - 1):
        self.worker_num = worker_num
        self.pool = mp.Pool(self.worker_num)

    def map(self, func, iter_args):
        iter_args = _generator_args(func, iter_args)

        try:
            res = self.pool.map(_run, iter_args)
        except Exception as e:
            self.pool.terminate()
            raise e
        return res
