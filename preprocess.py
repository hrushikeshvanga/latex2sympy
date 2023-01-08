import re
from threading import Thread, Lock
from TexSoup import TexSoup
import latex2sympy2
import hashlib

# Output mutex
output_lock = Lock()
hashes_lock = Lock()

# Hashes
map = dict()
hashes = []
file = ""

def main():
    global file
    # filename = input()
    ffile = open("exam.tex", "r")
    file = ffile.read()
    ffile.close()
    temp = "xxxxxxxx\[a+b\]xxxxxxx"
    inline_pattern = re.compile(r"\$(.*?)\$", re.DOTALL)
    inline_pattern2 = re.compile(r"\\\((.*?)\\\)", re.DOTALL)

    displayed_pattern = re.compile(r"\\\[(.*?)\\\]", re.DOTALL)
    displayed_pattern2 = re.compile(r"\\begin\{equation\}(.*?)\\end\{equation\}", re.DOTALL)

    
    # Finding and replacing equations with hash
    while (w:= re.search(inline_pattern, temp)) \
        or (w:=re.search(inline_pattern2, temp)) \
        or (w:=re.search(displayed_pattern, temp)) \
        or (w:=re.search(displayed_pattern2, temp)):
        start = w.start()
        end = w.end()

        if (file[start] == "$"):
            start = start + 1
        if (file[end] == "$"):
            end = end - 1
        

        equation = temp[start:end]
        hashed = get_hash(equation)
        map[hashed] = equation


        file = file[:start] + hashed + file[end:]

    # Spawn workers
    spawn_workers()

    # write to output
    final = get_final_text(file)

    output_file = open("output.text", "w")
    output_file.write(final)
    output_file.close()
    


def get_hash(str):
    return hashlib.sha256(str).hexdigest()

def thread_writer():
    global hashes, hashes_lock
    global output_lock, file
    # Work for each thread

    done = False
    while not done:
        hashes_lock.acquire()

        if not hashes: # no hashes left
            # Release lock and exit
            hashes_lock.release()
            done = True
            continue

        output_lock.acquire()
        hash = hashes.pop()

        # Release hashes lock
        hashes_lock.release()

        # replace hash in output file
        equation = map[hash]

        english = convert_to_english(equation)

        file.replace(hash, english)

        # Release file lock
        output_lock.release()


def convert_to_english(eq):
    pass


def spawn_workers():
    global hashes
    # Get all the hashes
    hashes = map.keys()

    # Spawning worker threads
    num_threads = 12

    for i in range(num_threads):
        t = Thread(thread_writer, args = [])
        t.run()
        t.join()



def get_final_text(latex):
    pass


if __name__ == "__main__":
    main()