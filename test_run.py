import multiprocessing
from alarm_controller import send_email
import time

class Sigplotter():
    def main(self):
        self.plotterInputQ = multiprocessing.Queue()
        self.plotterOutputQ = multiprocessing.Queue()
        self.plotterStopEvent = multiprocessing.Event()
        self.plotter = send_email(self.plotterInputQ,self.plotterOutputQ,self.plotterStopEvent)
        self.plotter.start()

        inputDict = {}
        inputDict['event_type'] = 'fast_movement'

        self.plotterInputQ.put(inputDict)

        time.sleep(5)

        self.plotterStopEvent.set()

if __name__ == '__main__':
    Sigplotter().main()