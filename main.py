import os
import shutil

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
os.makedirs(out_dir, exist_ok=True)
src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
shutil.copyfile(src, os.path.join(out_dir, "entry.txt"))
