import numpy as np

def load_file(filepath):
    with open(filepath, 'r') as file:
        content = file.read().strip()
    
    return content

class Function:
    def __init__(self,S):
        lines = S.split('\n')[1:]
        self.tuples: list[tuple[int,int,int]] = [[int(x) for x in line.split()] for line in lines]
    
    def apply_range(self, R):
        A = []
        for (dest, src, sz) in self.tuples:
            src_end = src+sz
            NR = []
            while R:
                (st, ed) = R.pop()
                before = (st, min(ed,src))
                inter = (max(st,src), min(src_end, ed))
                after = (max(src_end, st), ed)
                if before[1] > before[0]:
                    NR.append(before)
                if inter[1] > inter[0]:
                    A.append((inter[0]-src+dest, inter[1]-src+dest))
                if after[1] > after[0]:
                    NR.append(after)
            R = NR
        return A+R

def main():
    content = load_file('data.txt')
    parts = content.split('\n\n')
    seed, *others = parts
    seed = [int(x) for x in seed.split(':')[1].split()]
    Fs = [Function(s) for s in others]

    P2 = []
    pairs = list(zip(seed[::2] , seed[1::2]))
    for st,sz in pairs:
        R = [(st, st+sz)]
        for f in Fs:
            R = f.apply_range(R)
        P2.append(min(R)[0])
    print(min(P2))
 
if __name__ == '__main__':
    main()