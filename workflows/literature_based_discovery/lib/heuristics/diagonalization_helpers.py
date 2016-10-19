'''
Created on 10. okt. 2012

@author: matic
'''


def write_to_init_file(trains_class,trains_text,sorted_words,out_file_name="init.dat",binary=True):
    out_file = open(out_file_name, "wb")
    for train in trains_class.keys():
        set_of_words=set(trains_text[train])
        #train_nums=[]
        for word in sorted_words:
            if binary:
                num = 1 if word in set_of_words else 0
            #else:
                #if tf_idfs[train].get(word, 0.0)!=0:
                #    tfnnull+=1
                #num=1 if tf_idfs[train].get(word, 0.0)/max_tfidf >0.3 else "?"
                #train_nums.append(str(num))
            out_file.write( str(num) + " ")
        out_file.write("\n")
    out_file.close()

def write_to_init_file_inv(trains_class,trains_text,sorted_words,out_file_name="init_inv.dat",binary=True):
    out_file = open(out_file_name, "wb")
    for word in sorted_words:
        for train in trains_class.keys():
            if binary:
                num = 1 if word in trains_text[train] else 0

            out_file.write( str(num) + " ")
        out_file.write("\n")
    out_file.close()

import os
def identity_permutation(n):
    d={}

    for i in range(n):
        d[i]=i
    return d

def get_permutations(prefix,filename="init.dat"):
        #-----------------CREATE BANDED BINARY MATRIX-----------------
    print "creating banded binary matrix aaa"
    old_path=os.getcwd()
    os.chdir(prefix)
    #print os.getcwd(),('C:\Users\matic\workspace\diagonalization/' if os.getenv('COMPUTERNAME')=="PORFAVOR-PC" else "./")+"diag 1 34 1 11 < "+filename
    os.system(('C:\Users\matic\workspace\diagonalization/' if os.getenv('COMPUTERNAME')=="PORFAVOR-PC" else "./")+"diag 1 34 1 11 < "+filename)
    os.chdir(old_path)

    col_perm_rev={} #permutation of columns      #{0: 151 } na nictem mestu je 151. beseda
    row_perm_rev={} #permutation of rows


    #COLUMN ORDERING
    column_ordering_file=open(prefix+"min_flips_output_1_column_ordering.dat", 'r')
    line = column_ordering_file.readline()

    for i,new_col in enumerate(line.split(" ")):
        if new_col!="":
            col_perm_rev[i]=int(new_col)

    print "col_perm:",col_perm_rev
    column_ordering_file.close()

    #ROW ORDERING
    row_ordering_file=open(prefix+"min_flips_output_5_row_ordering.dat", 'r')
    line = row_ordering_file.readline()    # Invokes readline() method on file


    i=0
    while line:
        if line!="\n":
            spl=line.split("\n")
            row_perm_rev[i]=int(spl[0])
            #print i,spl[0]
            i+=1
        line = row_ordering_file.readline()
    print "row_perm:",row_perm_rev
    row_ordering_file.close()

    return col_perm_rev,row_perm_rev

from PIL import Image, ImageDraw
def draw_matrix(sorted_words,jursic_word_score,max_word_score,col_perm_rev,row_perm_rev,trains_class,name,filename,b_terms,col_perm_inv,classes):
    red = (255,0,0)
    blue = (0,0,255)
    white = (255,255,255)

    im = Image.new("RGB", [len(col_perm_rev),len(row_perm_rev)], white)#Image.open("after_col_perm.pgm")
    draw = ImageDraw.Draw(im)

    #DRAW YELLOW LINES: CROSSBEE SCORES
    if jursic_word_score:
        for j,old_j in col_perm_rev.items():#enumerate(sorted_words):
            word=sorted_words[old_j]
            w=jursic_word_score[word]/max_word_score
            #print w,255-int(255*w)
            #if not col_perm_inv or col_perm_inv.has_key(j):
            new_j=col_perm_inv[j] if col_perm_inv else j

            draw.line(((new_j,0),(new_j,len(row_perm_rev))), fill=(255,255,255-int(255*(w))))

        #draw.point((1,5), fill=blue)
    #print col_perm_inv and sorted(col_perm_inv.keys())



    #DRAW POINTS
    file=open(filename+".dat", 'r')
    line = file.readline()

    i=0
    while line:
        orig_i=row_perm_rev[i]

        draw.line(((0,i),(len(col_perm_rev),i)), fill=(255,200,200) if trains_class[orig_i]==classes[0] else (200,200,255))

        for j,value in enumerate(line.split(" ")):
            if value=="1":
                new_j=col_perm_inv[j] if col_perm_inv else j
                draw.point((new_j,i), fill=(red if trains_class[orig_i]==classes[0] else blue))
        line = file.readline()
        i+=1
    file.close()

    #DRAW GREEN LINES: B-TERMS
    for j,old_j in col_perm_rev.items():#enumerate(sorted_words):
        word=sorted_words[old_j]
        new_j=col_perm_inv[j] if col_perm_inv else j


        if word in b_terms:
            draw.line(((new_j,0),(new_j,len(row_perm_rev))), fill=(100,255,100))

    im.save(name+".png")
    #im.show()

import string
def generate_js_file(sorted_words,jursic_word_score,max_word_score,col_perm_rev,row_perm_rev,trains_class,trains_text,prefix,b_terms,greens_per_word,blues_per_word,classes,col_perm_rev_inv=False,col_perm_inv=False,domain_outliers=[]):

    outfile=open(prefix+"redpin/points.js","wb")
    outfile_py=open(prefix+"redpin/points.txt","wb")
    #var width = $('#redpin').redPin('width'); var height = $('#redpin').redPin('height');
    outfile.write("$(function(){  $('#status').css('margin-top','"+str(len(row_perm_rev)*6+22)+"px');$('#redpin').height("+str(len(row_perm_rev)*6+12)+"); $('#redpin').width("+str(len(col_perm_rev)*6+12)+"); $('#redpin').redPin({concept_count: 1});" )

    #DRAW YELLOW LINES: CROSSBEE SCORES
    if jursic_word_score:
        for j,old_j in col_perm_rev.items():#enumerate(sorted_words):
            word=sorted_words[old_j]
            w=jursic_word_score[word]/max_word_score*1.

            new_j=col_perm_rev_inv[j] if col_perm_rev_inv else j

            outfile.write("$('#redpin').redPin('plotRect',"+str(3+new_j*6)+","+str(255-int(255*(w)))+");")
            outfile_py.write("CS\t"+str(3+new_j*6)+"\t"+str(255-int(255*(w)))+"\n")


    #DRAW YELLOW LINES: B-TERMS
    for j,old_j in col_perm_rev.items():#enumerate(sorted_words):
        word=sorted_words[old_j]
        #new_j=col_perm_rev[old_j]
        w=1. if word in b_terms else 0.
        new_j=col_perm_inv[j] if col_perm_inv else j

        if word in b_terms:
            outfile.write("$('#redpin').redPin('plotRect',"+str(3+new_j*6)+","+str(255-int(255*(w)))+");") #TODO different color
            outfile_py.write("BT\t"+str(3+new_j*6)+"\t"+str(255-int(255*(w)))+"\n")

    for doc_outlier in domain_outliers:#enumerate(sorted_words):
#        word=sorted_words[old_j]
#        #new_j=col_perm_rev[old_j]
#        w=1. if word in b_terms else 0.
#        new_j=col_perm_inv[j] if col_perm_inv else j

        outfile.write("$('#redpin').redPin('plotRectHoriz',"+str(3+doc_outlier*6)+","+str(255-int(255*(w)))+");") #TODO different color
        outfile_py.write("DOCOUT\t"+str(3+doc_outlier*6)+"\n")


    file=open(prefix+"min_flips_output_7_original_banded_matrix.dat", 'r')
    line = file.readline()

    #DRAW POINTS
    i=0
    while line:
        orig_i=row_perm_rev[i]
        for j,bin_value in enumerate(line.split(" ")):
            word=sorted_words[col_perm_rev[j]]
            new_j=col_perm_inv[j] if col_perm_inv else j

            if bin_value=="1":
                outfile.write("\n\t$('#redpin').redPin('addDot',"+str(6+new_j*6)+","+str(6+i*6)+",'"+word+str(greens_per_word.get(word))+' '+str(blues_per_word.get(word))+"','"+trains_class[orig_i]+" "+string.join(trains_text[orig_i]," ")+"',"+("1" if trains_class[orig_i]==classes[0] else "0")+");")
                outfile_py.write("P\t"+str(6+new_j*6)+"\t"+str(6+i*6)+"\t"+word+"\t"+str(greens_per_word.get(word))+"\t"+str(blues_per_word.get(word))+"\t"+trains_class[orig_i]+"\t"+string.join(trains_text[orig_i]," ")+"\t"+("1" if trains_class[orig_i]==classes[0] else "0")+"\n")

        line = file.readline()
        i+=1
    file.close()

    outfile.write("$('#redpin').redPin('setStatus',$('#status')); });")
    outfile.close()

