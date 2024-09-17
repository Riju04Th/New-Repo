import cv2
import face_recognition

def compare_images(image_path1, image_path2):
    """
    Compares two images using face recognition and returns True if they match, False otherwise.
    """
    image1 = face_recognition.load_image_file(image_path1)
    image2 = face_recognition.load_image_file(image_path2)
    
    encoding1 = face_recognition.face_encodings(image1)[0]
    encoding2 = face_recognition.face_encodings(image2)[0]
    
    return face_recognition.compare_faces([encoding1], encoding2)[0] 

def get_data_if_match(image_path1, image_path2, data_location):
    """
    Checks if two images match using face recognition, and if so, retrieves data from the specified location.
    """
    if compare_images(image_path1, image_path2):
        # Assuming data is stored in a file with the same name as the image 
        data_file = image_path1.replace(".jpg", ".txt")  # Adjust extension if necessary
        with open(data_file, 'r') as f:
            data = f.read()
            return data
    else:
        return None 

# Example usage
image1_path = "path/to/image1.jpg" 
image2_path = "path/to/image2.jpg"
data_folder = "data_storage/" 

match_result = get_data_if_match(image1_path, image2_path, data_folder)

if match_result:
    print("Match found! Data:", match_result) 
else:
    print("No match found")