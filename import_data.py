
def parse_data(data, delimiter=','):
    result = []
    
    #split the data string into a list of lines
    lines_list = data.strip().split('\n')

    if not lines_list:
        print("Ocurred error - csv data is empty.")
        return result
    
    header = lines_list[0].split(delimiter)

    if len(header) < 3:
        print("header does not have enough columns.")
        return result  
    
    #process lines and split them into words
    result = [w.split(delimiter) for w in lines_list[1:]]
    
    return result


def highest_score(result):
    if not result:
        print("Error: No data to analyze.")

    #sorting the result list based on the
    #integer value of the third element  in descending order.
    sorted_result = sorted(result, key=lambda x: int(x[2]), reverse=True)
    top_score = int(sorted_result[0][2])

    #creating a list of names with the highest score.
    top_score_people = [name[0] + ' ' + name[1] for name in sorted_result if int(name[2]) == top_score]
    top_score_people.sort()

    return top_score, top_score_people
   


            







        
