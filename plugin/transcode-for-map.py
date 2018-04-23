import sys
import re
import pdb
import os 
 

 

    #key,value,order,name
    #map<key,value> name=order;
    
def transcode(filename,path):
    tmpl='''
    message map_item_%(name)s
    {
        optional %(key)s key=1;
        optional %(value)s value=2;
    }
    repeated map_item_%(name)s %(name)s=%(order)s;
    '''
    f=open(path+'/'+filename)
    #
    if f:
        content=f.read()
        f.close()
        if content:
    
            pat=re.compile(r'map<\s*(\w+)\s*,(\w+)\s*>\s+(\w+)\s*=\s*(\d+)\s*;')
            xxx=re.search(pat,content)
            
            
            while xxx:

                target=xxx.group(0)
                d={}
                d['key']=xxx.group(1)
                d['value']=xxx.group(2)
                d['name']=xxx.group(3)
                d['order']=xxx.group(4)
                
                print target
                data=tmpl%d;
                content=content.replace(target,data)
                xxx=re.search(pat,content)
                print content
            f=open('./tmp/'+filename,'w')
            f.write(content)
            f.close()

def main():
    targetPath=sys.argv[1]
    
    for dirpath,dirnames,filenames in os.walk(targetPath):
        for filename in filenames:
            if filename.endswith(".proto"):
                transcode(filename,targetPath)


if __name__ == "__main__":
    main()
