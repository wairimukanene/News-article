import unittest
from app.models import Articles




class ArticlesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setup(self):
      '''
      Set up method that will run before every Test
      '''

      self.new_article = Articles('the-verge','Richard Lawler','Metas VR roadmap reportedly has four new headsets, with both high-end and cheaper Quest units',
'Metas plans for virtual reality include four new headsets according to a report by The Information. The Project Cambria unit up first is a high-end mixed reality unit, plus another high-end headset and two Quest-like headsets','https://www.theverge.com/2022/5/2/23053888/meta-virtual-reality-headset-cambria-quest-vr-mr',' "https://cdn.vox-cdn.com/thumbor/uBMIca3yNIX7iPk1VrGFQTL24o4=/0x17:1632x871/fit-in/1200x630/cdn.vox-cdn.com/uploads/chorus_asset/file/22963875/Screen_Shot_2021_10_28_at_2.03.39_PM.png','2022-05-03T03:12:06Z')


    def test_instance(self):
      self.assertTrue(isinstance(self.new_article,Articles))


    def test_to_check_instance_variables(self):
      self.assertEqual(self.new_article.id,'the_verge')
      self.assertEqual(self.new_article.author,'Richard Lawler')
      self.assertEqual(self.new_article.title,'Metas VR roadmap reportedly has four new headsets, with both high-end and cheaper Quest units')
      self.assertEqual(self.new_article.description,'Metas plans for virtual reality include four new headsets according to a report by The Information. The Project Cambria unit up first is a high-end mixed reality unit, plus another high-end headset and two Quest-like headsets.')
      self.assertEqual(self.new_article.url,'https://www.theverge.com/2022/5/2/23053888/meta-virtual-reality-headset-cambria-quest-vr-mr')
      self.assertEqual(self.new_article.image,'https://cdn.vox-cdn.com/thumbor/uBMIca3yNIX7iPk1VrGFQTL24o4=/0x17:1632x871/fit-in/1200x630/cdn.vox-cdn.com/uploads/chorus_asset/file/22963875/Screen_Shot_2021_10_28_at_2.03.39_PM.png')
      self.assertEqual(self.new_article.date,'2022-05-03T03:12:06Z')





    if __name__ == '__main__':
      unittest.main() 


