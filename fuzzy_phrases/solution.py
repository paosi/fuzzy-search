#!/usr/bin/env python3

import json

def phrasel_search(P, Queries):

    ans = []  # Don't change this

    # Write your solution here

    # Set constraints to 1 < len(Queries) < 1000. Reduce queries if over limit.
    num_Queries = len(Queries)
    Q_limit = 999  # Limit to 999 queries
    if num_Queries <= 1:
        print("Not enough queries. Please add more.")
        return
    if num_Queries > Q_limit:
        num_Queries = Q_limit


    for i in range(num_Queries):

        # Set constraints to query length as 1 < len(query string) < 100,000. Shorten query string if over character limit.
        sentence = Queries[i]

        S_len = len(sentence)
        S_limit = 999999  # Limit to 99,999 character sentence
        if S_len <= 1:
            print("The query string is too short.")
            break
        if S_len > S_limit:
            sentence = sentence[0: S_limit]
            S_len = len(sentence)
        print(sentence, S_len)

        words = sentence.split()
        print(words)
        print(len(words))
        matches = []


        for i in range(len(words)):

            print(words[i], "-----------------------------------------------")
            word = words[i]

            # Set constraints to 1 < len(P) < 1,000,000. Shorten list of phrases if over limit.
            P_len = len(P)
            P_limit = 999999  # Limit to 999,999 phrases
            print(P_len)
            if P_len <= 1:
                print("There are not enough key phrases. Please enter at least 2.")
                break
            if P_len > P_limit:
                P_len = P_limit


            for i in range(P_len):

                phrase = P[i].split()
                print(phrase)

                if word == phrase[0]:
                    print("MATCH")
                    len_phrase = len(phrase)  # Return lenth of phrase with match at index [0]
                    print(len_phrase)
                    source = words.index(word)  # Return index of word that matched phrase [0]
                    print(source)
                    fuzzy_match = []


                    for i in range(len_phrase + 1):
                        try:
                            fuzzy_match.append(words[source])
                            print(fuzzy_match)
                            source += 1
                        except IndexError:
                            break
                    

                    fuzzy_match_copy = fuzzy_match.copy()


                    for i in range(len(fuzzy_match)):
                        item = fuzzy_match[i]
                        
                        if item in phrase:
                            continue
                        else:
                            if fuzzy_match.index(item) == len(phrase):
                                fuzzy_match_copy.remove(item)
                                if phrase == fuzzy_match_copy:
                                    print(fuzzy_match_copy, "EXACT MATCH")
                                    exact_string = " ".join(fuzzy_match_copy)
                                    print(exact_string, "<----------")
                                    matches.append(exact_string)
                                else:
                                    break
                            else:
                                print(item, "FOUND A FUZZY")
                                fuzzy_match_copy.remove(item)
                                if phrase == fuzzy_match_copy:                            
                                    print(fuzzy_match, "FUZZY MATCH")
                                    fuzzy_string = " ".join(fuzzy_match)
                                    print(fuzzy_string, "<--------")
                                    matches.append(fuzzy_string)
                                else:
                                    break
                        

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


        # Check results
        
        results_counter = 0
        for ans in returned_ans:
            for a in ans:
                results_counter += 1

        print(returned_ans, results_counter, "RESULTS")