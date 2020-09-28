import random
from queue import Queue

class Printer:
    def __init__(self, ppm):
        self.page_rate = ppm  # 每分钟打印的张数
        self.current_task = None # 当前任务
        self.time_remaining = 0 # 当前任务执行剩余时间
        
    def tick(self): #模拟打印机执行任务
        if self.current_task != None: # 当前有任务，则任务时间-1
            self.time_remaining -= 1
            if self.time_remaining <= 0: # 任务胜于时间为0， 任务结束
                self.current_task = None
                
                
                
    
    def busy(self): # 当前打印机是否忙碌
        if self.current_task != None:
            return True
        else:
            return False
        

    def start_next(self, newtask): # 开启下一个任务
        self.current_task = newtask
        self.time_remaining = newtask.get_pages() * 60 / self.page_rate
        

class Task:
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)  # 打印页数
        
    def get_stamp(self): # 任务生成时间
        return self.timestamp
        
    def get_pages(self):
        return self.pages
        
    def wait_time(self, current_time): # 任务等待时间
        return current_time - self.timestamp
        
        
def new_task(): # 180秒生成一个任务
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False
        
        
def simulation(num_seconds, pages_per_min):
    """模拟器，通过循环模拟任务执行"""
    printer = Printer(pages_per_min) # 打印机
    print_queue = Queue()     # 打印队列
    waiting_times = [] # 等待时间数组
    
    count = 0
    for current_sec in range(num_seconds):# 模拟执行时间，每执行一次，过1秒        
        if new_task(): # 生成任务
            count += 1
            task = Task(current_sec)
            print_queue.put(task)
            
        if (not printer.busy()) and (not print_queue.empty()): # 打印任务
            next_task = print_queue.get()
            waiting_times.append(next_task.wait_time(current_sec))
            printer.start_next(next_task)
    
        printer.tick() # 打印机执行
        
    
    averageWait=sum(waiting_times)/len(waiting_times)
    print("Average Wait %6.2f secs %3d tasks remaining."%(averageWait,print_queue.qsize()), count)


for i in range(10):
    simulation(3600, 5)




















