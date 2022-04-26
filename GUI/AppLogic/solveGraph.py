from PyQt5.QtWidgets import *

import networkx as nx

from AppLogic.SolveGraph.forwardPaths import generate_all_fwdpaths, get_fwdPaths_gains
from AppLogic.SolveGraph.loops import generate_all_loops, get_loops_gains
from AppLogic.SolveGraph.nontouchingLoops import *
from AppLogic.SolveGraph.transferFunctions import *
from AppLogic.errorMessage import ErrorMessage

class SolveGraph():
    graph: nx.DiGraph
    source: str
    target: str

    def __init__(self, output: QGroupBox):
        self.output = output
    
    def solveForwardPaths(self):
        fwd_paths = list(generate_all_fwdpaths(self.graph, self.source, self.target))
        gains = []
        fwd_paths_nodes = []
        for path in fwd_paths:
            gains.append(get_fwdPaths_gains(self.graph, path))

        outputs = self.output.children() 
        fwd_text = "" 
        for index in range(len(fwd_paths)):
            fwd_text +=  "Path: " + str(fwd_paths[index]) + ", Gain: " + str(gains[index]) + "\n"
        outputs[1].setText(fwd_text)

        return fwd_paths_nodes, gains

    def solveLoops(self):
        cycle_paths = list(generate_all_loops(self.graph))
        gains = []
        for path in cycle_paths:
            gains.append(get_loops_gains(self.graph, path))

        outputs = self.output.children() 
        cycle_text = "" 
        for index in range(len(cycle_paths)):
            cycle_text += "Path: " + str(cycle_paths[index]) + ", Gain: " + str(gains[index]) + "\n"
        outputs[3].setText(cycle_text)

        return cycle_paths, gains

    def solveNontouchingLoops(self):
        pass

    def solveTransferFunctions(self):
        pass

    def solve(self, source, target):
        if self.graph.has_node(source) and self.graph.has_node(target):
            self.source = source
            self.target = target
            fwd_paths, fwd_gains = self.solveForwardPaths()
            loop_paths, loop_gains = self.solveLoops()
            self.solveNontouchingLoops()
            self.solveTransferFunctions()
        else:
            message = ErrorMessage("Source or/and target does not exist in graph!")
            message.show()
