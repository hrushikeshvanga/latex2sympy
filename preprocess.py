import re
from threading import Thread, Lock, Event
import latex2sympy2
import hashlib
from pylatexenc import latex2text

# Output mutex
output_lock = Lock()
hashes_lock = Lock()

# Final all written event
event = Event()

# Hashes
map = dict()
hashes = []
file = ""

def preprocess():
    global file, threads, event
    filename = input()
    ffile = open(filename, "r")
    file = ffile.read()

    ffile.close()
    double_pattern = re.compile(r"\$\$(.*?)\$\$", re.DOTALL)
    inline_pattern = re.compile(r"\$(.*?)\$", re.DOTALL)
    inline_pattern2 = re.compile(r"\\\((.*?)\\\)", re.DOTALL)

    displayed_pattern = re.compile(r"\\\[(.*?)\\\]", re.DOTALL)
    displayed_pattern2 = re.compile(r"\\begin\{equation\}(.*?)\\end\{equation\}", re.DOTALL)

    
    # Finding and replacing equations with hash
    while (w:=re.search(double_pattern, file)) \
        or (w:= re.search(inline_pattern, file)) \
        or (w:=re.search(inline_pattern2, file)) \
        or (w:=re.search(displayed_pattern, file)) \
        or (w:=re.search(displayed_pattern2, file)):
        start = w.start()
        end = w.end()
        nstart = start
        nend = end
        if (file[start] == "$"):
            nstart = start + 1
            nend = end - 1
            if (file[start+1] == "$"):
                nstart += 1
                nend -= 1
        if (file[start] == "\\" and file[start+1] == "["):
            nstart = start + 2
            nend = end - 2
        if (file[start] == "\\" and file[start+1] == "("):
            nstart = start + 2
            nend = end - 2


        equation = file[nstart:nend]
        equation = equation.replace("\\\\", "")
        equation = equation.replace("\n", "")
        equation = list(equation)
        equation = "".join(equation)
        hashed = get_hash(equation.encode('utf-8'))        
        map[hashed] = equation


        file = file[:start] + hashed + file[end:]

    # st = r"\frac{\partial^2f}{\partial x^2}"
    # print(latex2sympy2.latex2sympyStr(st))
    # return

    # Spawn workers
    spawn_workers()

    # write to output
    event.wait()
    output_file = open("output.tex", "w")
    output_file.write(file)
    output_file.close()
    


def get_hash(str):
    return hashlib.sha256(str).hexdigest()

def thread_writer():
    global hashes, hashes_lock, event
    global output_lock, file, map
    # Work for each thread

    done = False
    while not done:
        hashes_lock.acquire()

        if not hashes: # no hashes left
            # Release lock and exit
            hashes_lock.release()
            event.set()
            done = True
            continue

        output_lock.acquire()
        hash = hashes.pop()

        # Release hashes lock
        hashes_lock.release()

        # replace hash in output file
        equation = map[hash]

        english = convert_to_english(equation)

        file = file.replace(hash, english)
        print(f"replaced {hash} with {english}")
        # Release file lock
        output_lock.release()


def convert_to_english(eq):
    try:
        return latex2sympy2.latex2sympyStr("{}".format(eq))
    except Exception as e:
        print(e)
        print("eq Exception=", eq)
        # st = latex2text.latex2text('$'+eq+'$')
        return "**Error**"
    
        


def spawn_workers():
    global hashes, threads
    # Get all the hashes
    hashes = list(map.keys())

    # Spawning worker threads
    num_threads = 12

    for i in range(num_threads):
        t = Thread(target=thread_writer, args=[])
        t.start()
        t.join()


if __name__ == "__main__":
    preprocess()