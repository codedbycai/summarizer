import re
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

def nettoyer_segmenter(text: str,langue="french"):
    
    text = re.sub(r"^#{1,6}\s*", "", text, flags=re.MULTILINE)          # titres #, ##, etc...

    text = re.sub(r"^\s*[-*+]\s+", "", text, flags=re.MULTILINE)        # listes -, * ou +
    text = re.sub(r"(\d+)[\.\)]", r"\1", text)                          #  "1." ou "1)" 
    
    text = re.sub(r"^[-*_]{3,}\s*$", "", text, flags=re.MULTILINE)      # (---, *** ou ___)

    text = re.sub(r"!\[.*?\]\(.*?\)", "", text)                         # images ![alt](url)

    text = re.sub(r"\[\s*\]\([^)]+\)", "", text)                        # liens texte vide
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)                # liens [texte](url) 
    
    text = re.sub(r"`{1,3}(.*?)`{1,3}", r"\1", text)                    # code


    text = re.sub(r"\*{1,3}(.*?)\*{1,3}", r"\1", text)                  # Gras et italique
    text = re.sub(r"^>+\s*", "", text, flags=re.MULTILINE)              # tab:  >, >>, etc...

    text = re.sub(r"_{1,3}(.*?)_{1,3}", r"\1", text)                    # __texte__

    text = re.sub(r"<.*?>", "", text)                                   # <b>...</b>
    
    text = re.sub(r"[\x00-\x08\x0B-\x0C\x0E-\x1F]+", " ", text)         # caractères non imprimables

    text = re.sub(r"(\w)[-'](\w)", r"\1 \2", text)                         # texte-texte

    text = re.sub(r"\s+", " ", text)                                    # réduire les espaces multiples
    # print(text)
    # print()

    phrases = sent_tokenize(text,language=langue)                       # separe en phrases
    # for i,phrase in enumerate(phrases,1):
    #     print(f"{i}. {phrase}")
    # print()
    
    stop_words = set(stopwords.words(langue))
    stop_words.discard("pas")

    phrases_nettoyer = []
    for phrase in phrases:
        tokens = word_tokenize(phrase, language=langue)                 # Phrase en mots
        #print(tokens)
        tokens = [mot.lower() for mot in tokens]                        # Conversion en minuscules
        tokens = [mot for mot in tokens if mot.isalnum()]               # Suppression de la ponctuation 
        tokens = [mot for mot in tokens if mot not in stop_words]       # filtrage stop words
        # Stemming ou lemmatisation basique à voir
        phrases_nettoyer.append(tokens)

    return phrases_nettoyer
