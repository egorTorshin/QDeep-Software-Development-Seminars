from multiprocessing import Process
import time, os


def worker(name):
    print(f"Start {name}, pid={os.getpid()}")
    time.sleep(1)
    print(f"End   {name}, pid={os.getpid()}")


if __name__ == "__main__":
    p1 = Process(target=worker, args=("A",))
    p2 = Process(target=worker, args=("B",))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Done")
