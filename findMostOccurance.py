#Program count each words in a document provided and return max occurance words

def Count_mostOccurenceWord():
    name = input("Enter file name : ")
    handle = open(name , 'r')   # read file mode
    counts = dict()  #initialize couint with empty dictionary hold two parameter(key, value)
    for line in handle:    #line is a subset of handle file
        words = line.split()  # biult in split function to count the number of words in a line
        for word in words:    #count each word for the total words sumed from all lines
            counts[word] = counts.get(word, 0) + 1  # get funciton if words is the same increment the count by one
        bigCount = None   #initialize the accumulated count as none or zero
        bigWord = None    #initianlize  the accumulated each words by none or zero
        for word, count in list(counts.items()):  # provide the two argument status(words, count) how many times the words
                #appear each words and sum up each word appearance
            if bigCount is None or count > bigCount:   #looking for the maximum occurance of the word
                bigWord = word    #assign maximum appearance of word  to bigword
                bigCount = count   #likewise max appearance count value to bigCount
    print( bigWord, bigCount)

if __name__ == '__main__':
    Count_mostOccurenceWord()

'''The output the below articles is
Enter file name : C:\----\me\Documents\TheEarth.txt\
    the   56    # The word "the" appears 56 times in the articles which is the highest frequence in the article.'''





"File name " \
"How The Earth was formed or History of Eearth" \
'''From Wikipedia, the free encyclopedia
This article is about scientific evidence concerning the history of Earth. For the history of humans,
 see History of the world.
 
The history of Earth concerns the development of planet Earth from its formation to the present day.[1][2] 
Nearly all branches of natural science have contributed to understanding of the main events of Earth's past,
 characterized by constant geological change and biological evolution.
The geological time scale (GTS), as defined by international convention,[3] depicts the large spans of time 
from the beginning of the Earth to the present, and its divisions chronicle some definitive events of Earth history.
 (In the graphic: Ga means "billion years ago"; Ma, "million years ago".) Earth formed around 4.54 billion years ago,
  approximately one-third the age of the universe, by accretion from the solar nebula.[4][5][6] Volcanic outgassing 
  probably created the primordial atmosphere and then the ocean, but the early atmosphere contained almost no oxygen.
   Much of the Earth was molten because of frequent collisions with other bodies which led to extreme volcanism. 
   While the Earth was in its earliest stage (Early Earth), a giant impact collision with a planet-sized body named 
   Theia is thought to have formed the Moon. Over time, the Earth cooled, causing the formation of a solid crust, 
   and allowing liquid water on the surface.
The Hadean eon represents the time before a reliable (fossil) record of life; it began with the formation of the planet 
and ended 4.0 billion years ago. The following Archean and Proterozoic eons produced the beginnings of life on Earth 
and its earliest evolution. The succeeding eon is the Phanerozoic, divided into three eras: the Palaeozoic, an era of 
arthropods, fishes, and the first life on land; the Mesozoic, which spanned the rise, reign, and climactic extinction of 
the non-avian dinosaurs; and the Cenozoic, which saw the rise of mammals. Recognizable humans emerged at most 2 million 
years ago, a vanishingly small period on the geological scale.
The earliest undisputed evidence of life on Earth dates at least from 3.5 billion years ago,[7][8][9]during the Eoarchean
 Era, after a geological crust started to solidify following the earlier molten Hadean Eon. There are microbial mat
  fossils such as stromatolites found in 3.48 billion-year-old sandstone discovered in Western Australia.[10][11][12] 
  Other early physical evidence of a biogenic substance is graphite in 3.7 billion-year-old metasedimentary rocks 
  discovered in southwestern Greenland[13] as well as "remains of biotic life" found in 4.1 billion-year-old rocks 
  in Western Australia.[14][15] According to one of the researchers, "If life arose relatively quickly on Earth … then
  it could be common in the universe."[14]
Photosynthetic organisms appeared between 3.2 and 2.4 billion years ago and began enriching the atmosphere with oxygen.
 Life remained mostly small and microscopic until about 580 million years ago, when complex multicellular life arose,
  developed over time, and culminated in the Cambrian Explosion about 541 million years ago. This sudden 
  diversification of life forms produced most of the major phyla known today, and divided the Proterozoic Eon from the
   Cambrian Period of the Paleozoic Era. It is estimated that 99 percent of all species that ever lived on Earth, over
    five billion,[16] have gone extinct.[17][18] Estimates on the number of Earth's current species range from 10 
    million to 14 million,[19] of which about 1.2 million are documented, but over 86 percent have not been described.
    [20] However, it was recently claimed that 1 trillion species currently live on Earth, with only one-thousandth 
    of one percent described.[21]
The Earth's crust has constantly changed since its formation, as has life since its first appearance. 
Species continue to evolve, taking on new forms, splitting into daughter species, or going extinct in the face 
of ever-changing physical environments. The process of plate tectonics continues to shape the Earth's continents 
and oceans and the life they harbor. Human activity is now a dominant force affecting global change, harming 
the biosphere, the Earth's surface, hydrosphere, and atmosphere with the loss of wild lands, over-exploitation 
of the oceans, production of greenhouse gases, degradation of the ozone layer, and general degradation of soil,
 air, and water quality
History of Earth
From Wikipedia, the free encyclopedia
Jump to navigationJump to search
This article is about scientific evidence concerning the history of Earth. For the history of humans, see History of 
the world.
 
The history of Earth concerns the development of planet Earth from its formation to the present day.[1][2] Nearly 
all branches of natural science have contributed to understanding of the main events of Earth's past, characterized
 by constant geological change and biological evolution.
The geological time scale (GTS), as defined by international convention,[3] depicts the large spans of time from 
the beginning of the Earth to the present, and its divisions chronicle some definitive events of Earth history. 
(In the graphic: Ga means "billion years ago"; Ma, "million years ago".) Earth formed around 4.54 billion years ago, 
approximately one-third the age of the universe, by accretion from the solar nebula.[4][5][6] Volcanic
 outgassing probably created the primordial atmosphere and then the ocean, but the early atmosphere contained 
 almost no oxygen. Much of the Earth was molten because of frequent collisions with other bodies which led
  to extreme volcanism. While the Earth was in its earliest stage (Early Earth), a giant impact collision 
  with a planet-sized body named Theia is thought to have formed the Moon. Over time, the Earth cooled, 
  causing the formation of a solid crust, and allowing liquid water on the surface.
The Hadean eon represents the time before a reliable (fossil) record of life; it began with the formation of
 the planet and ended 4.0 billion years ago. The following Archean and Proterozoic eons produced the beginnings 
 of life on Earth and its earliest evolution. The succeeding eon is the Phanerozoic, divided into three eras: 
 the Palaeozoic, an era of arthropods, fishes, and the first life on land; the Mesozoic, which spanned the rise
  reign, and climactic extinction of the non-avian dinosaurs; and the Cenozoic, which saw the rise of mammals. 
  Recognizable humans emerged at most 2 million years ago, a vanishingly small period on the geological scale.
The earliest undisputed evidence of life on Earth dates at least from 3.5 billion years ago,[7][8][9]during the
 Eoarchean Era, after a geological crust started to solidify following the earlier molten Hadean Eon. There are 
 microbial mat fossils such as stromatolites found in 3.48 billion-year-old sandstone discovered in Western 
 Australia.[10][11][12] Other early physical evidence of a biogenic substance is graphite in 3.7 billion-year-old
  metasedimentary rocks discovered in southwestern Greenland[13] as well as "remains of biotic life" found in 
  4.1 billion-year-old rocks in Western Australia.[14][15] According to one of the researchers, "If life arose 
  relatively quickly on Earth … then it could be common in the universe."[14]
Photosynthetic organisms appeared between 3.2 and 2.4 billion years ago and began enriching the atmosphere with 
oxygen. Life remained mostly small and microscopic until about 580 million years ago, when complex multicellular 
life arose, developed over time, and culminated in the Cambrian Explosion about 541 million years ago. This sudden 
diversification of life forms produced most of the major phyla known today, and divided the Proterozoic Eon from the
 Cambrian Period of the Paleozoic Era. It is estimated that 99 percent of all species that ever lived on Earth, over
  five billion,[16] have gone extinct.[17][18] Estimates on the number of Earth's current species range from 10
  million to 14 million,[19] of which about 1.2 million are documented, but over 86 percent have not been described.
  [20] However, it was recently claimed that 1 trillion species currently live on Earth, with only one-thousandth of 
  one percent described.[21]
The Earth's crust has constantly changed since its formation, as has life since its first appearance. Species continue
 to evolve, taking on new forms, splitting into daughter species, or going extinct in the face of ever-changing 
 physical environments. The process of plate tectonics continues to shape the Earth's continents and oceans and 
 the life they harbor. Human activity is now a dominant force affecting global change, harming the biosphere, 
 the Earth's surface, hydrosphere, and atmosphere with the loss of wild lands, over-exploitation of the oceans'''
