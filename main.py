import os
from classesandmethods import RenamingDictionary, LabelSeparator, PolygonSeparator, XYSeparator, creating_final_json_dict
import json
# Renaming images
'''
path = 'C:/Users/wuethral/Desktop/Create_json/images/Syringe'
image_number = 0
for f in os.listdir(path):
    old_file = os.path.join(path,f)
    if old_file != path + '\\.DS_Store':
        new_name = 'frame_' str(image_number) + '.jpg'
        new_file = os.path.join(path, new_name)
        os.rename(old_file, new_file)
        image_number += 1
'''
dict = {0: {'Stuhl': [[(386, 267), (471, 479), (636, 322), (394, 256)], [(199, 151), (149, 244), (296, 252), (296, 145), (207, 155)]]}, 1: {'Stuhl': [[(225, 227), (228, 308), (297, 309), (314, 242), (229, 222)]], 'Computer': [[(565, 390), (756, 286), (747, 454), (578, 399)]]}}
list_of_labels = ['Stuhl', 'Computer']

# Renaming dict, so that every page number (for example '0') becomes frame_pagenumber (for example frame_0). This is new_dict.
mask_dict = RenamingDictionary(dict)
mask_dict_new = mask_dict.rename()

# Creating a new list (list_for_ever_label) with frame and label for every label
list_for_every_lab = LabelSeparator(mask_dict_new)
list_for_every_label = list_for_every_lab.createlabellist(list_of_labels)

# Creating a new list (list_for_ever_polygon) so that every polygon is 1 index in the list
list_for_every_pol = PolygonSeparator(list_for_every_label)
list_for_every_polygon = list_for_every_pol.createpolygonlist()

# Ordering x, y coordinates and creating new list (list_of_ordered_x_y
list_of_ord_x_y = XYSeparator(list_for_every_polygon)
list_of_ordered_x_y = list_of_ord_x_y.separatexy()

# Creating a new dictionary that will be filled afterwards and is the building block for the dict that we want to turn into json
json_dict_final = {}

# Every frame with polygons as the key of the json_dict_final dictionary
for key in mask_dict_new:
    json_dict_final[key] = {"filename": key, "regions": []}

# Filling the regions of the json_dict_final with the polygons in list_of_ordered_x_y
json_dictionary_final = creating_final_json_dict(json_dict_final, list_of_ordered_x_y )

#Creating json_file
s = json.dumps(json_dictionary_final)

with open('polygon_labels.json', 'w') as f:
    f.write(s)








