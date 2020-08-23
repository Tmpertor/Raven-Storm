#!/usr/bin/python
import CLIF_Framework.framework as framework

console = framework.console()
console.rsversion = "3"

framework.module("modules.main", console)

console.run()
