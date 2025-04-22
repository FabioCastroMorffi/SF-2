from __future__ import annotations
from functools import total_ordering 
import json

@total_ordering
class Quest:
    def __init__(self, name: str, difficulty: int, \
                 participants: list[str]):
        self.name = name
        self.difficulty = difficulty
        self.participants = participants
    def __lt__(self, other_quest: Quest) -> bool:
        return isinstance(other_quest,Quest) and self.difficulty < other_quest.difficulty
    def __equal__(self, other_quest:Quest)-> bool:
        return isinstance(other_quest, Quest) and self.difficulty == other_quest.difficulty
    def __repr__(self):
        return f'{self.name}'
def threshold_input()->int:
    flag = False
    while not flag:
        try:
            threshold = int(input())
        except ValueError:
            print('Input an integer')
        if 0 <= threshold <= 10:
            flag = True
        else:
            print('input integer between 0 and 10 inclusively') 
    return threshold

def unpacking_quests(lst: list[dict])-> list[Quest]:
    lst = []
    for dict in lst:
        quest = Quest(dict['name'], dict['difficulty'], dict['participants'])
        lst.append(quest)
    return lst
def filtering_quest(lst: list[Quest], threshold:int) -> list[Quest]:
    lst = []
    for quest in lst:
        if quest.difficulty < threshold:
            lst.append(quest)
    lst.sort()






def main():
    try:
        input_file = open('quests.json','r')
    except FileNotFoundError:
        print('File not found')
        exit()
    list_dicts = json.load(input_file)
    threshold = threshold_input()
    lst_quests = unpacking_quests(list_dicts)
    quests_filtered = filtering_quest(threshold, lst_quests)
    '''
    print
    for quest in quests_filtered:
    '''   

    
    