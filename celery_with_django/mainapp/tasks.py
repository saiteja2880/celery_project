from celery import shared_task


@shared_task(bind=True)
def test_func(self):
    for i in range(10):
        print(i)
    return "done"


@shared_task
def print_hello():
    return "Hii Everyone !"

@shared_task
def hii():
    return "hii !"