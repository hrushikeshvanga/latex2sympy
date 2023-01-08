from threading import Thread, Lock

lock = Lock()

lock.acquire()
lock.release()