import gzip
import shutil
import io
import zlib
import base64

infile = "C:/Users/Bananus/Downloads/flag.gz"
outfile = "C:/Users/Bananus/Downloads/flagout.txt.gz"

# f = open(infile, "r")

# data = f.read()

# compressed_data = base64.b64decode(data.encode())
# output = zlib.decompress(compressed_data).decode()
# print(output)
# f.close()

## GZIP

with gzip.decompress(infile) as f_in:
    with open(outfile, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)