## GFF3 coordinate system: 1-based, inclusive for both start (col 4) and end (col 5).
## Joining segments therefore only requires adding the cumulative length of all
import argparse
import os

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--gff', type = str, required = True, nargs='+', help = "per-segment gff files")
    parser.add_argument('--segment-order', type = str, required = True, nargs='+', help = "segment names (gff file names without extension) in concatenation order")
    parser.add_argument('--output', type = str, required = True, help = "output whole genome gff")
    args = parser.parse_args()

# args.gff = ['config/h3n2/pb2/genemap.gff', 'config/h3n2/ha/genemap.gff', 'config/h3n2/na/genemap.gff']
# args.segment_order = ['pb2', 'ha', 'na']
# args.output = 'builds/flu_seasonal_washington_h3n2_3y/concat_annotation.gff'

    files = dict(zip(args.segment_order, args.gff))

    offset = 0
    lines = []
    for segment in args.segment_order:
        length = 0
        for line in open(files[segment]):
            if line.startswith('##sequence-region'):
                length = int(line.split()[3])
            elif not line.startswith('#') and line.strip():
                newline = line.rstrip('\n').split('\t')
                newline[3], newline[4] = str(int(newline[3]) + offset), str(int(newline[4]) + offset)
                lines.append('\t'.join(newline))
        offset += length

    with open(args.output, 'w') as out:
        out.write(f"##gff-version 3\n##sequence-region reference 1 {offset}\n")
        out.write('\n'.join(lines) + '\n')