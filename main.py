#!/usr/bin/python3
import CLIF_Framework.framework as framework

console = framework.console()
console.rsversion = "3.1.5"

framework.module("modules.main", console)

console.run()
