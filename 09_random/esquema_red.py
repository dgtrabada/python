import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

class red:
    def __init__(self, Capa,ver_pesos):
        a=[]
        for i in Capa:
            a.append(np.zeros(i))
        self.Capa = np.array(a) 
        self.ver_pesos = ver_pesos

         
    def plt(self):
        G = nx.Graph()
        Capa_label=[]
        abc="abcdefg"
        abc2="wvxyz"
        for i in range(len(self.Capa)):
            aux=[]
            for j in range(len(self.Capa[i])):
                aux.append(abc[i]+str(j))
            Capa_label.append(aux)
        
        # Capa_label=[
        #     ['a3','a2','a1'],
        #     ['b4','b3','b2','b1'],
        #     ['c3','c2','c1']]
    
        edge_labels_aux={}
        edges=[]
        
        for i in range(len(self.Capa)-1):
            for x in range(len(self.Capa[i])):
                for y in range(len(self.Capa[i+1])):
                    edges.append([Capa_label[i][x],Capa_label[i+1][y]])
                    d=(Capa_label[i][x],Capa_label[i+1][y])
                    w=abc2[i]
                    w=w+Capa_label[i][x][1]+Capa_label[i+1][y][1]
                    edge_labels_aux.update({d : w})   
                    
        G.add_edges_from(edges)
        pos = nx.spring_layout(G)

        for x in range(len(self.Capa)):
             for y in range(len(self.Capa[x])):
                    pos[Capa_label[x][y]]=[x,len(Capa_label[x])/2-y]
        
    
        nx.draw(
            G, pos, edge_color='darkgrey', width=1, linewidths=1,
            node_size=600, node_color='pink', alpha=0.9,
            labels={node: node for node in G.nodes()}
        )
      
        if self.ver_pesos:
            nx.draw_networkx_edge_labels(
                G, pos,
                edge_labels=edge_labels_aux,
                font_color='red'
            )
    
        plt.figure()
        #plt.axis('off')
        #plt.show()
        return plt
     
    def Pintar(self,A,W,B,V,C):
        G = nx.Graph()
        edge_labels_aux={}
        edges=[]
        for i in range(len(A)):
            l="a"+str(i)
            for j in range(len(B)):
                ll="b"+str(j)
                edges.append([l,ll])

        for i in range(len(B)):
            l="b"+str(i)
            for j in range(len(C)):
                ll="c"+str(j)
                edges.append([l,ll])
    
        for i in range(len(C)):
            l="c"+str(i)
        
        G.add_edges_from(edges)
        pos = nx.spring_layout(G)

        for y in range(len(A)):
            l="a"+str(y)
            pos[l]=[0,-len(A)/2+y]
        
        for y in range(len(B)):
            l="b"+str(y)
            pos[l]=[1,-len(B)/2+y]    
        
        for y in range(len(C)):
            l="c"+str(y)
            pos[l]=[2,-len(C)/2+y] 
        
        color=[]
        for i in pos:
            if i[0] == "a":
                if A[int(i[1])] > 0.5:
                    color.append("yellowgreen")
                else:
                    color.append("coral")  
            if i[0] == "b":
                if B[int(i[1])] > 0.5:
                    color.append("yellowgreen")
                else:
                    color.append("coral") 
            if i[0] == "c":
                if C[int(i[1])] > 0.5:
                    color.append("yellowgreen")
                else:
                    color.append("coral") 
        widthaux=[]
        max_l=4
        min_l=0
        for i in edges:
            if i[0][0] == "a":
                f = W[int(i[0][1])][int(i[1][1])] 
            if i[0][0] == "b":
                f = V[int(i[0][1])][int(i[1][1])]
            widthaux.append( 
                max_l*(f - W.min())/(W.max()- W.min())  
                + min_l*(W.max() - f )/(W.max()- W.min()) )   
        nx.draw(
            G, pos, 
            edge_color="cornflowerblue",
            width=widthaux, 
            linewidths=1,
            node_size=400, 
            node_color=color, 
            alpha=0.9,
            labels={node: node for node in G.nodes() } 
        ) 
        plt.figure()
        #plt.axis('off')
        return plt #.show()        
 
