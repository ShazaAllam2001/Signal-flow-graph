from re import T
from PyQt5.QtWidgets import *

import networkx as nx

from AppLogic.SolveGraph.forwardPaths import generate_all_fwdpaths, get_fwdPath_gain
from AppLogic.SolveGraph.loops import generate_all_loops, get_loop_gain
from AppLogic.SolveGraph.nontouchingLoops import get_nonTouching_loops
from AppLogic.SolveGraph.deltaCalculations import calculate_delta_i, calculate_delta
from AppLogic.SolveGraph.transferFunctions import calculate_transfer_function
from AppLogic.errorMessage import ErrorMessage

class SolveGraph():
    graph: nx.DiGraph
    source: str
    target: str

    def __init__(self, output: QGroupBox):
        self.outputs = output.children()
    
    def solveForwardPaths(self):
        fwd_paths = list(generate_all_fwdpaths(self.graph, self.source, self.target))
        gains = []
        for path in fwd_paths:
            gains.append(get_fwdPath_gain(self.graph, path))

        fwd_text = "" 
        for index in range(len(fwd_paths)):
            fwd_text +=  "Path: " + str(fwd_paths[index]) + ", Gain: " + str(gains[index]) + "\n"
        self.outputs[1].setText(fwd_text)

        return fwd_paths, gains

    def solveLoops(self):
        cycle_paths = list(generate_all_loops(self.graph))
        gains = []
        for path in cycle_paths:
            gains.append(get_loop_gain(self.graph, path))
 
        cycle_text = "" 
        for index in range(len(cycle_paths)):
            cycle_text += "Path: " + str(cycle_paths[index]) + ", Gain: " + str(gains[index]) + "\n"
        self.outputs[3].setText(cycle_text)

        return cycle_paths, gains

    def solveNontouchingLoops(self, loop_paths):
        nonTouching_paths = get_nonTouching_loops(loop_paths)
 
        nonTouching_text = "" 
        for index in range(len(nonTouching_paths)):
            nonTouching_text += str(index+2) + " non-touching loops:\n"
            for path in nonTouching_paths[index]:
                nonTouching_text += str(path) + ",\n"
            nonTouching_text += "\n"           
        self.outputs[5].setText(nonTouching_text)

        return nonTouching_paths

    def solveDeltas(self, fwd_paths, loops, nonTouching_loops):
        deltas = []
        for path in fwd_paths:
            deltas.append(calculate_delta_i(self.graph, path, loops, nonTouching_loops))
        
        delta = calculate_delta(self.graph, loops, nonTouching_loops)

        deltas_text = "" 
        for index in range(len(fwd_paths)):
            deltas_text += "delta " + str(index+1) + " = " + str(deltas[index]) + "\n" 
        deltas_text += "delta = " + str(delta)  
        self.outputs[7].setText(deltas_text)

        return deltas, delta

    def solveTransferFunctions(self, deltas, delta, fwd_paths):
        transfer_function = calculate_transfer_function(self.graph, deltas, delta, fwd_paths)
        self.outputs[9].setText(str(transfer_function))
        return transfer_function

    def solve(self, source, target):
        self.outputs[1].setText("")
        self.outputs[3].setText("")
        self.outputs[5].setText("")
        self.outputs[7].setText("")
        self.outputs[9].setText("")

        if self.graph.has_node(source) and self.graph.has_node(target):
            self.source = source
            self.target = target
            fwd_paths, fwd_gains = self.solveForwardPaths()
            loop_paths, loop_gains = self.solveLoops()
            nonTouching_paths = self.solveNontouchingLoops(loop_paths)
            deltas, delta = self.solveDeltas(fwd_paths, loop_paths, nonTouching_paths)
            print(deltas, delta)
            self.solveTransferFunctions(deltas, delta, fwd_paths)
        else:
            message = ErrorMessage("Source or/and target does not exist in graph!")
            message.show()
