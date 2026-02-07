import sys

if len(sys.argv) != 3:
    print("Usage: python route_bin_ext.py <input_file> <output_file>")
    sys.exit(1)

inf = open(sys.argv[1], "rb")
of = open(sys.argv[2], "wb")

NAND_PAGE_BLK = 64
NAND_PAGE_SIZE = 2048
BLK_SIZE = NAND_PAGE_BLK * NAND_PAGE_SIZE

def page2off(pgno):
    return pgno * 0x840

def read_page(inf, blkno, pgno):
    blklen = BLK_SIZE
    fileoff = blklen * blkno + page2off(pgno)

    print("reading block %d page %d: offset %08x" % (blkno, pgno, fileoff))

    inf.seek(fileoff, 0)
    block = inf.read(blklen)
    buf = bytearray()

    for i in range(NAND_PAGE_SIZE):
        buf.append(block[i])

    return buf

for blkn in range(1024):
    for pagen in range(64):
        res = read_page(inf, blkn, pagen)
        of.write(res)

inf.close()
of.close()
