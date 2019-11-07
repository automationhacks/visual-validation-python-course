import time

POLL_FREQUENCY = 0.5
WAIT_TIME = 1


def until(method, args=None, timeout=30, message=''):
    time_to_wait = WAIT_TIME

    end_time = time.time() + timeout
    while True:
        try:
            value = method(args)
            if value:
                return value
        except Exception as exc:
            print(exc)

        time_to_wait *= POLL_FREQUENCY

        time.sleep(time_to_wait)
        if time.time() > end_time:
            break
    raise NameError(message)
