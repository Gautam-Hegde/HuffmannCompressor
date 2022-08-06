from fileinput import filename
import os
import heapq
class HuffmanCoding:
    def __init__(self,path):
        self.path = path
        self.heap= []
        self.codes={}
    class HeapNode:
        def __init__(self,char,freq):
            self.char=char
            self.freq=freq
            self.left=None
            self.right=None
        def __lt__(self,other):
            return self.freq<other.freq
        def __eq__(self,other):
            #checks
            if(other==None):
                return False
            if(not isinstance(other,HeapNode)):
                return False
            return self.freq==other.freq


    def make_frequency_dict(text):
        frequency={}
        for character in text:
            if not character in frequency:
                frequency[character]=0
            else:
                frequency[character]+=1
        return frequency
        #we need to make a frequency dictionary

    def make_heap(self,frequency):
        #we need to make a heap
        for key in frequency:
            node= self.HeapNode(key,frequency[key])
            heapq.heappush(self.heap,node)

          


    def merge_codes(self):
        #build the huffman tree and save root node in heap
        while(len(self.heap)>1):
            node1=heapq.heappop(self.heap)
            node2=heapq.heappop(self.heap)

            merged=self.HeapNode(None,node1.freq+node2.freq)
            merged.left=node1
            merged.right=node2
            heapq.heappush(self.heap,merged)


    def make_codes(self):
        #make the codes for each character in the text


    def get_encoded_text(self,text):
        pass
        #replace character with code and return it

    def pad_encoded_text(self, encoded_text):
        pass
        #add padding so that the encoded text is a multiple of 8
        #return the padded encoded text
    def get_byte_array(self,padded_encoded_text):
        pass
        #convert the padded encoded text into a byte array
        #return the byte array

    def compress(self):
        filename, file_extension = os.path.splitext(self.path)
        output_path = filename + ".bin"
        with open(self.path,'r') as file, open(output_path,'wb') as output:
            text = file.read()
            text = text.rstrip() #removing extra white spaces

            frequency = make_frequency_dict(text)

            self.make_heap(frequency)
            self.merge_codes()
            self.make_codes()


           encoded_text = get_encoded_text(text)
           padded_encoded_text= pad_encoded_text(encoded_text)

            b= self.get_byte_array(padded_encoded_text)
            output.write(bytes(b))
        print("Compressed")
        return output_path    

