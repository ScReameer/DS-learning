from collections import deque, defaultdict


tasks = [(36871, 'office', False),
(40690, 'office', False),
(35364, 'voltage', False),
(41667, 'voltage', True),
(33850, 'office', False)
]


def task_manager(tasks:list) -> defaultdict:
    
    result_dict = defaultdict(deque)
    
    for task_num, server_name, high_priority in tasks:
        
        if high_priority:
            result_dict[server_name].appendleft(task_num)
        else:
            result_dict[server_name].append(task_num)
            
    return result_dict


print(task_manager(tasks))
