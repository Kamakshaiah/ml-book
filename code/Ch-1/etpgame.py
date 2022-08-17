
import random as rnd

class Agent:

    '''
    Following code is a small game that demonstrate learning atmosphere. The "Agent's" initial experience is either awarded or punished based
    on performance measure defined through certain formula i.e. [(a-b)/(a+b)]. The agents learning and total experience were calculated based on a random input from it's learning environment.
    '''

         
    def __init__(self):
        self.exp = 0

    def getExp(self):
        return self.exp
    
class Task(Agent):

    task_list = []
    learning = 1
    total_exp = 0
    
    def __init__(self):
        Agent.__init__(self)
        

    def performTask(self, task_name):
        self.task_list.append(task_name)

        rnd_num = rnd.random() # random input from the environment 
        self.learning = (self.learning - rnd_num)/(self.learning + rnd_num) # learning function
        
        learning_type = ['awarded' if self.learning > rnd_num else 'punished'] # reward for performance 
        self.exp = self.exp + self.learning

        print('Task', task_name, ' was done. Now my experience is ', self.exp, ' and I am ', learning_type, 'for my performance and the learning is ', self.learning)
        return {'learning': self.learning , 'input': rnd_num, 'total_exp': self.exp, 'type': learning_type}
        

if __name__ == '__main__':
    agent = Agent()
    
    print('Initial experience')
    print(agent.exp)
    t = Task()
    t.performTask('one')
    t.performTask('two')
    t.performTask('three')
    t.performTask('four')
    t.performTask('five')
    
    

        


    
