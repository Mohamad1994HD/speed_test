from threading import Thread, Event
from datetime import datetime
from subprocess import Popen, PIPE


class CONFIG:
    FILE_PATH = ''
    REQUEST_DELAY = 60


class MyThread(Thread):
    def __init__(self, event, repeat_every, function):
        Thread.__init__(self)
        self.stopped = event
        self.function = function
        self.rep_every = repeat_every

    def run(self):
        while not self.stopped.wait(self.rep_every):
            # call a function
            self.function()

    def stop(self):
        self.stopped.set()


def to_save(f):
    def log_data_to_file(data):
        with open(CONFIG.FILE_PATH, 'a') as txt_file:
            txt_file.write(data)

    def decorator():
        info = f()
        return log_data_to_file(data=info)

    return decorator


@to_save
def measure_connection():
    print 'starting test'
    date = str(datetime.utcnow())
    p = Popen("speedtest-cli", stdout=PIPE)
    output_sp = str(p.communicate()[0])
    # p = Popen(["speedtest-cli", "--bytes"], stdout=PIPE)
    # output_b = str(p.communicate()[0])

    return "Date:\n\n%s\n\nSpeed test:\n\n%s\n\n\n" % (date, output_sp)


def start_tests():
    MyThread(event=Event(),
             function=measure_connection,
             repeat_every=CONFIG.REQUEST_DELAY,
             ).start()


if __name__ == '__main__':
    th = MyThread(event=Event(),
                  function=measure_connection,
                  repeat_every=CONFIG.REQUEST_DELAY,
                  )
    th.run()
