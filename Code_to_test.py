import pickle


class Trajectory:
    def __init__(self):
        self.something = 0

    def do_something(self):
        if self.something != 0:
            print("It is not 0")
        else:
            print("It is 0")



def DataProcessing(number):
    trj = Trajectory()
    trj.something = number

    output_f='./data/trajectory'+str(number)+'.pkl'

    with open(output_f, 'wb') as f:
        pickle.dump(trj, f, pickle.HIGHEST_PROTOCOL)



if __name__ == "__main__":
    DataProcessing(5)

    DataProcessing(0)
