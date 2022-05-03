import unittest
from app.models import Source



class SourceTest(unittest .TestCase):
  '''
  Test Class to test the behaviour of the source class
  '''

  def setUp(self):
    '''
    Set up method that will run before every Test
    '''

    self.new_source = Source('al-jazeera-english','Al Jazeera English','News, analysis from the Middle East and worldwide, multimedia and interactives, opinions, documentaries, podcasts, long reads and broadcast ','http://www.aljazeera.com','general','us','en')


    
def test_instance(self):
  self.assertTrue(isinstance(self.new_source,Source))


def test_to_check_instance_variables(self):
        self.assertEqual(self.new_source.id,'al-jazeera-english')
        self.assertEqual(self.new_source.name,'Al Jazeera English')
        self.assertEqual(self.new_source.description,'News, analysis from the Middle East and worldwide, multimedia and interactives, opinions, documentaries, podcasts, long reads and broadcast')
        self.assertEqual(self.new_source.url,'http://www.aljazeera.com')
        self.assertEqual(self.new_source.category,'general')
        self.assertEqual(self.new_source.country,'us')
        self.assertEqual(self.new_source.language,'en')



        if __name__ == '__main__':
          unittest.main() 





