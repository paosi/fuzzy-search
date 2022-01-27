#!/usr/bin/env python3

import json

def phrasel_search(P, Queries):

    ans = []  

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
        S_limit = 99999  # Limit to 99,999 character sentence
        if S_len <= 1:
            print("The query string is too short.")
            break
        if S_len > S_limit:
            sentence = sentence[0: S_limit]
            S_len = len(sentence)

        words = sentence.split()  
        matches = []


        for j in range(len(words)):

            # Set constraints to 1 < len(P) < 1,000,000. Shorten list of phrases if over limit.
            P_len = len(P)
            P_limit = 999999  # Limit to 999,999 phrases

            if P_len <= 1:
                print("There are not enough key phrases. Please enter at least 2.")
                break
            if P_len > P_limit:
                P_len = P_limit

            word = words[j]
        

            for i in range(P_len):

                phrase = P[i].split()

                if word == phrase[0]:

                    len_phrase = len(phrase)  # Return length of phrase with match at index [0]
                    source = j  # Return the index of the matching query word
                    fuzzy_match = []

                    # Create list of possible fuzzy matches from query
                    for i in range(len_phrase + 1):
                        try:
                            fuzzy_match.append(words[source])
                            source += 1
                        except IndexError:
                            break
                    
                    # print(fuzzy_match)
                    fuzzy_match_copy = fuzzy_match.copy()

                    # Determine if there is an exact or fuzzy match
                    for i in range(len(fuzzy_match)):
                        item = fuzzy_match[i]
                        
                        if item in phrase:
                            continue
                        else:
                            if fuzzy_match.index(item) == len(phrase):
                                fuzzy_match_copy.remove(item)

                                if phrase == fuzzy_match_copy:
                                    exact_string = " ".join(fuzzy_match_copy)
                                    matches.append(exact_string)
                                else:
                                    break
                            else:
                                fuzzy_match_copy.remove(item)

                                if phrase == fuzzy_match_copy:                            
                                    fuzzy_string = " ".join(fuzzy_match)
                                    matches.append(fuzzy_string)
                                else:
                                    break
                        
                else:
                    # No matches
                    continue

        #print(matches)
        ans.append(matches)

    return ans  
    

if __name__ == "__main__":
    with open('sample.json', 'r') as f:
        sample_data = json.loads(f.read())
        P, Queries = sample_data['phrases'], sample_data['queries']
        returned_ans = phrasel_search(P, Queries)
        print('============= ALL TEST PASSED SUCCESSFULLY ===============')


        # Check results 
        # solution = sample_data['solution']
        # print(solution == returned_ans)
