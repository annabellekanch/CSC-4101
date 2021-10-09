Project Members:
Annabelle Kanchirathingal &
Benjamin Bordelon

Dr. Gerald Baumgartner

CSC 4101

Oct 8th, 2021

Project Motivations:
    We used our limited knowledge of Scheme to produce a lexical analyzer that can take integer values and produce sutiable tokens out of them while excluding any values such as white spaces or characters. We wanted our lexical analyzer to work to its fullest extent, however due to a lack of time management and a general lack of knowledge we were only able to produce a half-way working analyzer. In our implementation of parseExp and parseRest we tried to make it imitate the grammar as much as possible. Our biggest issue was the implementation of our scanner. The analyzer could only take in integer values and would return any other characters(besides spaces and comments) as Illegal Characters. We know that this issue stems from the fact we could not reinitialize self.buf to accept a new string and then move to the next token. 
    
What Works & Does Not Work:
    Our Scheme pretty printer recognizes integer values and whitespaces and makes sure to exclude white spaces. However, it has trouble identiying characters such as 'a', which is a mistake on our part as we did not know how to properly reinitialize self.buf to accept a new string. 
