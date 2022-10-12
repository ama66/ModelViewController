# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 11:13:36 2022

@author: amohammed
"""
from model import Model 
from view import View
import tkinter as tk 
from tkinter import ttk 



##Controller
class Controller:
    def __init__(self):
        self.model=Model()
        self.view=View(self)
        
    def main(self):
        self.view.main()
        
    def on_button_click(self,caption):
       # print(f'button {caption} clicked')
        result=self.model.calculate(caption)
        self.view.value_var.set((result))

        
        
        
        

if __name__=='__main__':
    calculator=Controller()
    calculator.main()
        
        
