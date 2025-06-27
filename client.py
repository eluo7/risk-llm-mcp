import asyncio
from fastmcp import Client

# 配置MCP server地址
config = {
  "mcpServers": {
    "risk-llm": {
      "url": "http://127.0.0.1:8011/mcp",
      "transport": "streamable-http"
    }
  }
}

client = Client(config)

async def main():
    async with client:
        # print(f'Client connected: {client.is_connected()}')

        # # 0.列出所有工具
        # tools = await client.list_tools()
        # print(f'Available tools: {tools}')

        # 1.打招呼
        response = await client.call_tool("greet", {"name": "Alice"})
        print(f"1.打招呼: {response}\n")

        # 2.获取当前时间
        response = await client.call_tool("get_current_time")
        print(f"2.获取当前时间: {response}\n")

        # 3.生成随机数
        response = await client.call_tool("generate_random_number", {"min": 0, "max": 100})
        print(f"3.生成随机数: {response}\n")

        # 4.计算平方根
        response = await client.call_tool("calculate_square_root", {"number": 16})
        print(f"4.计算平方根: {response}\n")

        # 5.获取最新判决文书
        response = await client.call_tool("get_latest_judgment", {"credit_code": "91330105MADWLBFF2J"})
        print(f"5.获取最新判决文书: {response}\n")

        # 6.获取客户风险信息
        response = await client.call_tool("get_risk_info", {"credit_code": "91330105MADWLBFF2J"})
        print(f"6.获取客户风险信息: {response}\n")

    # Connection is closed automatically here
    # print(f'Client connection closed: {client.is_connected()}')

if __name__ == "__main__":
    asyncio.run(main())