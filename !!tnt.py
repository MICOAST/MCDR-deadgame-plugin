# -*- coding: utf-8 -*-
from mcdreforged.api.all import *
import random

PLUGIN_METADATA = {
    'id': '死亡轮盘赌',
    'version': '1.0.0',
    'name': 'game of death',
    'description': 'a LITTEL GAME',
    'author': '浔钰',
    'link': '暂时没有qwq'
}

option_2 = None
weight = [0.5,0.5]
weights = [0,0]

def update_weights(new_weights): #修改权值
    global weight,weights
    try:
        weights[0]=int(new_weights[0])
        weights[1]=int(new_weights[1])
        total = sum(weights)
        if total == 100:
            weight = weights
            weight[0]=weights[0]/100
            weight[1]=weights[1]/100
            return f"§5权重已更新：§l输入者概率:§l{weight[0]},冤大头概率§l{weight[1]}"
        else:
            return "§5权重之和必须为§l100"
    except ValueError:
        return "§5无效的权重值格式"

def on_info(server, info):
    global option_2
    if info.content == '!!dead':
      option_1 = "{}".format(info.player)
      probability = [option_1]+[option_2]
      selected_option = random.choices(probability,weight)
      server.execute("/effect give {} minecraft:instant_damage 1 4".format(selected_option[0]))
      server.say("{}被魔法杀死了".format(selected_option[0]))

    if info.content == '!!dead help':
       server.say(f"§6输入者概率{weight[0]},冤大头概率{weight[1]},§c冤大头{option_2}")
       server.say(f"§3若要修改概率，请按以下命令修改。eg:§b!!dead config w:80,20")
       server.say(f"§3若要修改冤大头，请按以下命令修改。eg:§b!!dead config p:player")

    if info.content.startswith('!!dead config w:'):
        cmd_parts = info.content.split(":")
        result_message = update_weights(str(cmd_parts[1]).split(","))
        server.say(result_message)

    if info.content.startswith('!!dead config p:'):
        cmd_parts = info.content.split(":")
        server.say(f"§5成功修改冤大头为:§l{cmd_parts[1]}")
        option_2 = cmd_parts[1]
        



      

