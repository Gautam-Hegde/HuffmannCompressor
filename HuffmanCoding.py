from fileinput import filename
import os

class HuffmanCoding:
    def __init__(self,path):
        self.path = path
        self.heap= []
        self.codes={}

    def make_frequency_dict(text):
        pass
        #we need to make a frequency dictionary

    def make_heap(self,frequency):
        #we need to make a heap
        pass    


    def merge_codes(self):
        #build the huffman tree and save root node in heap


    def make_codes(self):
        #make the codes for each character in the text


    def get_encoded_text(self,text):
        pass
        #replace character with code and return it

    def pad_encoded_text(self, encoded_text):
        pass
        #add padding so that the encoded text is a multiple of 8
        #return the padded encoded text

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



