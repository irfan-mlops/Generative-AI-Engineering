"""
05_multithreading.py

Topic:
Introduction to Multithreading.

Threading is useful when we have tasks that spend time waiting,
such as downloading files, API requests, or reading data.
"""

import threading
import time


# ------------------------------------------------------------
# FUNCTION THAT WILL RUN IN A THREAD
# ------------------------------------------------------------

def task(name):
    """Simulate a slow task."""

    print(f"{name} started.")

    # Simulate waiting for an operation.
    time.sleep(3)

    print(f"{name} finished.")


# ------------------------------------------------------------
# CREATE THREADS
# ------------------------------------------------------------

thread1 = threading.Thread(
    target=task,
    args=("Task 1",)
)

thread2 = threading.Thread(
    target=task,
    args=("Task 2",)
)


# ------------------------------------------------------------
# START THREADS
# ------------------------------------------------------------

start = time.time()

thread1.start()
thread2.start()


# ------------------------------------------------------------
# WAIT FOR THREADS
# ------------------------------------------------------------

"""
join() makes the main program wait until
the thread has completed.
"""

thread1.join()
thread2.join()


# ------------------------------------------------------------
# CHECK TOTAL TIME
# ------------------------------------------------------------

end = time.time()

print(
    "Total time:",
    round(end - start, 2),
    "seconds"
)