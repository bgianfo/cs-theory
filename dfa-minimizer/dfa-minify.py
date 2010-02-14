#!/usr/bin/env python
# -*- coding: utf-8 -*-:

# Note: This source file contains utf-8 symbols, edit and 
#       run in a compatible editor and terminal.
#
# Author: Brian Gianforcaro (bjg1955@cs.rit.edu)
# Course: Computer Science Theory
#
# Simple implementation of the MyHill-Nerode DFA Minimization Algorithm.
#
##############################################################################
# Input dfa's are in the form:
# 
# initial <state>
# <curr-state> <current-char> <next-state>
# final <state>
#      or
# final <state>,<state>,...etc
# Any line beginning with '#' is a comment.
# 
#  Example:
#  --------
#  initial 1
#  1 1 1
#  1 0 2
#  2 1 2
#  2 0 1
#  final 1
##############################################################################
#
# DFA is defined as a 5-tuple ( Q,   Σ*,    δ,    q0, F )  
class minify:
    # Q     - Indexable data structure of states in the DFA
    # sigma - Indexable data structure containing symbols in the DFA's alphabet
    # delta - Function mapping from curr char and state to the next state.
    # q0    - Initial state of the DFA begins operation.
    # F     - Set of final states in the DFA
    def __init__( self, Q, sigma, delta, q0, F ):
      """
      Minify constructor
      """
      self.__Q     = Q
      self.__q0    = q0
      self.__delta = delta
      self.__F     = F
      self.__sigma = sigma

    def output(self):
      """
      Print all members 
      """
      print "DFA: (Q, Σ*, δ, q0, F)"
      print "Q:", ', '.join(self.__Q)
      print "Σ*:", ', '.join(self.__sigma)
      print "q0:", self.__q0
      print "F:", ', '.join(self.__F)
      print "δ|"," | ".join(map(str,self.__Q))
      print "-----"* len(self.__Q) 
      for char in self.__sigma:
          results = map( lambda state: self.__delta(state, char), self.__Q )
          print char, "|", " | ".join(map(str, results))
      print "-----"* len(self.__Q) 

    def write(self, filename):
      """
      Output the DFA to a file: filename
      """

      fd = open( filename, 'wr' )
      fd.write( "initial %s\n" % self.__q0 )
      for state in self.__Q:
        for c in self.__sigma:
          if self.__delta( state, c ):
            fd.write( "%s %s %s\n" % ( state, c, self.__delta(state,c) ) )

      fd.write( "final %s\n" % ','.join(self.__F) )
      fd.close()

    # Stupid hash function for any arbitrary value
    def __hash(self, value):
        d = {}
        for state in self.__Q:
            d[state] = value
        return d

    def __reachable(self):
        """
        Create a set of states reachable from initial, and return.
        """
        initial = self.__q0
        collector = self.__hash(False)
        collector[initial] = True
        waiting = [initial]

        while len(waiting):
          s = waiting.pop()
          for a in self.__sigma:
            next = self.__delta(s, a)
            if collector[next] == False:
              collector[next] = True
              waiting.append(next)

        return [state for state in self.__Q if collector[state]]

    def __calc_equality(self):
        """
        Compare states for equality using the Myhill-Nerode equality matrix.
        """
        # -------------
        # |-|1|2|3|4|5|
        # |1|-|-|-|-|-| 
        # |2| |-|-|-|-| 
        # |3| | |-|-|-|
        # |4| | | |-|-|
        # |5| | | | |-|
        # -------------
        matrix = []
        matrix.append(self.__F)
        matrix.append( [s for s in self.__Q if s not in self.__F] )

        updating = True
        while updating:
          updating = False
          # check all classes
          for m in matrix:
            changed = False
            # All characters in the alphabet
            for char in self.__sigma:
              nextm, new = None, []
              for state in m:
                # If we don't have a next, find one
                if nextm == None:
                  for row in matrix:
                    if self.__delta(state, char) in row:
                      nextm = row 
                # We have found a non equal state, add it to the new row.
                elif self.__delta(state, char) not in nextm:
                  new.append( state )
                  updating, changed = True, True

              # If we have changed, then update classes, and move on.
              if changed:
                old = [state for state in m if state not in new]
                matrix.remove( m )
                matrix.append( old )
                matrix.append( new )
                break

        return matrix

    def __transform(self, myhillMatrix):
        """
        Build a new DFA given the Myhill-Nerode equivalences. 
        """

        start, delta, states, accepts, map = None , None, [], [], {}

        # Find new start state, while building new map.
        for cls in myhillMatrix:
          states.append( cls[0] )
          for state in cls:
            map[state] = cls[0]
            if state is self.__q0:
              start = cls[0]

        # After we have pruned states, a new transition table is needed.
        transitions = {}
        for state in states:
          transitions[state] = {}
          for alpha in self.__sigma:
            transitions[state][alpha] = map[self.__delta(state, alpha)]

        # Replace our new updated states.
        self.__Q  = states
        # Rest our new start state
        self.__a0 = start
        # Rebuild accepting states
        self.__F = [s for s in self.__F if s in states]
        # Transition table was rebuilt, redefine the delta lambda/thunk
        self.__delta   = (lambda s, a: transitions[s][a])

    # Myhill-Nerode DFA Minimization
    def minimize( self ):
      """
      Public api to minimize the DFA object.
      """
      # Trash un-needed states in the DFA.
      self.__Q = self.__reachable()
      self.__F = [q for q in self.__F if q in self.__Q]

      # Create new dfa given these equivalence duplications.
      self.__transform( self.__calc_equality() )

def usage(name):
  print "usage: %s <-w> <-p> <-h> inputfile" % name
  print "   -w : Write the minimized DFA to inputfile.min"
  print "   -p : (default) Output the minimized DFA to the screen, use when -w is also given."
  print "   -h : Print this help message."

# If the script is called directly then read input
if __name__ == '__main__':

  import sys,os

  # Initialize some structures
  states     = set()
  alphabet   = set()
  start      = ""
  accepting  = set()
  transitions = dict();

  if len( sys.argv ) < 2:
    print "No input dfa given"
    usage( sys.argv[0] )
    exit()

  prnt = True
  write = False

  if "-w" in sys.argv:
    write = True
    prnt = False

  if "-p" in sys.argv:
    prnt = True

  if "-h" in sys.argv:
    usage( sys.argv[0] )
    exit()

  ####################################
  # Open input file and parse contents
  # ----------------------------------
  # - "initial" defines initial DFA states.
  # - "final" - defines a comma separated list of final DFA states.
  # - Any line with three 
  # - Any line beginning with "#" will be ignored, it is comment.
  ####################################

  filename =  sys.argv[len(sys.argv)-1]

  file = open( filename, 'r' )

  for curr in file:
    line = curr.strip("\n")
    if line[0] is not "#":
      tokens = line.split(" ")
      if "initial" in line: initial = tokens[1]
      elif "final" in line: accepting = tokens[1].split( "," )
      else:
        src, on, dest = tokens[0], tokens[1], tokens[2]
        states.add( src )
        alphabet.add( on )
        states.add( dest )
        try:
          transitions[src][on] = dest
        except:
          transitions[src] = dict( { on : dest } )

  file.close()

  # Create a function we can use to map transitions.
  delta = ( lambda state, char: transitions[state][char] )

  # 5-tuple     (   Q   ,    Σ    ,   δ  ,   q0   ,     F     )
  dfa = minify( states, alphabet, delta, initial, accepting ) 

  dfa.minimize()

  if prnt:
    dfa.output()
  if write:
    dfa.write( filename + ".min" )
