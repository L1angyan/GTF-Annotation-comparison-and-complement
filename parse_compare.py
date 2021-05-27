import sys

def extract_id(string):
    l = string.split(";")[:-1]
    #delete the ";" of the end of string
    d = {}
    for i in l:
        il = i.split()
        d[il[0]] = il[1]
    return d

ipf = sys.argv[1]
ipo = open(ipf,"r")
#cor_dict = {}
id_list = []

for line in ipo.readlines():
    line = line.strip()
    linelist = line.split("\t")
    if linelist[2] != "transcript":continue
    correspond = linelist[-1]
    trans_id,mode,gene_id = extract_id(correspond)["transcript_id"],extract_id(correspond)["class_code"],extract_id(correspond)["gene_id"]
    trans_id = trans_id[1:-1]
    gene_id = gene_id[1:-1]
    if mode!='"="':
        id_list.append(gene_id+"\t"+trans_id)
        #print(gene_id+"\t"+trans_id)
        
        #print(trans_id[1:-1]+"\t"+mode[1:-1])

#for i in id_list:print(i)
#print("ribo"+"\t"+"ref")
#for i,j in cor_dict.items():
#    print(i+"\t"+j)
ipo.close()

for line in open("../rice_merge_update.gtf",'r').readlines():
    line  = line.strip()
    if line[0]=="#":continue
    if line.split("\t")[2] == "gene":continue
    #print(extract_id(line.split("\t")[-1]))
    trans_id,gene_id = (extract_id(line.split("\t")[-1]))["transcript_id"],(extract_id(line.split("\t")[-1]))["gene_id"]
    trans_id = trans_id[1:-1]
    gene_id = gene_id[1:-1]
    #trans_id = trans_id[1:-1]
    if gene_id+"\t"+trans_id in id_list:
        print(line)
        #print("yes")
    #else:
        #print(gene_id+"\t"+trans_id)
