def move_zeros_to_left(arr):
    low = len(arr) - 1
    current_non_zero = len(arr) - 1
    while low >= 0:
        if arr[low] != 0:
            arr[current_non_zero] = arr[low]
            current_non_zero -= 1
        low -= 1
    while current_non_zero >= 0:
        arr[current_non_zero] = 0
        current_non_zero -= 1
    return arr


# def test(arr):
#     assert move_zeros_to_left(arr) == [0, 0, 1, 10, -1, 11, 5, -7, 25, -35]
#
#
# if __name__ == '__main__':
#     arr = [1, 10, -1, 11, 5, 0, -7, 0, 25, -35]
#     test(arr)
def possition(start, end, arr):
    while arr[start] != '':
        start += 1
    while arr[end] != '':
        end -= 1
    return start, end


import asyncio


async def hello_world_message() -> str:
    await asyncio.sleep(1)
    return 'Hello World!'

async def main() -> None:
    message = await hello_world_message()
    print(message)


import asyncio


async def delay(delay_seconds: int) -> int:
    print(f'sleeping for {delay_seconds} second(s)')
    await asyncio.sleep(delay_seconds)
    print(f'finished sleeping for {delay_seconds} second(s)')
    return delay_seconds


import asyncio


async def hello_every_second():
    for i in range(3):
        await asyncio.sleep(1)
        print("I'm running other code while I'm waiting!")


async def main():
    first_delay = asyncio.create_task(delay(4))
    second_delay = asyncio.create_task(delay(4))
    await hello_every_second()
    await first_delay
    await second_delay
asyncio.run(main())