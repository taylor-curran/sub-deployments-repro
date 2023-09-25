from prefect import flow, task
from prefect_aws.s3 import S3Bucket
import time
from tasks_subflows_models.flow_params import SimulatedFailure
from prefect_dask.task_runners import DaskTaskRunner
from prefect import flow, get_run_logger

@task
def task_l():
    logger = get_run_logger()
    logger.info("Log from task l")
    print("task f")
    return {"l": "task l"}

@task
def task_o():
    logger = get_run_logger()
    logger.info("Log from task o")
    print("task o")
    return {"o": "task o"}

@flow()
def child_flow_d(sleep_time=0):
    logger = get_run_logger()
    logger.info("Log from child flow d")
    l = task_l.submit()
    time.sleep(sleep_time+3)
    o = task_o.submit()
    return {"d": "child flow d"}

@task()
def upstream_task_h():
    logger = get_run_logger()
    logger.info("Log from upstream task h")
    print("upstream task")
    return {"h": "upstream task"}


@task()
def upstream_task_i():
    logger = get_run_logger()
    logger.info("Log from upstream task i")
    print("upstream task")
    return {"i": "upstream task"}


@task()
def downstream_task_p(h):
    logger = get_run_logger()
    logger.info("Log from downstream task p")
    print(h)
    return {"p": "downstream task"}

@flow
def dask_logging_test():
    logger = get_run_logger()
    logger.info("Log from parent flow")
    h = upstream_task_h.submit()
    i = upstream_task_i()
    d = child_flow_d()
    p = downstream_task_p.submit(h)




if __name__ == '__main__':
    dask_logging_test()