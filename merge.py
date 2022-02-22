#!/usr/bin/env python3


def merge(DB1, DB2):

    DB3 = []
    DB1_copy = DB1.copy()
    DB2_copy = DB2.copy()

    # Iterate through both lists
    for i in DB1:
        for key1, value1 in i.items():
            for j in DB2:
                key_dict = {}
                for key2, value2 in j.items():
                    if key1 == key2:  # Find dict items with matching key
                        value_dict = {**value2, **value1}  # Merge values with DB1 values taking precedence
                        key_dict[key1] = value_dict
                        DB3.append(key_dict)  # Add merged dict items to new list

                        # Remove merged dict items from original lists
                        DB1_copy.remove(i)
                        DB2_copy.remove(j)

    # Add unmatched dict items to list
    for k in DB1_copy:
        DB3.append(k)
    for l in DB2_copy:
        DB3.append(l)

    # Get the key of each item in DB3 and sort the keys
    db_dict = {}
    for m in DB3:
        for key3, value3 in m.items():
            db_dict[key3] = value3
    db_keys = sorted(db_dict.keys())

    # Match the sorted keys to the key of each item in DB3 and add to sorted_DB3 in order
    sorted_DB3 = []
    for item in db_keys:
        for n in DB3:
            for key5, _ in n.items():
                if item == key5:
                    sorted_DB3.append(n)

    return sorted_DB3


if __name__ == "__main__":

    DB1 = [{'134': {'scoreB': 353, 'scoreC': 130, 'scoreD': 135, 'scoreF': 345}},
    {'139': {'scoreA': 214, 'scoreB': 249, 'scoreC': 69}},
    {'152': {'scoreD': 66, 'scoreE': 360}},
    {'156': {'scoreB': 387, 'scoreC': 342, 'scoreF': 115}},
    {'189': {'scoreB': 390, 'scoreC': 59, 'scoreF': 280}},
    {'198': {'scoreA': 216, 'scoreB': 419, 'scoreD': 47, 'scoreF': 266}},
    {'229': {'scoreA': 294, 'scoreB': 117, 'scoreE': 108, 'scoreF': 135}},
    {'25': {'scoreB': 327, 'scoreC': 307, 'scoreE': 47}},
    {'258': {'scoreB': 231, 'scoreC': 143, 'scoreE': 379}},
    {'264': {'scoreD': 386, 'scoreF': 11}},
    {'280': {'scoreA': 310, 'scoreD': 92, 'scoreE': 169}},
    {'282': {'scoreA': 176, 'scoreC': 347, 'scoreD': 8, 'scoreE': 395}},
    {'3': {'scoreB': 354, 'scoreC': 108, 'scoreD': 128}},
    {'313': {'scoreA': 263, 'scoreB': 70, 'scoreC': 323, 'scoreF': 215}},
    {'318': {'scoreA': 240, 'scoreF': 84}},
    {'327': {'scoreA': 174, 'scoreC': 369, 'scoreE': 261, 'scoreF': 335}},
    {'337': {'scoreB': 332, 'scoreC': 80, 'scoreE': 31}},
    {'35': {'scoreA': 161, 'scoreB': 407, 'scoreF': 22}},
    {'351': {'scoreA': 189, 'scoreB': 120, 'scoreD': 346, 'scoreF': 277}},
    {'358': {'scoreA': 313, 'scoreB': 51, 'scoreC': 334, 'scoreD': 10}},
    {'370': {'scoreA': 350, 'scoreB': 166, 'scoreC': 292, 'scoreF': 100}},
    {'374': {'scoreA': 211, 'scoreF': 99}},
    {'379': {'scoreD': 241, 'scoreE': 240, 'scoreF': 334}},
    {'380': {'scoreA': 2, 'scoreC': 281, 'scoreE': 375}},
    {'399': {'scoreB': 351, 'scoreD': 285, 'scoreE': 413}},
    {'407': {'scoreB': 55, 'scoreE': 319, 'scoreF': 293}},
    {'41': {'scoreB': 397, 'scoreD': 331, 'scoreE': 310, 'scoreF': 407}},
    {'437': {'scoreA': 195, 'scoreB': 339, 'scoreD': 218}},
    {'465': {'scoreA': 25, 'scoreB': 49, 'scoreC': 178, 'scoreE': 334}},
    {'484': {'scoreA': 417, 'scoreE': 329, 'scoreF': 312}},
    {'487': {'scoreA': 260, 'scoreB': 65, 'scoreD': 392, 'scoreF': 206}},
    {'516': {'scoreB': 326, 'scoreC': 113, 'scoreD': 418, 'scoreE': 141}},
    {'530': {'scoreC': 242, 'scoreD': 278, 'scoreF': 104}},
    {'556': {'scoreA': 143, 'scoreC': 264, 'scoreE': 209, 'scoreF': 202}},
    {'643': {'scoreB': 322, 'scoreD': 5, 'scoreE': 200}},
    {'653': {'scoreA': 357, 'scoreD': 248, 'scoreE': 191}},
    {'656': {'scoreB': 258, 'scoreD': 31, 'scoreF': 109}},
    {'657': {'scoreA': 235, 'scoreE': 43, 'scoreF': 7}},
    {'675': {'scoreC': 369, 'scoreF': 311}},
    {'681': {'scoreA': 100, 'scoreB': 88, 'scoreD': 259, 'scoreF': 150}},
    {'686': {'scoreC': 178, 'scoreE': 191, 'scoreF': 268}},
    {'706': {'scoreA': 262, 'scoreB': 106, 'scoreD': 96}},
    {'711': {'scoreA': 207, 'scoreB': 99, 'scoreC': 365}},
    {'721': {'scoreB': 62, 'scoreF': 18}},
    {'747': {'scoreA': 161, 'scoreB': 402, 'scoreE': 294, 'scoreF': 340}},
    {'769': {'scoreA': 301, 'scoreB': 178, 'scoreC': 300, 'scoreE': 352}},
    {'770': {'scoreA': 102, 'scoreB': 317, 'scoreF': 294}},
    {'783': {'scoreA': 327, 'scoreB': 271, 'scoreD': 144, 'scoreF': 46}},
    {'819': {'scoreA': 370, 'scoreC': 5}},
    {'833': {'scoreB': 90, 'scoreF': 77}},
    {'846': {'scoreA': 275, 'scoreC': 235, 'scoreF': 230}},
    {'862': {'scoreA': 103, 'scoreB': 122, 'scoreE': 307}},
    {'885': {'scoreC': 245, 'scoreD': 330, 'scoreE': 367, 'scoreF': 218}},
    {'894': {'scoreA': 245, 'scoreC': 295, 'scoreD': 241, 'scoreF': 200}},
    {'905': {'scoreA': 235, 'scoreE': 158, 'scoreF': 120}},
    {'984': {'scoreA': 100, 'scoreB': 273, 'scoreD': 83}},
    {'998': {'scoreA': 91, 'scoreB': 223}}]

    DB2 = [{'11': {'scoreA': 263, 'scoreC': 267, 'scoreD': 115}},
    {'152': {'scoreA': 279, 'scoreB': 22, 'scoreD': 379}},
    {'156': {'scoreA': 82, 'scoreC': 157, 'scoreD': 53, 'scoreF': 359}},
    {'161': {'scoreE': 260, 'scoreF': 221}},
    {'189': {'scoreA': 172, 'scoreB': 304, 'scoreC': 9, 'scoreF': 360}},
    {'258': {'scoreA': 375, 'scoreC': 204, 'scoreE': 200}},
    {'261': {'scoreA': 254, 'scoreB': 222, 'scoreC': 230, 'scoreE': 331}},
    {'264': {'scoreB': 119, 'scoreC': 197, 'scoreE': 112, 'scoreF': 225}},
    {'280': {'scoreB': 48, 'scoreE': 286, 'scoreF': 170}},
    {'282': {'scoreA': 43, 'scoreE': 193, 'scoreF': 77}},
    {'285': {'scoreB': 61, 'scoreC': 55, 'scoreE': 221, 'scoreF': 121}},
    {'291': {'scoreB': 19, 'scoreC': 107, 'scoreF': 73}},
    {'3': {'scoreA': 215, 'scoreD': 95, 'scoreF': 137}},
    {'300': {'scoreB': 141, 'scoreD': 292, 'scoreF': 391}},
    {'306': {'scoreA': 377, 'scoreD': 273, 'scoreE': 220, 'scoreF': 157}},
    {'324': {'scoreB': 310, 'scoreE': 353}},
    {'337': {'scoreA': 29, 'scoreC': 294, 'scoreE': 186}},
    {'35': {'scoreA': 162, 'scoreD': 39, 'scoreF': 315}},
    {'351': {'scoreB': 205, 'scoreC': 84, 'scoreE': 360}},
    {'358': {'scoreA': 12, 'scoreB': 198, 'scoreE': 64}},
    {'364': {'scoreB': 102, 'scoreD': 130, 'scoreF': 368}},
    {'370': {'scoreA': 293, 'scoreB': 294, 'scoreD': 58, 'scoreE': 179}},
    {'379': {'scoreB': 241, 'scoreC': 296, 'scoreE': 206}},
    {'380': {'scoreA': 125, 'scoreC': 89, 'scoreD': 306, 'scoreE': 77}},
    {'407': {'scoreB': 280, 'scoreE': 369, 'scoreF': 303}},
    {'41': {'scoreB': 198, 'scoreC': 14, 'scoreE': 164}},
    {'423': {'scoreA': 304, 'scoreB': 202, 'scoreE': 37}},
    {'437': {'scoreA': 158, 'scoreB': 256, 'scoreC': 74, 'scoreF': 285}},
    {'44': {'scoreB': 323, 'scoreC': 415, 'scoreD': 84, 'scoreF': 188}},
    {'465': {'scoreA': 366, 'scoreB': 117, 'scoreF': 97}},
    {'484': {'scoreA': 372, 'scoreB': 173, 'scoreC': 103}},
    {'487': {'scoreA': 408, 'scoreE': 384, 'scoreF': 254}},
    {'493': {'scoreA': 197, 'scoreB': 390, 'scoreC': 368}},
    {'530': {'scoreC': 245, 'scoreF': 245}},
    {'556': {'scoreA': 48, 'scoreB': 153, 'scoreC': 267}},
    {'566': {'scoreA': 308, 'scoreD': 231, 'scoreE': 41, 'scoreF': 262}},
    {'615': {'scoreD': 5, 'scoreE': 108}},
    {'622': {'scoreC': 146, 'scoreE': 273}},
    {'653': {'scoreC': 371, 'scoreD': 193, 'scoreF': 339}},
    {'657': {'scoreC': 37, 'scoreE': 192, 'scoreF': 356}},
    {'675': {'scoreA': 130, 'scoreB': 120, 'scoreD': 278, 'scoreE': 291}},
    {'681': {'scoreA': 320, 'scoreB': 314, 'scoreC': 386, 'scoreE': 393}},
    {'686': {'scoreB': 265, 'scoreD': 373, 'scoreF': 228}},
    {'706': {'scoreC': 166, 'scoreE': 188, 'scoreF': 415}},
    {'721': {'scoreD': 336, 'scoreE': 285, 'scoreF': 120}},
    {'743': {'scoreC': 24, 'scoreD': 310, 'scoreE': 67, 'scoreF': 396}},
    {'747': {'scoreA': 229, 'scoreB': 329, 'scoreD': 292, 'scoreE': 69}},
    {'756': {'scoreA': 113, 'scoreB': 191, 'scoreD': 245}},
    {'765': {'scoreB': 183, 'scoreD': 227}},
    {'785': {'scoreB': 353, 'scoreC': 333, 'scoreD': 28, 'scoreF': 109}},
    {'805': {'scoreA': 155, 'scoreC': 236, 'scoreF': 346}},
    {'809': {'scoreA': 393, 'scoreB': 232, 'scoreC': 308}},
    {'826': {'scoreA': 54, 'scoreD': 72, 'scoreF': 243}},
    {'833': {'scoreB': 283, 'scoreD': 412, 'scoreE': 342, 'scoreF': 232}},
    {'844': {'scoreA': 408, 'scoreC': 282, 'scoreE': 178}},
    {'846': {'scoreA': 243, 'scoreB': 66, 'scoreC': 283, 'scoreF': 341}},
    {'848': {'scoreA': 332, 'scoreB': 6, 'scoreE': 392, 'scoreF': 101}},
    {'859': {'scoreC': 338, 'scoreE': 262, 'scoreF': 257}},
    {'885': {'scoreA': 362, 'scoreE': 78, 'scoreF': 85}},
    {'889': {'scoreA': 205, 'scoreE': 199, 'scoreF': 306}},
    {'894': {'scoreC': 405, 'scoreE': 393}},
    {'928': {'scoreA': 162, 'scoreD': 175, 'scoreF': 373}},
    {'956': {'scoreC': 69, 'scoreD': 216, 'scoreE': 175, 'scoreF': 356}},
    {'98': {'scoreB': 63, 'scoreD': 154, 'scoreF': 140}}]


    print(merge(DB1, DB2))

    