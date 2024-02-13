orig = open("/Users/yuyu/Desktop/2-data-munging-anyuchenn/data/GLB.Ts+dSST.txt", 'r')
clean = open("/Users/yuyu/Desktop/2-data-munging-anyuchenn/data/clean_data.csv", 'w')

def fix_nums(ns):
    fixed_ns = []
    for n in ns:
        try:
            n_float = float(n)  
            if n_float < 1879:
                res = round((n_float / 100) * 1.8, 1)  
                fixed_ns.append(str(res))  
            else:
                fixed_ns.append(n)  
        except ValueError:
            fixed_ns.append(n)  
    return fixed_ns



for _ in range(7):
    orig.readline()

hdr = orig.readline().strip()
hdr_cols = ','.join(hdr.split())
clean.write(hdr_cols + "\n")

lines = orig.readlines()
lines = lines[:-7]

for idx, line in enumerate(lines):
    if line.strip():
        parts = line.split()
        parts_fixed = fix_nums(parts)
        line_new = ','.join(parts_fixed)
        if line_new != hdr_cols:
            clean.write(line_new)
            if idx < len(lines) - 1:
                clean.write("\n")

orig.close()
clean.close()