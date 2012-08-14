# coding=UTF-8
from string import Template
import random
from commandbase import BaseCommand

class BenchmarkCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "benchmark" ]
        self.templates = [  Template("compares $name to $name and declares a no contest."),
                            Template("compares $name to $name and declares a breakeven."), 
                            Template("is disappointed with $name s fiscal performance."), 
                            Template("grabs his copy of Six Sigma for Dummies."), 
                            Template("presents $name with a tiny financial breakdown."), 
                            Template("audits his suppliers."),
                            Template("does something in Excel."), 
                            Template("blames Marketing."), 
                            Template("thinks $name would perform better if $name outsourced $name s drinking."), 
                            Template("puts on a super massive tiny suit."),
                            Template("tells $name to make a fucking appointment, just like $name did."), 
                            Template("whips out his calculator.") ]

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out
 