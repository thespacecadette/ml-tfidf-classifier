#! /usr/bin/env python                                                                  
import sys                                                                              
import re                                                                               
class CountMapReduce():                                                                 
    def __init__(self):                                                                 
        self.current_item = None                                                        
        self.count_sum = 0                                                              
    def __output(self):                                                                 
        if self.current_item:                                                           
            print(self.current_item,'\t,', self.count_sum)                              
    def map(self, line):                                                                
        WORD_RE = re.compile(r"[\w']+")                                                 
        res = dict()                                                                    
        for word in WORD_RE.findall(line) :                                             
            if len(word) > 0:                                                           
                if word.lower() in res.keys():                                          
                    res[word.lower()] += 1                                              
                else:                                                                   
                    res[word.lower()] = 1                                               
        for key in res.keys():                                                          
            print("\t".join([key,str(res[key])]))                                       
    def reduce(self, item, count):                                                      
        if self.current_item != item:                                                   
            self.__output()                                                             
            self.current_item = item                                                    
            self.count_sum = 0                                                          
        self.count_sum += int(count)                                                    
    def reduce_end(self):                                                               
        #Print the last item count sum.                                                 
        self.__output()             
                                                    
if __name__ == '__main__':                                                              
    mr_flag = sys.argv[1]                                                               
    mapreduce = CountMapReduce()                                                        
    if mr_flag == 'map':                                                                
        for line in sys.stdin:                                                          
            line = line.strip()                                                         
            mapreduce.map(line)                                                         
    elif mr_flag == 'reduce':                                                           
        for line in sys.stdin:                                                          
            line = line.strip()                                                         
            item, count = line.split('\t', 1)                                           
            mapreduce.reduce(item, count)                                               
    mapreduce.reduce_end()                                                              
