import util



class Algorithms:
    def ucs(self,graph,source,destination):
        parent = {}
        closed = []
        open = util.PriorityQueue()
        open.push(source,0)
        
        while True:
            
            if open.isEmpty():
                break
         
            else:
                selected_node = open.pop()
                
            if selected_node == destination:
                break

           
            if selected_node not in closed:
                closed.append(selected_node)
        
            children = graph.neighbours(selected_node)

            if children != None:
                for child in children:
                    city,cost = child
                    if city not in parent.keys():
                        parent[city] = selected_node
            
                    if city == destination:
                        closed.append(city)
                        break
            
                    if cost != None and city not in closed:
                        open.push(city,cost)
        path = [destination]
        curr = destination
        while curr != source:
            curr = parent[curr]
            path.insert(0,curr)

        return path




    def bidirectional(self,graph,source,destination):
        source_parent = {}
        source_visited = []
        source_queue = util.Queue()
        dest_parent = {}
        dest_visited = []
        path = []
        dest_queue = util.Queue()

        source_queue.push(source)
        print(graph.graph.keys())
        print("sourc",source)

        if source in graph.graph.keys():
            print("uuedalsdflajksf")
        else:
            print("no way")
        dest_queue.push(destination)
        
        if graph.neighbours(destination):
            for ele in graph.neighbours(destination):
                if ele[0] == source:
                    return [source, destination]


        while True and source_queue:
            selected = source_queue.pop()
            source_visited.append(selected)
            connected = graph.neighbours(selected)

            if connected != None:
                for child in connected:
                    city,cost = child

                    if city not in source_parent.keys() and city not in source_parent:
                        source_parent[city] = selected
                
                    if city not in source_queue.list and city not in source_visited:
                        source_queue.push(city)
            

            selected_dest = dest_queue.pop()
            dest_visited.append(selected_dest)
            connected_dest = graph.neighbours(selected_dest)
            

            if connected_dest != None:
                for child in connected_dest:
                    city_dest, cost_dest = child
                    
                    if city_dest not in dest_parent.keys() and city_dest not in dest_parent.values():
                        dest_parent[city_dest] = selected_dest
                    if city_dest not in dest_queue.list and city_dest not in dest_visited:
                        dest_queue.push(city_dest)

            
        
            for each in source_queue.list:
                if each == source or each == destination:
                        
                        break
                if each in dest_queue.list:
                    path_dest = []
                    current_dest = dest_parent[each]
                    while current_dest != destination:
                        path_dest.append(current_dest)
        
                        current_dest = dest_parent[current_dest]
                    path_dest.append(destination)
                    
                    current = each
                
                    while current != source:
                        if current not in path:
                            path.insert(0,current)
                            current = source_parent[current]
                    
                    path.insert(0,source)
                
                    return path + path_dest