import spacy
from benepar.spacy_plugin import BeneparComponent

nlp = spacy.load('en')
nlp.add_pipe(BeneparComponent('benepar_en'))
doc = nlp("i Jinping is a Chinese politician who has served as General Secretary of the Chinese Communist Party (CCP) and Chairman of the Central Military Commission (CMC) since 2012, and President of the People's Republic of China (PRC) since 2013. He has been the paramount leader of China, the most prominent political leader in the country, since 2012. The son of Chinese Communist veteran Xi Zhongxun, he was exiled to rural Yanchuan County as a teenager following his father's purge during the Cultural Revolutionandlived in a cave in the village of Liangjiahe, where he joined the CCP and worked as the party secretary.")
sent = list(doc.sents)[0]
print(sent._.parse_string)
print(list(sent._.children)[0])
