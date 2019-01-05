# hebrewSubtitlesPunctuationFliiper
Flip punctuation in broken Hebrew subtitles 

VERY initial script!!!

goal: load text file, go over the rows, for each row -> take the last puncuation bulk (., ..., ...! etc..) and put it in the beginning of the sentence.

it is usefull for LTR (hebrew) subtitles that in some players won't present the punctuation well.
example:
sentence: my dog is cute!!!
new sentence: !!!my dog is cute

known issues:
1. \[this is a sentence in brackets] will be changed into ]\[this is a sentence in brackets
2. "this is.." will be changed into ..""this is

