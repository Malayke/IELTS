import unittest
from process import process_image

class TestProcessImage(unittest.TestCase):
    def test_process_image(self):
        img_path = 'test_images/29.png'
        expected_output = [
            ['beauty', 'bed', 'bedroom', 'bed sheet'], 
            ['bedsit', 'behaviors', 'belt', 'benefit'], 
            ['beverage', 'bibliography', 'bicycle', 'bill'], 
            ['biologist', 'bird', 'birth', 'blanket'], 
            ['blast', 'block', 'blouse', 'board'], 
            ['boarder', 'boat', 'bone', 'bowl'], 
            ['bowling', 'branch', 'breakfast', 'brick'], 
            ['bridge', 'brochures', 'building', 'bungalow'], 
            ['burger', 'burglar', 'bus', 'cab']
        ]
        result = process_image(img_path)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()
