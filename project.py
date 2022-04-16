import requests

def main():
    #get the Json response from the given API, parse it and sort it by the height in inches
    response = requests.get('https://mach-eight.uc.r.appspot.com/')
    dataset = response.json()['values']

    #ask user's queries and get its answer, printing it in the asked format
    print('Insert a number to match it with the sum of two NBA players height or any key to exit')
    while(True):
        query = input('>')
        if not query.isnumeric():
            print('Exit succesfully')
            break
        queryAnswer = getPlayers(dataset,int(query))
        if not queryAnswer:
            print('No matches found')
        else:
            for playersPair in queryAnswer:
                print(f"- {playersPair[0]['first_name']} {playersPair[0]['last_name']}\t{playersPair[1]['first_name']} {playersPair[1]['last_name']}")


def getPlayers(data:list,target:int) -> list:
    """
    Hashing strategy to find the pairs of players which sum of heights in inches is equal to the given target- Average time Complexity: O(n), Space Complexity: O(n)

    Parameters
    ----------
    data:
        List of dictionaries that contains the information of all the players
    target:
        The desired sum of the height in inches of the pairs of players that are going to be founded

    Returns
    -------
    list
        a list of pairs of dictionaries that contains the information of all the pairs of players of which the sum of their height in inches is equal to the target
    """
    #Creating the dictionary of heights and the answer´s deque. It is a deque since append on a list is O(n) and in a deque is O(1), parsing it later to a list is also O(n) so it is more efficient than doing 'n' appends of cost 'n'.
    players_height = {}
    answer = []
    for player in data:
        #is any player with the height needed to sum the target in the dictionary?
        needed_height = str(target - int(player['h_in']))   
        if players_height.get(needed_height,0):
            #Generate the pairs
            for pair in players_height[needed_height]:
                answer.append((player,pair))

        #if player not in dict, generate array in the key and then append him to it
        if not players_height.get(player['h_in'],0):
            players_height[player['h_in']] = []
        players_height[player['h_in']].append(player)
     
    return answer
    
if __name__ == "__main__":  
    main()
 