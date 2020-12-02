arr = ['aestheticcottagecore', 'la.lilly', 'aestheticcottagecore', '#cottagecore', '#cottagecorevibes','','', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '#plantcore', '#bedroomdecore', '#plantcollection', '#bedroomideas', '#cozybedroom', '#bedroominspo', '#interiorinspo', '#interiordecor', '#greenbedroom', 'mithara.bui', '1w', 'fairycore.shop', '1w', 'cottagecorefashion', '1w', 'amfadaspud', '1w', 'camille_coker17', '1w', 'paradoxalexx', 
'1w', 'paradoxalexx', '1w', 'one_ebrown', '1w', 'janeyellis54', '1w', 'delicate.lamb', '1w', 'eli_yasa7', '1w', 'mae_tlt', '1w', 'haidedang', '1w', 'mati.luzz', '1w', '_ilaria__p', '1w', 'gismc_13', '1w', 'aniee_0.0_', '1w', 'bakjiapax', '1w', 'teresa_magliulo', '1w', 'hannaholife', '1w', 'edabilgex', '1w', 'miranda.moonchild', '1w', 'elfshits', '1w', 'kirall.1', '1w', 'cherriesandwinnne', '1w', 
'sirenjailer', '@imoonhaneull', '1w', 'keep.spankem', '@redsalt.rocklamp', '2d', 'marynminou', '@cococmpls', '1w', 'alecristineb', '@cafofododani', '1w', 'esme3anna', '@melissajaene', '1w', 'thaliacoatney', '1w', 'virginlv8', '1w', 'by.elisha', '1w', 'siimran1986', 
'1w', 'astridsimmonds', '@hollyraineyy', '1w', 'elif.cansukaplan', '1w', 'fleurmperry', '1w', 'not.merrill', '1w', 'fuzzbuttfotos', '1w', 'thehouseofgentry', '1w', 'meriem.s.e.r', '1w', 'llamalovespotatoes', '1w', 'margaux_martinique', '4d', 'gusandgreen', '1w', 'hannahsdagger', '1w', 'storm_nc', '1w', 'idkhow_u', '6d', 'adalbertjuniorbr', '1w', 'monkeycrabz', '@art_in_the_trash', '1w', 'kaitlyn_spammsssssssss', '1w', 'lafilleauberet', '1w', 'wilderskies', '1w', 'lratraisch', '1w', 'a.e.s.t.h.e.t.i.c_picture', '1w', '_imma_beanbag_', '1w', 'theme.sparkles', '1w', 'erikoul41', '1w', 'annewithane__lucasjadezumann', '1w', 'eowindir', '1w', 'bukankimpoidraa', '1w', 'gallantjennifer', '1w', 'queen.jinri', '1w', 'kenzie_pallante', '1w', 'audramaye', '1w', 'cryptickitsun.e', '1w', 'autumnchild_1704', '3d', 'k.ylieemarie', '1w', 'sharellepage', '1w', 'clementine.patel', '2d', 'half.magic', '1w', 'OCTOBER 30', 'aestheticcottagecore', '9', 'About', 'Blog', 'Jobs', 'Help', 'API', 'Privacy', 'Terms', 'Top Accounts', 'Hashtags', 'Locations', 'Locations', 'Locations', 'Locations', 'Locations', 'Locations', 'Locations', 'Locations', 'Jobs', 'Help', 'API', 'Locations', 'Locations', 'Jobs', 'Help', 'API', 'Locations']

from time import sleep

class Bot:
    def __init__(self):
        print("cool")

    def fetchComments(self):
        store = {}
        i = 0 
        tracker=[]

        while True:
            for element in arr:
                if element == '':
                    continue
                try:
                    store[element]
                    tracker.append(True)
                    i = i +1 
                    difference =  len(tracker) - store[list(store)[-1]] 
                    if difference > 8:
                        print('infinite loop')
                        print(store)
                        print (tracker)
                        print (store[list(store)[-1]])
                        print (len(tracker))
                        endresult = list(store.keys())
                        print(endresult)
                        return endresult
                    continue
                except:
                    tracker.append(False)
                    store[element] = i + 1 
                    i = i + 1     
    
    def cleanComments(self, comments):
        for comment in list(comments):
            print(comment[0])
            if comment[0] == '#':
                comments.remove(comment)
            if comment[0].isupper():
                comments.remove(comment)
            if len(comment)<=2:
                comments.remove(comment)
        return comments       
       
""" myBot = Bot()
comments= myBot.fetchComments()
end = myBot.cleanComments(comments)
print(end) """
#cleanComments = myBot.cleanComments(comments)

#print("end result", cleanComments)


test = ['aestheticcottagecore', 'la.lilly', 'haidedang', 'mati.luzz', '_ilaria__p', 'gismc_13', 'aniee_0.0_', 'bakjiapax', 'teresa_magliulo', 'hannaholife', 'edabilgex', 'miranda.moonchild', 'elfshits', 'kirall.1', 'cherriesandwinnne', 'sirenjailer', '@imoonhaneull', 'keep.spankem', '@redsalt.rocklamp', 'marynminou', '@cococmpls', 'alecristineb', '@cafofododani', 'esme3anna', '@melissajaene', 'thaliacoatney', 'virginlv8', 'by.elisha', 'siimran1986', 'astridsimmonds', 
'@hollyraineyy', 'elif.cansukaplan', 'fleurmperry', 'not.merrill', 'fuzzbuttfotos', 'thehouseofgentry', 'meriem.s.e.r', 'llamalovespotatoes', 'margaux_martinique', 'gusandgreen', 'hannahsdagger', 'storm_nc', 'idkhow_u', 'adalbertjuniorbr', 'monkeycrabz', '@art_in_the_trash', 'kaitlyn_spammsssssssss', 'lafilleauberet', 'wilderskies', 'lratraisch', 'a.e.s.t.h.e.t.i.c_picture', '_imma_beanbag_', 'theme.sparkles', 'erikoul41', 'annewithane__lucasjadezumann', 'eowindir', 'bukankimpoidraa', 'eli_yasa7', 'mae_tlt', 'gallantjennifer', 'queen.jinri', 'kenzie_pallante', 'cryptickitsun.e', 'audramaye', 'autumnchild_1704', 'k.ylieemarie', 'sharellepage', 'clementine.patel', 'half.magic', 'mithara.bui', 'fairycore.shop', 'cottagecorefashion', 'amfadaspud', 'camille_coker17', 'paradoxalexx', 'one_ebrown', 'janeyellis54', 'delicate.lamb']

print(len(test))