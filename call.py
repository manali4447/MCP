from fastmcp import Client

client = Client("server.py")


async def main():
    async with client:
        result = await client.call_tool("add", {"a": "5", "b": 4})
        print(result)


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())