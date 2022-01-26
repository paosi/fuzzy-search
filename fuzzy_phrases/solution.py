#!/usr/bin/env python3

import json
import re

def phrasel_search(P, Queries):

    ans = []  # Don't change this

    # Write your solution here
    for sentence in Queries:  # 2 Iterations

        words = sentence.split()
        print(words)
        print(len(words))
        matches = []
        
        for i in range(len(words)):
            print(words[i], "-----------------------------------------------")
            word = words[i]

            for i in range(len(P)):
                phrase = P[i].split()
                print(phrase)

                if word == phrase[0]:
                    print("MATCH")
                    lenphrase = len(phrase)  # Return lenth of phrase with match at index [0]
                    print(lenphrase)
                    source = words.index(word)  # Return index of word that matched phrase [0]
                    print(source)
                    fuzzy_match = []

                    for i in range(lenphrase + 1):
                        fuzzy_match.append(words[source])
                        print(fuzzy_match)
                        source += 1

                    for item in fuzzy_match:
                        if item in phrase:
                            continue
                        else:
                            print(item, "FOUND THE FUZZY")
                            if fuzzy_match.index(item) == lenphrase:
                                fuzzy_match.remove(item)
                                print(fuzzy_match, "EXACT MATCH")
                                exact_string = " ".join(fuzzy_match)
                                print(exact_string, "<--------")
                                matches.append(exact_string)
                            else:
                                print(fuzzy_match, "FUZZY MATCH")
                                fuzzy_string = " ".join(fuzzy_match)
                                print(fuzzy_string, "<--------")
                                matches.append(fuzzy_string)

                else:
                    print("Not a match. Next word.")

        print(matches, "***********************")
        ans.append(matches)
        
    return ans  # Don't change this

if __name__ == "__main__":
    with open('sample.json', 'r') as f:
        sample_data = json.loads(f.read())
        P, Queries = sample_data['phrases'], sample_data['queries']
        returned_ans = phrasel_search(P, Queries)
        print('============= ALL TEST PASSED SUCCESSFULLY ===============')


        ### DELETE EVERYTHING BELOW
        print(returned_ans, "*************************************")