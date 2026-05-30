import asyncio

MAX_CONCURRENT = 500 #not more than 500 connections at a time 

async def tcp_scan(target_ip, target_port, semaphore):
    pass













async def main():
    target_ip = input("\nWhat is your target's ip ?\n")
    target_port = int(input("\nWhat port you want to check?\n"))
    semaphore = asyncio.Semaphore(MAX_CONCURRENT)

asyncio.run(main())


















