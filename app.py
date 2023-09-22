from flask import Flask, request
import time
import threading
import multiprocessing

app = Flask(__name__)


def cpu_bound_task(iterations):
    result = 0
    for _ in range(1, iterations + 1):
        result += 1
    return result


# def cpu_bound_task1(iterations):
#     result = 0
#     time.sleep(5)
#     for _ in range(1, iterations + 1):
#         result += 1
#     print("process1")
#     return result


@app.route("/single-thread", methods=["GET"])
def single_thread():
    start_time = time.time()

    result = cpu_bound_task(5000000)

    end_time = time.time()

    return f"Single thread, Time taken: {end_time - start_time} seconds"


@app.route("/multi-thread", methods=["GET"])
def threading_route():
    start_time = time.time()

    thread1 = threading.Thread(target=cpu_bound_task, args=(2500000,))
    thread2 = threading.Thread(target=cpu_bound_task, args=(2500000,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    end_time = time.time()

    return f"multi Thread, Time taken: {end_time - start_time} seconds"


@app.route("/multiprocessing", methods=["GET"])
def multiprocessing_route():
    start_time = time.time()

    process1 = multiprocessing.Process(target=cpu_bound_task, args=(2500000,))
    process2 = multiprocessing.Process(target=cpu_bound_task, args=(2500000,))

    process1.start()

    process2.start()
    
    process1.join()

    process2.join()

    end_time = time.time()

    return f"Multiprocessing, Time taken: {end_time - start_time} seconds"


if __name__ == "__main__":
    app.run(debug=True)
